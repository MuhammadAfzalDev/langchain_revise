from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

schema = [
    ResponseSchema(name='fact_1',description='fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 facts about {topic}.\n{format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic': 'Black hole'})

print(result)