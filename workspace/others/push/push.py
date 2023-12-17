from modules.MyGit import MyGit
from modules.MyFormat import MyFormat
import os


git_path=os.path.join(os.getcwd(),'../../../')
workspace_path=os.path.join(os.getcwd(),'../../vvn20206205.code-workspace')

message = "VuVanNghia20206205"
MyGit.chdir(git_path)
MyGit.add()
MyGit.commit(message)
MyFormat.workspace(workspace_path)