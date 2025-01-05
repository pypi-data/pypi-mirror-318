import getpass
import os

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

result = model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)
print(result)