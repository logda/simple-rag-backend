from dotenv import load_dotenv

load_dotenv()

from langchain_community.llms import Tongyi

output = Tongyi().invoke("Hi")
print(output)
