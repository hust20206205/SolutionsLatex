from modules.MyGit import MyGit
from modules.MyFormat import MyFormat
import os


# vi_tri=os.getcwd()
# print("🐍 File: push/push.py | Line: 7 | undefined ~ vi_tri",vi_tri)
git_path=os.path.join(os.getcwd(),'../../../')
workspace_path=os.path.join(os.getcwd(),'../../vvn20206205.code-workspace')
# print("🐍 File: push/push.py | Line: 7 | undefined ~ vi_tri",vi_tri)

message = "VuVanNghia20206205"
MyGit.chdir(git_path)
MyGit.add()
MyGit.commit(message)
MyFormat.workspace(workspace_path)