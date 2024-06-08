import os

API_KEY = os.environ["LLAMA_CLOUD_API_KEY"]

#method 2:automatically sets the metadata of each document according to filename_fn
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

parser = LlamaParse(
    api_key=API_KEY,
    result_type="markdown",  # "markdown" and "text" are available
    verbose=True,
)

filename_fn = lambda filename: {"file_name": filename}
file_extractor = {".csv": parser}
documents = SimpleDirectoryReader(
    "./orders", file_extractor=file_extractor, file_metadata=filename_fn
).load_data()

print(documents)