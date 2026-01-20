from typing import TypedDict, List



class GithubCopilotAgent(TypedDict):
    unstaged_files: List[str]
    staged_files: List[str]
    staged_files_diff: str
    commit_message: str