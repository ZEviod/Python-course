def readFile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")
        
readFile("a1.txt")
readFile("a2.txt")
readFile("a3.txt")