from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_ollama.llms import OllamaLLM


model = OllamaLLM(model="llama3.2:latest")

animal_fact_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are facts expert who knows facts about {animal}."),
        ("human", "Tell me {count} facts.")
    ]
)

# Define a prompt template for translation to French
translation_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator and convert the provided text into {language}."),
        ("human", "Translate the following text to {language}:{text}"),
    ]
)

# Define additional processing steps using RunnableLambda
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")
prepare_for_translation = RunnableLambda(lambda output:{"text":output, "language":"french"})

# Create  the combined  chain using Langchain Expression Language(LCEL)

chain = animal_fact_template | model | StrOutputParser() | prepare_for_translation |translation_template | model | StrOutputParser()

#Run the chain
result = chain.invoke({
  "animal":"cat",
  "count": 2
})

# Output
print(result)


