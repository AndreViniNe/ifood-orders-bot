<div align="center">

<p align="center">

  <a href="" rel="noopener">

<img width=300px height=150px src="https://www.neobyte.com.br/wp-content/uploads/2020/10/analytics.png" alt="Bot logo"></a>

</p>
 
<h3 align="center">Ifood Orders Bot</h3>

</div>
 
<div align="center">
 
  [![Status](https://img.shields.io/badge/status-active-success.svg)]()

  [![GitHub Issues](https://img.shields.io/github/issues/AndreViniNe/ifood-orders-bot.svg)](https://github.com/AndreViniNe/ifood-orders-bot/issues)

  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/AndreViniNe/ifood-orders-bot.svg)](https://github.com/AndreViniNe/ifood-orders-bot/pulls)

  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
 
</div>
 
---
 
<p align="center">
 
This repository contains all Ifood Orders Bot implementation utilizing phi3 SLM (Small Language Model) from LlamaIndex data framework to vectorize the selected documents.
  

</p>
 
## 📝 Table of Contents

+ [About](#about)

+ [Demo / Working](#demo)

+ [How it works](#working)

+ [Usage](#usage)

+ [Getting Started](#getting_started)

+ [Built Using](#built_using)

+ [Authors](#authors)

+ [Acknowledgments](#acknowledgement)
 
## 🧐 About <a class = "about"></a>

In this project, we utilize the RAG method to get a better response from the model based on a single/list of documents (in our case, JSON documents). The JSON documents are indexed together with the user query. Then these indexes are passed to the phi3 SLM (Small Language Model) from the Ollama framework, giving the user a response based on the context of all this. We can see all this process in the image below:

![About](/docs/images/llamaindex.webp)
 
## 🎥 Demo / Working <a class = "demo"></a>

Here, we can see the input and the output of the react agent RAG.

![](/docs/images/re_agent_code1.png)
![](/docs/images/re_agent_code2.png)
  
And here we can see the input and output of the simple RAG

![](/docs/images/simple_rag_code.png)
 
## 💭 How it works <a class = "working"></a>
 
The project is divided in parts:  
**Documents**: As the name says, they are specific documents that will be passed either directly to the model or via Nodes, that is, chunks of the document with specific characteristics that differentiate them (nodes are utilized in a normal RAG, not in the react agent). These documents can be of different types (.json, .pdf, .csv, etc.)  
**Index**: "Categorization" of the documents, so the Vetorization can be done easilly.  
**Vetorization**: Type of index that uses vector representations of text for efficient retrieval of relevant context. During query time, the VectorStoreIndex can quickly retrieve the most relevant nodes for a given query.  
**Query**: Question asked to the model by the user  
**Response**: LLM answer to the user question, based on the context, the documents and the answer, all of that together
 
## 🎈 Usage <a name = "usage"></a>
 
The user needs to run the Poetry command from the prerequisites tab, this way they will have all the necessary libraries for the project to work on their machine.  
The JSON files in the "Orders" folder are examples of pizzeria orders that ChatGPT made. The user can place orders for any type of establishment, as long as it is in a JSON file, otherwise the reading of the document in the RAG .py file will have to be changed  
The .py files can be executed having a query to be passed to the SLM (Small Language Model). 
 
 
## 🏁 Getting Started <a name = "getting_started"></a>
 
### Prerequisites

*Poetry installation* -> Check the official documentation below  
All the other installation prerequisites are in the file **pyproject.toml**. The only thing needed is a command in Terminal to install all the dependencies:  
  
*poetry install --no--root*  
  
*Documents* -> All of the documents needs to be created and moved to the "Orders" folder
  

## ⛏️ Built Using <a name = "built_using"></a>

+ [Llama Index](https://docs.llamaindex.ai/en/stable/) - Python Data Framework for LLM or SLM applications

+ [Poetry](https://python-poetry.org/docs/) - Python packaging and dependency management made easy

+ [PyEnv](https://github.com/pyenv/pyenv) - Simple Python Version Management
 
## ✍️ Authors <a name = "authors"></a>

+ [@André Vinícius](andrevini.neves@gmail.com) - Project Development

 
## 🎉 Acknowledgements <a name = "acknowledgement"></a>
 
Articles, websites and official documentations that helped me building this project  
+ Medium articles   
[Question answering in RAG using LlamaIndex](https://medium.com/@aneesha161994/question-answering-in-rag-using-llama-index-92cfc0b4dae3)   
[Advanced RAG using LlamaIndex](https://medium.aiplanet.com/advanced-rag-using-llama-index-e06b00dc0ed8)  
  
+ LlamaIndex official website  
[Embedding using HuggingFace](https://docs.llamaindex.ai/en/stable/examples/embeddings/huggingface/)  
[ReAct Agent RAG](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/)