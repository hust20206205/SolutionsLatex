import os
from modules.MyExecute import MyExecute


class MyGit:
    def add():
        os.chdir("../../../")
        cmd = f'git add .'
        MyExecute(cmd)

    def commit(message):
        cmd = f'git commit -m "{message}"'
        MyExecute(cmd)
