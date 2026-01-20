from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

from agent_schemas import GithubCopilotAgent


os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

class CommitMessageGenerator:
    def __init__(self, model: str = "gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model)

        self.prompt = ChatPromptTemplate.from_template("""
            You are an experienced code reviewer.
            Your task is to review the provided file diff and give a concise commit message.

            Follow these steps:
            1. Analyze the provided diff carefully.
            2. Generate a commit message summarizing the changes.

            Diff:
            {staged_files_diff}
        """)

        self.chain = self.prompt | self.llm

    def generate(self, state: GithubCopilotAgent) -> str:
        response = self.chain.invoke(
            {"staged_files_diff": state["staged_files_diff"]}
        )
        return {"commit_message": response.content.strip()}
