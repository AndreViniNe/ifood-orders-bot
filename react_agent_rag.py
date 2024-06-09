from llama_index.core import SimpleDirectoryReader, ServiceContext, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool, QueryEngineTool, ToolMetadata

def add(a: float, b: float) -> float:
   """Add two integers and returns the result integer"""
   return a + b

add_tool = FunctionTool.from_defaults(fn=add)

filename_fn = lambda filename: {"file_name": filename}
documents = SimpleDirectoryReader(
    "./orders", file_metadata=filename_fn
).load_data()

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-large-en-v1.5")
ctx_base = ServiceContext.from_defaults(
    embed_model=embed_model,
    llm=None
)

base_index = VectorStoreIndex.from_documents(documents, service_context=ctx_base)
print(dir(base_index))

base_engine = base_index.as_query_engine(similarity_top_k=3)

query_engine_tools = [
    QueryEngineTool(
        query_engine=base_engine,
        metadata=ToolMetadata(
            name="base_query_orders",
            description=(
                "Provide informations about the total price of the orders"
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ), add_tool
]

llm = Ollama(model="phi3", request_timeout=120.0, temperature=0)
agent = ReActAgent.from_tools(
    query_engine_tools,
    llm=llm,
    verbose=True,
    # context=context
)

response = agent.chat("What was the total price of the orders?")
print(str(response))
