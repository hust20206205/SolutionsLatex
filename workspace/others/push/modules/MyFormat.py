import os
import glob


class MyFormat:
    def workspace(file):
        with open(file, 'r', encoding="utf-8") as file:
            contents = file.read()
        while '  ' in contents:
            contents = contents.replace('  ', ' ')
        with open(file, 'w', encoding="utf-8") as file:
            file.write(contents)

    def markdown(path):
        files = glob.glob(os.path.join(path, f'**/*.md'), recursive=True)
        for file in files:
            with open(file, 'r', encoding="utf-8") as file:
                contents = file.read()
            while '  ' in contents:
                contents = contents.replace('  ', ' ')
            contents = '\n'.join(line.strip() for line in contents.split('\n'))
            while "\n\n\n" in contents:
                contents = contents.replace("\n\n\n", "\n\n")
            contents = contents.lstrip('\n')
            with open(file, 'w', encoding="utf-8") as file:
                file.write(contents) 