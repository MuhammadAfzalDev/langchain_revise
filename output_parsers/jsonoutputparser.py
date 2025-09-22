from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age, and city of a fictional person.\n{format_instructions}',
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = template | model | parser

final_result = chain.invoke({})

print(final_result)
print(type(final_result))