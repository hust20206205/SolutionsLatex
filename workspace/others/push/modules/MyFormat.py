import os
import glob

replacements = {
    '\n': '\n\n\n',
}


class MyFormat:
    def workspace(workspace_path):
        with open(workspace_path, 'r', encoding="utf-8") as file:
            contents = file.read()
        while '  ' in contents:
            contents = contents.replace('  ', ' ')
        contents = '\n'.join(line.strip() for line in contents.split('\n'))
        while "\n\n\n" in contents:
            contents = contents.replace("\n\n\n", "\n\n")
        contents = contents.lstrip('\n')
        with open(workspace_path, 'w', encoding="utf-8") as file:
            file.write(contents)

    def markdown(git_path):
        files = glob.glob(os.path.join(git_path, f'**/*.md'), recursive=True)
        for file_markdown in files:
            with open(file_markdown, 'r', encoding="utf-8") as file:
                contents = file.read()

            if contents == '':
                continue

            contents = contents.replace('\n', '\n\n\n')

            while '  ' in contents:
                contents = contents.replace('  ', ' ')
            contents = '\n'.join(line.strip() for line in contents.split('\n'))
            while "\n\n\n" in contents:
                contents = contents.replace("\n\n\n", "\n\n")
            contents = contents.lstrip('\n')
            with open(file_markdown, 'w', encoding="utf-8") as file:
                file.write(contents)

    def basic(gitignore_path):
        with open(gitignore_path, 'r', encoding="utf-8") as file:
            contents = file.read()

        contents = contents.replace('\n', '\n\n\n')

        while '  ' in contents:
            contents = contents.replace('  ', ' ')
        contents = '\n'.join(line.strip() for line in contents.split('\n'))
        while "\n\n\n" in contents:
            contents = contents.replace("\n\n\n", "\n\n")
        contents = contents.lstrip('\n')
        with open(gitignore_path, 'w', encoding="utf-8") as file:
            file.write(contents)

    def latex(git_path):
        files = glob.glob(os.path.join(git_path, f'**/*.tex'), recursive=True)
        for file_latex in files:
            with open(file_latex, 'r', encoding="utf-8") as file:
                contents = file.read()

            if contents == '':
                continue

            for key, value in replacements.items():
                value = f"  {value}  "
                contents = contents.replace(key, value)

            while ' ,' in contents:
                contents = contents.replace(' ,', ', ')
            contents = contents.replace(' ,', ', ')
            while ' ?' in contents:
                contents = contents.replace(' ?', '? ')
            contents = contents.replace(' ?', '? ')
            while ' !' in contents:
                contents = contents.replace(' !', '! ')
            contents = contents.replace(' !', '! ')

            while '  ' in contents:
                contents = contents.replace('  ', ' ')

            while '( ' in contents:
                contents = contents.replace('( ', '(')
            while ' )' in contents:
                contents = contents.replace(' )', ')')
            while '[ ' in contents:
                contents = contents.replace('[ ', '[')
            while ' ]' in contents:
                contents = contents.replace(' ]', ']')
            while '{ ' in contents:
                contents = contents.replace('{ ', '{')
            while ' }' in contents:
                contents = contents.replace(' }', '}')

            contents = '\n'.join(line.strip() for line in contents.split('\n'))
            while "\n\n\n" in contents:
                contents = contents.replace("\n\n\n", "\n\n")
            contents = contents.lstrip('\n')
            with open(file_latex, 'w', encoding="utf-8") as file:
                file.write(contents)
