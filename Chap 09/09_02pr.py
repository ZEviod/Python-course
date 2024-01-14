def game():
    return 678
score = game()
with open("highscore.txt") as f:
    hscore = f.read()

if hscore=='':
    with open('highscore.txt','w') as f:
        f.write(str(score))
elif int(hscore)<score or hscore=='':
    with open('highscore.txt','w') as f:
        f.write(str(score))