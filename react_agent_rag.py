from llama_index.core import SimpleDirectoryReader, ServiceContext, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool, QueryEngineTool, ToolMetadata

def add(a: float, b: float) -> float:
   """Add two integers and returns the result integer"""
   return a + b

def read_files(folder: str) -> list:
    """Read all files in a folder and load them into a list"""
    filename_fn = lambda filename: {"file_name": filename}
    documents = SimpleDirectoryReader(
        folder, file_metadata=filename_fn
    ).load_data()
    return documents

def create_index(model: str):
    """Create a context based on a embeded model. Then this context 
    is sent to be vectorized together with the documents. This 
    vector indexing will be passed to the SLM model"""
    embed_model = HuggingFaceEmbedding(model_name=model)
    ctx_base = ServiceContext.from_defaults(
        embed_model=embed_model,
        llm=None
    )

    documents = read_files("./orders")
    base_index = VectorStoreIndex.from_documents(documents, service_context=ctx_base)
    return base_index

def slm_agent(model="phi3", timeout=120.0, temp=0.75, **kwargs):
    """Create a query engine based on the index and tools that the query engine will use to 'learn'.
    Create the model from Ollama and pass it as a parameter with the Query Engine to the agent"""
    base_index = create_index("BAAI/bge-large-en-v1.5")
    base_engine = base_index.as_query_engine(similarity_top_k=3)

    add_tool = FunctionTool.from_defaults(fn=add)
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

    slm = Ollama(model=model, request_timeout=timeout, temperature=temp)
    agent = ReActAgent.from_tools(
        query_engine_tools,
        llm=slm,
        verbose=True,
        # context=context
    )
    return agent

def query_response():
    """Ask the user to make a question to the Agent and returns the answer of the Agent to the question"""
    prompt = str(input("Ask the model a question: "))
    agent = slm_agent()
    agent.chat(prompt)


if __name__ == "__main__":
    query_response()