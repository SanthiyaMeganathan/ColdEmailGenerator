from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile"
)

response = llm.invoke("The first person to land on moon was..")
print(response.content)