import os
from modules.MyGit import MyGit
from modules.MyFormat import MyFormat
from modules.MyView import MyView


git_path = os.path.join(os.getcwd(), '../../../')
workspace_path = os.path.join(os.getcwd(), '../../vvn20206205.code-workspace')
gitignore_path = os.path.join(git_path, ".gitignore") 
message = "VuVanNghia20206205"

MyGit.chdir(git_path)
MyGit.add()
MyGit.commit(message)

MyFormat.workspace(workspace_path)
MyFormat.gitignore(gitignore_path)
MyFormat.gitignore(r"C:\Users\vvn20206205\Desktop\SolutionsLatex\baocao\start\init.sty")
MyFormat.markdown(git_path)
MyFormat.latex(git_path)

MyView.CloseTab()
MyView.Target(2)
MyView.CloseTerminal()
MyView.CloseScrollBar()
# MyView.CollapseFolders()
MyView.OpenGit()
