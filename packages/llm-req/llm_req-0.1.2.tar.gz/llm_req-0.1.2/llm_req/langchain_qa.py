import os
from .struct import Document, KnowledgeCompletionRequest, KnowCompletionResponse,ChatMessage, DocsRequest, NoneRequest, KnowDocs
import json
from typing import List,Any, Optional, Dict
import requests

def quick_cut_as_docs(lang_doc:str, source=None,**metadata):
    docs = []
    paragraph = ""
    if "source" in metadata and metadata["source"]  is not None and isinstance(metadata["source"],str):
        if source is None:
            source = metadata["source"]

    for no,line in enumerate(lang_doc.split("\n")):
        if no == 0 and source == None:
            source = line.strip()
        if line.strip() == "":continue
        
        paragraph += "\n"+line
        if len(paragraph) > 100:
            startat = lang_doc.index(paragraph)
            endat = startat + len(paragraph)
            metadata["source"] = source + ":"+str(startat)+":"+str(endat)
            docs.append(Document(page_content=paragraph, metadata=metadata))
            paragraph = ""
    if len(paragraph) > 0:
        startat = lang_doc.index(paragraph)
        endat = startat + len(paragraph)
        metadata["source"] = source + ":"+str(startat)+":"+str(endat)
        docs.append(Document(page_content=paragraph, metadata=metadata))
    
    return docs


class QA:

    id: str = "chatglm3-6b-128k"
    max_tokens: int = 50000
    temperature: float = 0.01
    top_p = 0.9
    history = []
    history_id = "default"
    tokenizer = None
    model  = None
    history_len: int = 10
    model  = None
    tokenizer  = None
    cpu: bool = False
    streaming: bool = True
    system:str = "You are ChatGLM3, a helpful assistant. Follow the user's instructions carefully. Respond using markdown."
    verbose: bool = False
    knowledge_id: str = None
    remote_host  = None

    def __init__(self, remote_host, knowledge_id=None):
        self.remote_host = remote_host
        self.knowledge_id = knowledge_id
        
        

    def use_knowledge(self, knowledge_id):
        self.knowledge_id = knowledge_id

    def list_knowledges(self):
        session = requests.Session()
        n = NoneRequest(id="None")
        data = n.dict()
        return session.post(f"http://{self.remote_host}:15001/v1/knowledge/list", json=data).json()
    
    def upload(self, lang_docs):
        req = DocsRequest(
            docs=lang_docs,
            id=self.knowledge_id,
            stream=self.streaming,
        )
        data = req.dict()
        response = requests.post(f"http://{self.remote_host}:15001/v1/knowledge/upload", json=data, stream=self.streaming)
        return response.json()
    
    def delete(self):
        assert self.knowledge_id is not None
        session = requests.Session()
        req = DocsRequest(
            docs=[],
            id=self.knowledge_id,
        )
        data = req.dict()
        response = session.post(f"http://{self.remote_host}:15001/v1/knowledge/delete", json=data, stream=self.streaming)
        return response.json()

    def answer(self, question):
        assert self.knowledge_id is not None
        msgs = self.history
        msgs.append(ChatMessage(role="user", content=question))
        return self.create_chat_completion(f"http://{self.remote_host}:15001/v1/knowledge/answer", msgs, temperature=self.temperature, top_p=self.top_p, max_tokens=self.max_tokens, model=self.id, use_stream=self.streaming)

    def search(self, query):
        assert self.knowledge_id is not None
        req = KnowledgeCompletionRequest(
            model="", 
            functions=None,
            messages=[ChatMessage(role="user", content=query)],
            top_p=0,
            temperature=0,
            stream=True,
            max_tokens=9999,
            knowledge_id=self.knowledge_id,
        )
        data = req.dict()
        res = requests.post(f"http://{self.remote_host}:15001/v1/knowledge/search", json=data, stream=True)
        return res.json()

    def create_chat_completion(self, url, messages, functions=None, use_stream=True,model="chatglm3-6b-128k",temperature=0.8,top_p=0.8, max_tokens=8000):
        req = KnowledgeCompletionRequest(
            model=model, 
            functions=functions,
            messages=messages,
            top_p=top_p,
            temperature=temperature,
            stream=use_stream,
            max_tokens=max_tokens,
            knowledge_id=self.knowledge_id,
        )
        data = req.dict()
        
        response = requests.post(url, json=data, stream=use_stream)
        if response.status_code == 200:
            if use_stream:
                # 处理流式响应
                
                for line in response.iter_lines():
                    if line:
                        
                        decoded_line = line.decode('utf-8')[6:]
                        try:
                            if decoded_line.strip():
                                response_json = json.loads(decoded_line.strip())
                                
                                c = KnowCompletionResponse.from_dict(response_json)
                                # import ipdb;ipdb.set_trace()
                                if c.choices[-1].finish_reason == "stop":
                                    yield c
                                    break
                                elif c.choices[-1].finish_reason == "function_call":
                                    yield c
                                    break
                                
                                yield c
                                
                        except Exception as e:
                            # cprint(decoded_line,'red')
                            
                            # raise e
                            pass
            else:
                # 处理非流式响应
                decoded_line = response.json()
                # content = decoded_line.get("choices", [{}])[0].get("message", "").get("content", "")
                yield KnowCompletionResponse.parse_obj(decoded_line)
        else:
            print("Error:", response.status_code)
            return None
