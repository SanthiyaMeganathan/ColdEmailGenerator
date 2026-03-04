from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import pandas as pd
import chromadb 
import uuid
load_dotenv()


llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile"
)

response = llm.invoke("The first person to land on moon was..")
print(response.content)


loader= WebBaseLoader("https://careers.nike.com/manager-software-engineering-reliability-engineering-itc/job/R-66050")
page_data = loader.load().pop().page_content
print(page_data)

prompt_extract = PromptTemplate.from_template(
    """
    ### SCRAPED TEXT FROM WEBSITE:
    {page_data}
    ###INSTRUCTION:
    The Scraped text is from the career's page of a website
    Your job is to extract the job posting and return them in json formate container
    following keys:`role`,`experience`,`skills` and`description`.
    only return the valid json.
    ###VALID JSON(NO PREAMBLE)
    """
)

chain_extract = prompt_extract | llm
res=chain_extract.invoke(input={'page_data':page_data})
print("***********************")
print(type(res))
print(res.content)
print(type(res.content))

print("******^^^^^^^^^")

json_parser = JsonOutputParser()
json_res = json_parser.parse(res.content)
print(json_res)

print(type(json_res))


pd.set_option('display.max_colwidth', None)
df = pd.read_csv("my_portfolio.csv")
print(df)

client = chromadb.PersistentClient('vectorstore')
collection = client.get_or_create_collection(name="portfolio")

if not collection.count():
    for _, row in df.iterrows():
        collection.add(documents=row['Techstack'],
                       metadatas={"links": row["Links"]},
                       ids=str(uuid.uuid4()))