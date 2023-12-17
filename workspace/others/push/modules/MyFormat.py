class MyFormat:
    def workspace():
        with open('vvn20206205.code-workspace', 'r') as file: 
            content = file.read()
        print(content)
