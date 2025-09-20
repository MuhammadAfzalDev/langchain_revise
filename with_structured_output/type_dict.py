from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Review(BaseModel):
    rating: int
    comment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""This is a great product! I love it!
                                 I would recommend it to anyone.
                                 I would give it a 5 star rating.
                                 I love the quality of the product.
                                 I love the price of the product.
                                 I love the customer service of the product.
                                 I love the shipping of the product.
                                 I love the return policy of the product.
                                 I love the warranty of the product.""")

print(result.rating)
print(result.comment)



