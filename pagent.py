from langgraph.graph import StateGraph, START, END
from git_utils import GitCopilotUtils
from agent_schemas import GithubCopilotAgent
from review_agent import CommitMessageGenerator


gitUtils = GitCopilotUtils()
commitMessageGenerator = CommitMessageGenerator()
graph = StateGraph(GithubCopilotAgent)


graph.add_node("list_unstaged_files", gitUtils.git_unstaged_files)
graph.add_node("stage_files_safe", gitUtils.stage_files_safe)
graph.add_node("get_staged_diff", gitUtils.get_staged_diff)
graph.add_node("generate_commit_message", commitMessageGenerator.generate)

graph.add_edge(START, "list_unstaged_files")
graph.add_edge("list_unstaged_files", "stage_files_safe")
graph.add_edge("stage_files_safe", "get_staged_diff")
graph.add_edge("get_staged_diff", "generate_commit_message")
graph.add_edge("generate_commit_message", END)
app = graph.compile()


print("List files: ", app.invoke({}))

