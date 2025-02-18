from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_ollama.llms import OllamaLLM


model = OllamaLLM(model="llama3.2:latest")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts.")
    ]
)

# Create  the combined  chain using Langchain Expression Language(LCEL)

chain = prompt_template | model | StrOutputParser()

#Run the chain
result = chain.invoke({
  "animal":"cat",
  "fact_count": 2
})

# Output
print(result)


