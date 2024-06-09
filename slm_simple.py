from llama_index.llms.ollama import Ollama
llm = Ollama(model="phi3", request_timeout=120.0, temperature=0)
resp = llm.complete("Who discovered Brasil?")
print(resp)