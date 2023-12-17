class MyFormat:
    def workspace(path):
        with open(path, 'r', encoding="utf-8") as file:
            contents = file.read()
        while '  ' in contents:
            contents = contents.replace('  ', ' ')
        with open(path, 'w', encoding="utf-8") as file:
            file.write(contents)
