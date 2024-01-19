# PyNlux 🌲

This project contains the source code for the demo server and APIs used on the [NLUX.ai](https://nlux.ai) 
website.<br />These APIs are built using **LangChain**, **LangServe**, and **OpenAI".

They are currently being served via Heroku, and this repository contains related Heroku config files.

## Creating Conversational AI Interfaces with NLUX

NLUX (for _Natural Language User Experience_) is an open-source Javascript library that makes it simple to integrate
powerful Large Language Models like ChatGPT into your web app or website. With just a few lines of code, 
you can add conversational AI capabilities and interact with your favourite LLM.

In addition to the UI AiChat component, NLUX also provides [adapters to connect to several LLMs](https://docs.nlux.ai/learn/adapters) 
such as the OpenAI models, Hugging Face, and LangChain.

Visit [NLUX.ai](https://nlux.ai) for examples, documentation, and to learn more.

## Repository Content

If you are interested in learning how to use LangChain to build an API powered by LLM, or you are
just curious about how the NLUX demo APIs works, you can check the folders in this repository:

* `./app` ― The FastAPI endpoint and web server.
* `./packages` ― Several Python packages matching different endpoints.

## Building + Running This Project

Please check `./pipeline/README.md` in this repository for further instructions on how to build and run this 
project on your local dev machine or server.
