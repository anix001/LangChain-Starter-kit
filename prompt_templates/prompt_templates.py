from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """ Write a{tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a 
key strength. keep it to max 4 lines"""


prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2:latest")

chain = prompt | model

msg = chain.invoke({
    "tone": "energetic",
    "company": "Samsung",
    "position": "AI Engineer",
    "skill":"AI"
    })
print(msg)