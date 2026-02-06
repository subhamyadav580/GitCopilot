from langgraph.graph import StateGraph, START, END
from core.git_utils import GitCopilotUtils
from core.agent_schemas import GithubCopilotAgent
from core.review_agent import CommitMessageGenerator


gitUtils = GitCopilotUtils()
commitMessageGenerator = CommitMessageGenerator()
graph = StateGraph(GithubCopilotAgent)


graph.add_node("find_git_repos", gitUtils.find_git_repos)
graph.add_node("select_and_navigate_repo", gitUtils.select_and_navigate_repo)
graph.add_node("get_current_git_branch", gitUtils.get_current_git_branch)
graph.add_node("list_unstaged_files", gitUtils.git_unstaged_files)
graph.add_node("stage_files_safe", gitUtils.stage_files_safe)
graph.add_node("get_staged_diff", gitUtils.get_staged_diff)
graph.add_node("check_files_to_commit", gitUtils.check_files_to_commit)
graph.add_node("generate_commit_message", commitMessageGenerator.generate)
graph.add_node("commit_files", gitUtils.commit_files)
graph.add_node("push_branch", gitUtils.push_branch)


graph.add_edge(START, "find_git_repos")
graph.add_edge("find_git_repos", "select_and_navigate_repo")
graph.add_conditional_edges(
    "select_and_navigate_repo",
    lambda state: (
        "get_current_git_branch"
        if state["repo_path"] != ""
        else END
    ),
)
graph.add_edge("get_current_git_branch", "list_unstaged_files")
graph.add_edge("list_unstaged_files", "stage_files_safe")
graph.add_edge("stage_files_safe", "get_staged_diff")
graph.add_edge("get_staged_diff", "check_files_to_commit")
graph.add_conditional_edges(
    "check_files_to_commit",
    lambda state: (
        "generate_commit_message"
        if state["has_staged_files"]
        else END
    ),
)
graph.add_edge("generate_commit_message", "commit_files")
graph.add_edge("commit_files", "push_branch")
graph.add_edge("push_branch", END)
app = graph.compile()


# def run_agent():
#     print("Running GitCopilot agent...")
#     return app.invoke({})

# run_agent()



for event in app.stream({}):
    print("Event", event)
