content = True
i=1
with open("log_sample.txt") as f:
    while content:
        content = f.readline()
        if "python" in content.lower():    #or can use as content.lower() here
            print(content)
            print(f"Yes python is present on line number {i}")
        i+=1
