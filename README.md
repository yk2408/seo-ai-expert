# SEO AI Expert

A repository for an AI Chat bot who is specialised in SEO. 

This is a web application is using a Pinecone as a vectorsotre 
and answers questions about Best SEO strategies and anything about SEO.

## Tech Stack
Client: Streamlit

Server Side: LangChain 🦜🔗

Vectorstore: Pinecone 🌲

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PINECONE_API_KEY`
`OPENAI_API_KEY`
`TAVILY_API_KEY`
`LANGCHAIN_API_KEY`

Rename sample.env file to .env and add your API keys to run the project.

## Run Locally

Clone the project

```bash
  git clone https://github.com/yk2408/seo-ai-expert.git
```

Go to the project directory

```bash
  cd seo-ai-expert
```

Download LangChain Documentation
```bash
  mkdir langchain-docs
  wget -r -A.html -P langchain-docs  https://api.python.langchain.com/en/latest
```

Install dependencies

```bash
  pipenv install
```

Start the flask server

```bash
  streamlit run main.py
```


## Running Tests

To run tests, run the following command

```bash
  pipenv run pytest .
```