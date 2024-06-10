from llama_index.core import SimpleDirectoryReader, ServiceContext, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.postprocessor import MetadataReplacementPostProcessor

def read_files(folder: str) -> list:
    """Read all files in a folder and load them into a list"""
    filename_fn = lambda filename: {"file_name": filename}
    documents = SimpleDirectoryReader(
        folder, file_metadata=filename_fn
    ).load_data()
    return documents

def create_index(embeded_model: str, slm_model="phi3", timeout=120.0, temp=0.75, **kwargs):
    """Create a context based on a embeded model. Creates Nodes, 
    which are portions of the document that contain similar characteristics. 
    The context receives as parameters the SLM, the Nodes and the embeded model, 
    and then this context is passed as a parameter for vectorization"""
    documents = read_files("./orders")
    embed_model = HuggingFaceEmbedding(model_name=embeded_model)

    base_node_parser = SimpleNodeParser()
    base_nodes = base_node_parser.get_nodes_from_documents(documents)

    llm = Ollama(model=slm_model, request_timeout=timeout, temperature=temp)

    ctx_base = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model,
        node_parser=base_nodes)

    base_index = VectorStoreIndex(
        base_nodes,
        service_context=ctx_base)
    return base_index

def query_response():
    """Create a query engine based on the index and the nodes postprocessor that the query engine will use to 'learn'.
    Ask the user to make a question to the model and returns the answer of the model to the question"""
    base_index = create_index("BAAI/bge-large-en-v1.5")
    base_query_engine = base_index.as_query_engine(
        similarity_top_k=5,
        verbose=True,
        node_postprocessor=[
            MetadataReplacementPostProcessor("window")
            ],
        )

    query = str(input("Ask the model a question: "))
    response = base_query_engine.query(query)

    print(response)

def main():
    query_response()

if __name__ == "__main__":
    main()