from langchain.chat_models import init_chat_model
from langchain.agents import initialize_agent, Tool
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool
import os

os.environ["GROQ_API_KEY"] = "your free api key from https://console.groq.com/keys"

llm = init_chat_model("llama3-8b-8192", model_provider="groq")

wikipedia = WikipediaAPIWrapper(wiki_client=None)

@tool
def my_tool(location) -> str:
    """
    dexcription of the tool
    """
    # implement your tool
    return "result"

tools = [
    Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="useful for getting information about a place from Wikipedia",
    ),
    my_tool
]

agent = initialize_agent(
    llm=llm, tools=tools, verbose=True, handle_parsing_errors=True
)

# cemplete the prompt & input
prompt = PromptTemplate(
    input_variables=["input"],
    template="tel me about {input}..."
)

res = agent.invoke({"input": "AI"})
print(res["output"])
