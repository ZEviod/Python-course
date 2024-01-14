class Remote:
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass

player1 = Player()
remote1 = Remote()

if(remote1.isLeftPressed()):
    player1.moveleft()