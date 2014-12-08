class Reindeer:
    def currentDirection(self):
        return self.direction

    def setDirection(self,direction):
        self.direction = direction

    def rotateLeft(self):
        if ( self.currentDirection() == "N"):
            self.setDirection("W")
        if ( self.currentDirection() == "S"):
            self.setDirection("E")
        if ( self.currentDirection() == "W"):
            self.setDirection("N")
        if ( self.currentDirection() == "E"):
            self.setDirection("S")
        return

    def decideNextMove(self,movementTuple):
        if ( "PE" in movementTuple ):
            self.setDirection("E")