try:
    import langchain
    from langchain.vectorstores import FAISS
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.prompts import PromptTemplate
    from langchain.chains import RetrievalQA

    from contextlib import contextmanager
    # from gptcache.processor.pre import get_prompt
    # from gptcache.manager.factory import get_data_manager
    from langchain.globals import set_llm_cache
    from gptcache import Cache
    from gptcache.manager.factory import manager_factory
    from gptcache.processor.pre import get_prompt
    from langchain.cache import GPTCache

    from langchain.cache import GPTCache
    from termcolor import colored
    import pathlib
    from typing import Any, AsyncIterator,cast, Literal, Union
    import asyncio
    from langchain.callbacks.streaming_aiter import AsyncCallbackHandler
    from langchain.chains.query_constructor.base import AttributeInfo
    from langchain.retrievers.self_query.base import SelfQueryRetriever
    from loguru import logger

    DEFAULT_EMBEDDING_PATH = str(pathlib.Path.home() / ".cache" / "chatglm-embedding" / "base-embedding")

    DEFAULT_LOCAL_QA_VS_PATH = str(pathlib.Path.home() / ".cache" / "media_collect"/"vec"/"vec_cache")

    DEFAULT_CACHE_MAP_PATH = str(pathlib.Path.home() / ".cache" / "local_qa_cache_map")
    if not os.path.exists(DEFAULT_LOCAL_QA_VS_PATH):
        os.makedirs(DEFAULT_LOCAL_QA_VS_PATH)

    i = 0
    # file_prefix = "data_map"
    def load_embedding(model_path=DEFAULT_EMBEDDING_PATH):
        try:
            print(colored("Loading embeddings...", "green"))
            return HuggingFaceEmbeddings(model_name=model_path)
        finally:
            print(colored("Embeddings loaded.", "green"))

    # def init_gptcache_map(cache_obj: gptcache.Cache):
    #     global i
    #     cache_path = f'{DEFAULT_CACHE_MAP_PATH}_{i}.txt'
    #     cache_obj.init(
    #         pre_embedding_func=get_prompt,
    #         data_manager=get_data_manager(data_path=cache_path),
    #     )
    #     i += 1

    import hashlib


    def get_hashed_name(name):
        return hashlib.sha256(name.encode()).hexdigest()


    def init_gptcache(cache_obj: Cache, llm: str):
        hashed_llm = get_hashed_name(llm)
        cache_obj.init(
            pre_embedding_func=get_prompt,
            data_manager=manager_factory(manager="map", data_dir=f"{DEFAULT_CACHE_MAP_PATH}map_cache_{hashed_llm}"),
        )



    set_llm_cache(GPTCache(init_gptcache))

    # langchain.llm_cache = GPTCache(init_gptcache_map)


    class KnowdageQA:
            
        @classmethod
        def create_from_local(cls,kn_name ,docs, embeddings, vs_path=DEFAULT_LOCAL_QA_VS_PATH):
            vs_path = pathlib.Path(vs_path) / kn_name
            print("kn name:", kn_name)
            cls.save_loaders(docs, embeddings=embeddings,vs_path=vs_path)


        def __init__(self,llm,embeddings=None, vs_path=DEFAULT_LOCAL_QA_VS_PATH, max_history_len=1, top_k=7):
            self.embeddings = embeddings
            if self.embeddings is  None:
                self.embeddings = load_embedding(model_path=DEFAULT_EMBEDDING_PATH)

            self.db = None
            self.vs_path_dir = vs_path
            self.llm = llm
            self.top_k = top_k
            self.max_history_len = max_history_len
            self.history = self.llm.history

            # if len(self.llm.callbacks) == 2:
            #     self.llm.callbacks[1] = QACallbacks()

        def load(self, name):
            self.db = FAISS.load_local( str(pathlib.Path(self.vs_path_dir)/name), self.embeddings)

        @classmethod
        def save_loaders(cls,docs, embeddings=None, vs_path=DEFAULT_LOCAL_QA_VS_PATH, model_path=DEFAULT_EMBEDDING_PATH):
            if embeddings is None:
                embeddings = load_embedding(model_path=model_path)

            if os.path.isdir(vs_path) and os.path.exists(str(pathlib.Path(vs_path) / "index.faiss")):
                db = FAISS.load_local(vs_path, embeddings)
                db.add_documents(docs)
            else:
                db = FAISS.from_documents(docs, embeddings)
            db.save_local(vs_path)
            return db

        @contextmanager
        def with_context(self, history):
            try:
                old_history = self.history
                self.history = history
                yield
            finally:
                self.history = old_history
        
        def get_chains(self):
            assert self.db is not None
            prompt_template = """基于以下已知信息，简洁和专业的来回答用户的问题。
            如果无法从中得到答案，请说 "没有提供足够的相关信息"，不允许在答案中添加编造成分。
            
            已知内容:
            {context}
            
            问题:
            {question}"""
            prompt = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )
            if len(self.history) > self.max_history_len:
                self.history = self.history[-self.max_history_len:]
            self.llm.history = self.history

            
            # vector_store = FAISS.load_local(vs_path, self.embeddings)
            # knowledge_chain = RetrievalQA.from_chain_type(
            #     llm=self.llm,
            #     chain_type="map_reduce",
            #     retriever=self.db.as_retriever(search_kwargs={"k": self.top_k}),
            #     # chain_type_kwargs={"prompt":prompt},
            #     return_source_documents=True)
            
            knowledge_chain = RetrievalQA.from_llm(
                llm=self.llm,
                retriever=self.db.as_retriever(search_kwargs={"k": self.top_k}),
                prompt=prompt,
            )
            knowledge_chain.combine_documents_chain.document_prompt = PromptTemplate(
                input_variables=["page_content"], template="{page_content}"
            )

            knowledge_chain.return_source_documents = True
            return knowledge_chain
        
        def answer(self, question):
            assert self.db is not None
            prompt_template = """基于以下已知信息，简洁和专业的来回答用户的问题。
如果无法从中得到答案，请说 "没有提供足够的相关信息"，不允许在答案中添加编造成分。
            
<已知内容>:
    {context}
            
<问题>:
    {question}"""
            summary_prompt_template = """总结合并所有得到的内容
<已知内容>:
    {context}
            
<问题>:
    {question}"""
            prompt = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )
            if len(self.history) > self.max_history_len:
                self.history = self.history[-self.max_history_len:]
            self.llm.history = self.history
            docs = self.db.similarity_search(question, k=self.top_k)
            _pr = prompt.format(context="\n".join([i.page_content for i in docs]), question=question)
            if len(_pr) > self.llm.max_tokens - 1000:
                ps = []
                
                chain = self.llm.copy_llm()
                chain.history = []
                ans = []
                
                # def _an(llm,q,s):
                #     res = await llm.apredict(q)
                #     return {"response":res, "sources":s}
                
                a_tasks = []
                for doc in docs:
                    
                    _p = prompt.format(context="\n".join([i.page_content for i in ps]), question=question)
                    if len(_p) + len(doc.page_content) > self.llm.max_tokens - 1000:
                        new_chain = chain.copy_llm()
                        new_chain.cache = False
                        logger.info(f"Use Source: {len(ps)} Contex: {len(_p)}")
                        for a in new_chain.stream(_p):
                            a["sources"] = ps.copy()
                            yield a
                        
                        ps = []
                        
                    ps.append(doc)
                if len(ps) > 0:
                    _p = prompt.format(context="\n".join([i.page_content for i in ps]), question=question)
                    if len(_p) + len(doc.page_content) > self.llm.max_tokens - 1000:
                        new_chain = chain.copy_llm()
                        new_chain.cache = False
                        logger.info(f"Use Source: {len(ps)} Contex: {len(_p)}")
                        for a in new_chain.stream(_p):
                            a["sources"] = ps.copy()
                            yield a
            else:
                chain = self.llm.copy_llm()
                chain.history = []
                new_chain = chain.copy_llm()
                for a in new_chain.stream(_pr):
                    a["sources"] = docs
                    yield a
                # return {"response":res, "sources":docs}

        async def aanswer(self, question):
            assert self.db is not None
            prompt_template = """基于以下已知信息，简洁和专业的来回答用户的问题。
            如果无法从中得到答案，请说 "没有提供足够的相关信息"，不允许在答案中添加编造成分。
            
            已知内容:
            {context}
            
            问题:
            {question}"""
            summary_prompt_template = """总结合并所有得到的内容
            已知内容:
            {context}
            
            问题:
            {question}"""
            prompt = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )
            if len(self.history) > self.max_history_len:
                self.history = self.history[-self.max_history_len:]
            self.llm.history = self.history
            docs = self.db.similarity_search(question, k=self.top_k)
            _pr = prompt.format(context="\n".join([i.page_content for i in docs]), question=question)
            if len(_pr) > self.llm.max_tokens - 1000:
                ps = []
                
                chain = self.llm.copy_llm()
                chain.history = []
                ans = []
                
                async def _an(llm,q,s):
                    res = await llm.apredict(q)
                    return {"response":res, "sources":s}
                
                a_tasks = []
                for doc in docs:
                    
                    _p = prompt.format(context="\n".join([i.page_content for i in ps]), question=question)
                    if len(_p) + len(doc.page_content) > self.llm.max_tokens - 1000:
                        new_chain = chain.copy_llm()
                        new_chain.cache = False
                        logger.info(f"Use Source: {len(ps)} Contex: {len(_p)}")
                        a_tasks.append(asyncio.create_task(_an(new_chain, _p, ps.copy())))
                        # res = await asyncio.ensure_future(new_chain.apredict(_p))
                        # ans.append({"response":res, "sources":ps})
                        ps = []
                        
                    ps.append(doc)
                if len(ps) > 0:
                    _p = prompt.format(context="\n".join([i.page_content for i in ps]), question=question)
                    if len(_p) + len(doc.page_content) > self.llm.max_tokens - 1000:
                        new_chain = chain.copy_llm()
                        new_chain.cache = False
                        logger.info(f"Use Source: {len(ps)} Contex: {len(_p)}")
                        a_tasks.append(asyncio.create_task(_an(new_chain, _p, ps.copy())))
                        # res = await asyncio.ensure_future(new_chain.apredict(_p))
                        # ans.append({"response":res, "sources":ps})
                        ps = []
                for a in await asyncio.gather(*a_tasks):
                    logger.info(f"- {a['response']}")
                    ans.append(a)

                if len(ans) > 0:
                    new_chain = chain.copy_llm()
                    new_chain.cache = False
                    sours = []
                    for i in ans:
                        sours += i["sources"]
                    
                    prompt = PromptTemplate(
                        template=summary_prompt_template,
                        input_variables=["context", "question"]
                    ) 
                    p = prompt.format(context="\n".join([i["response"] for i in ans]), question=question)
                    res = await new_chain.apredict(p)
                    return res, sours
            else:
                new_chain = chain.copy_llm()
                res = await new_chain.acall(_p)
                return {"response":res, "sources":docs}

        def get_self_query_chains(self, persistent_path):
            from langchain.vectorstores import Chroma
            db = Chroma(persist_directory=persistent_path, embedding_function=self.embeddings)
            metadata_field_info = [
                AttributeInfo(
                    name="title",
                    description="The news's title",
                    type="string"
                ),
                AttributeInfo(
                    name="date",
                    description="The news's publish datetime",
                    type="string"
                ),
                AttributeInfo(
                    name="desc",
                    description="The news's short description",
                    type="string"
                ),
                AttributeInfo(
                    name="keywords",
                    description="The news's some import keywords",
                    type="string"
                ),
                AttributeInfo(
                    name="url",
                    description="The url for news's raw source.",
                    type="string"
                ),
                AttributeInfo(
                    name="source",
                    description="which media publish this news.",
                    type="string"
                ),
                AttributeInfo(
                    name="text",
                    description="The news's all content.",
                    type="string"
                ),
            ]

            knowledge_chain = SelfQueryRetriever.from_llm(
                self.llm,
                db,
                "Brief summary of a news",
                metadata_field_info,
            )
            # knowledge_chain.combine_documents_chain.document_prompt = PromptTemplate(
            #     input_variables=["page_content"], template="{page_content}"
            # )
            # knowledge_chain.return_source_documents = True
            return knowledge_chain

        async def agenerate(self, query):
            assert self.db is not None
            prompt_template = """基于以下已知信息，简洁和专业的来回答用户的问题。
            如果无法从中得到答案，请说 "根据已知信息无法回答该问题" 或 "没有提供足够的相关信息"，不允许在答案中添加编造成分。
            
            已知内容:
            {context}
            
            问题:
            {question}"""
            prompt = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )
            if len(self.history) > self.max_history_len:
                self.history = self.history[-self.max_history_len:]
            self.llm.history = self.history
            # vector_store = FAISS.load_local(vs_path, self.embeddings)
            knowledge_chain = RetrievalQA.from_llm(
                llm=self.llm,
                retriever=self.db.as_retriever(search_kwargs={"k": self.top_k}),
                prompt=prompt
            )
            knowledge_chain.combine_documents_chain.document_prompt = PromptTemplate(
                input_variables=["page_content"], template="{page_content}"
            )

            knowledge_chain.return_source_documents = True
            result = await asyncio.ensure_future(knowledge_chain.acall({"query": query}))
            
            # result = knowledge_chain({"query": query})
            # self.llm.history[-1][0] = query
            self.history = self.llm.history
            return result
        
        def set_callbacks(self, callbacks):
            self.llm.callbacks = [callbacks]
        
        @classmethod
        def QuickParseAsDocs(cls, lang_doc, source=None,**metadata):
            return quick_cut_as_docs(lang_doc, source=source, **metadata)

        def __call__(self, query):
            assert self.db is not None
            prompt_template = """基于以下已知信息，简洁和专业的来回答用户的问题。
            如果无法从中得到答案，请说 "根据已知信息无法回答该问题" 或 "没有提供足够的相关信息"，不允许在答案中添加编造成分。
            
            已知内容:
            {context}
            
            问题:
            {question}"""
            prompt = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )
            if len(self.history) > self.max_history_len:
                self.history = self.history[-self.max_history_len:]
            self.llm.history = self.history
            # vector_store = FAISS.load_local(vs_path, self.embeddings)
            knowledge_chain = RetrievalQA.from_llm(
                llm=self.llm,
                retriever=self.db.as_retriever(search_kwargs={"k": self.top_k}),
                prompt=prompt
            )
            knowledge_chain.combine_documents_chain.document_prompt = PromptTemplate(
                input_variables=["page_content"], template="{page_content}"
            )

            knowledge_chain.return_source_documents = True
            result = knowledge_chain({"query": query})
            # self.llm.history[-1][0] = query
            self.history = self.llm.history
            return result, self.llm.history
        

    class QACallbacks(AsyncCallbackHandler):
        queue: asyncio.Queue[Any]
        done: asyncio.Event

        @property
        def always_verbose(self) -> bool:
            return True

        def __init__(self) -> None:
            self.queue = asyncio.Queue()
            self.done = asyncio.Event()
        
        async def on_msg(self, msg, **data):
            print(msg, end="",flush=True)

        async def on_result(self, result,run_id=None, **kargs):
            print("\n--- end ---",kargs)

        async def on_llm_start(self, *args, **kargs):
            pass
        async def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
            
            if token is not None and token != "":
                await self.on_msg(token, **kwargs)

        async def on_llm_end(self, response: Any,verbose=False, **kwargs: Any) -> None:
            await self.on_result(response, **kwargs)

        async def on_llm_error(self, error: BaseException, **kwargs: Any) -> None:
            self.done.set()
    
except Exception as e:
    print(e)



    
