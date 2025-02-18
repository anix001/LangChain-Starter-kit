from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

messages = [
    SystemMessage("You are expert in Full stack development."),
    HumanMessage("Give me a short code of react.js")
]

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2:latest")

chain = prompt | model

answer = chain.invoke(messages)
print(answer)