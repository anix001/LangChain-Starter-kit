from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2:latest")

chain = prompt | model

chat_history = [] #Used a list to store message

# Set a initial system message
system_message = SystemMessage(content="You are a helpful assistant.")
# Append it to list
chat_history.append(system_message)



# Chat Loop 

while True:
   query = input("🧑‍🦳: ")
   if query.lower() == "exit":
      break
   chat_history.append(HumanMessage(content=query)) # Add User Message to Chat history

   #Get AI response using chat_history
   answer = chain.invoke(chat_history)
   chat_history.append(AIMessage(content=answer))  # Add AI Message to Chat history

   print(f"🤖: {answer}")

print("___ Chat History___")

print(chat_history)


