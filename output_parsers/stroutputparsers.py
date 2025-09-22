from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Prompt to generate a detailed report from a topic
report_prompt = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"],
)

# Prompt to summarize the generated report text
summary_prompt = PromptTemplate(
    template="Write a 5 line summary on the following text.\n{text}",
    input_variables=["text"],
)

parser = StrOutputParser()

chain = report_prompt | model | parser | summary_prompt | model | parser

result = chain.invoke({"topic": "The Great Gatsby"})

print(result)

