with open("log_sample.txt") as f:
    content = f.read().lower()

if "python" in content:    #or can use as content.lower() here
    print("Yes python is present")