class MyFormat:
    def workspace(path):
        with open(path, 'r') as file: 
            content = file.read()
        print(content)
