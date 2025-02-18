from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain_ollama.llms import OllamaLLM


model = OllamaLLM(model="llama3.2:latest")

summary_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are movie critic."),
        ("human", "Provide a brief summary of the movie {movie_name}.")
    ]
)

# Define plot analysis step
def analyze_plot(plot):
    plot_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are movie critic."),
            ("human","Analyze the plot: {plot}. What are weakness and strengths?")
        ]
    )
    return plot_template.format_messages(plot=plot)

# Define character analysis step
def analyze_character(characters):
    character_template = ChatPromptTemplate.from_messages(
        [
            ("system","You are movie critic."),
            ("human","Analyze the characters: {characters}. What are weakness and strengths?")
        ]
    )
    return character_template.format_messages(characters=characters)

# Combine the final verdict
def combine_verdict(plot_analysis, character_analysis):
    return f"Plot Analysis:\n{plot_analysis}\n\nCharacter Analysis:\n{character_analysis}"

# Simplify branches with LECL
plot_branch_chain = (
    RunnableLambda(lambda x: analyze_plot(x)) | model | StrOutputParser()
)

character_branch_chain = (
    RunnableLambda(lambda x:analyze_character(x)) | model | StrOutputParser()
)

# Create  the combined  chain using Langchain Expression Language(LCEL)

chain = (
        summary_template 
        | model 
        | StrOutputParser() 
        | RunnableParallel(branches={"plot": plot_branch_chain, "characters": character_branch_chain})
        | RunnableLambda(lambda x: combine_verdict(x["branches"]["plot"], x["branches"]["characters"]))
       )
       

#Run the chain
result = chain.invoke({
 "movie_name":"Inception"
})

# Output
print(result)


