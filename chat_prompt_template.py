from langchain_core.prompts import ChatPromptTemplate

# This Method is use for dynamic prompt template for multiple messagesgit commit -m "first commit"



chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} assistant"),
    ("human", " Explain in simple terms, what is {topic}"),
])

prompt = chat_template.invoke({'domain': 'finance', 'topic': 'stock market'})

print(prompt)
