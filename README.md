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
 
This repository contains all Ifood Orders Bot implementation utilizing phi3 SLM (Small Language Model) from Microsoft with LlamaIndex data framework to vectorize the selected documents.
  

</p>
 
## 📝 Table of Contents

+ [About](#about)

+ [Demo / Working](#demo)

+ [How it works](#working)

+ [Usage](#usage)

+ [Getting Started](#getting_started)

+ [Deploying your own bot](#deployment)

+ [Built Using](#built_using)

+ [Authors](#authors)

+ [Acknowledgments](#acknowledgement)
 
## 🧐 About <a name = "about"></a>

In this project, we utilize the RAG method to get a better response from the model based on a single/list of documents (in our case, JSON documents). The JSON documents are indexed together with the user query. Then these indexes are passed to the phi3 SLM (Small Language Model), giving the user a response based on the context of all this. We can see all this process in the image below:

![About](/docs/images/llamaindex.webp)
 
## 🎥 Demo / Working

Here, we can see the input and the output of the react agent RAG.

![](/docs/images/re_agent_code1.png)
![](/docs/images/re_agent_code2.png)
 
## 💭 How it works
 
Descreva como o modulo(s) funciona, suas entradas e saída, aqui pode ser adicionado diagramas de sequencia (UML) ou algum outro diagrama de simples entendimento do fluxo do modulo, especificar no desenho geral do projeto onde esse modulo se encontra também é valido. Detalhes de como foi desenvolvido e o porque da escolha da tecnologia são importantes. Também detalhes técnicos de requisitos de usuário, por exemplo acuracia do modelo ou latência de rede, autenticação de grupos de usuários, quais grupos.
 
## 🎈 Usage <a name = "usage"></a>
 
Nesse bloco deve ser apresentado como utilizar o modulo que já foi feito o deploy, especificar onde estão todas as instancias e recursos por exemplo, dev, stg e prd, com os id's especificos na nuvem ou hostname onprem para que o leitor consiga encontrar os recursos caso precise. Especificar para onde estão indo os logs, os tipos de logs, os erros mais comuns, como a interface funciona, quais as opções do usuário na interface, por ex, se backend link para swagger e breve descrição geral das funções.
 
 
## 🏁 Getting Started <a name = "getting_started"></a>

Nessa etapa, deve ser mostrado como montar o ambiente local para desenvolvimento, especificar com exemplos como rodar, como testar, como debugar, como buildar, pre-requisitos de instalação para rodar localmente este modulo, detalhes do deploy do modulo na nuvem ou onpremisse.
 
### Prerequisites
 
All the installation prerequisites are in the file **pyproject.toml**. The only thing needed is a command in Terminal to install all the dependencies:  
  
*poetry install --no--root*
 
### Installing
 
Passo-passo para rodar local subtopico de getting started.
 
 
## ⛏️ Built Using <a name = "built_using"></a>

+ [Llama Index](https://docs.llamaindex.ai/en/stable/) - Python Data Framework for LLM or SLM applications

+ [Poetry](https://python-poetry.org/docs/) - Python packaging and dependency management made easy

+ [PyEnv](https://github.com/pyenv/pyenv) - Simple Python Version Management
 
## ✍️ Authors <a name = "authors"></a>

+ [@André Vinícius](andrevini.neves@gmail.com) - Project Development

 
## 🎉 Acknowledgements <a name = "acknowledgement"></a>
 
+ Referencias externas ou a projetos com relação, por exemplo pode especificar todos os repos que tem relação com este projeto no smartmix