from llama_index.core import SimpleDirectoryReader, ServiceContext, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.postprocessor import MetadataReplacementPostProcessor

filename_fn = lambda filename: {"file_name": filename}
documents = SimpleDirectoryReader(
    "./orders", file_metadata=filename_fn
).load_data()

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-large-en-v1.5")

base_node_parser = SimpleNodeParser()
base_nodes = base_node_parser.get_nodes_from_documents(documents)

llm = Ollama(model="phi3", request_timeout=120.0, temperature=0)

ctx_base = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
    node_parser=base_nodes)

base_index = VectorStoreIndex(
    base_nodes,
    service_context=ctx_base)

base_query_engine = base_index.as_query_engine(
    similarity_top_k=5,
    verbose=True,
    node_postprocessor=[
        MetadataReplacementPostProcessor("window")
        ],
    )

query_orders = "What are the names of the people that made the orders?"
response_orders = base_query_engine.query(query_orders)

print(response_orders)