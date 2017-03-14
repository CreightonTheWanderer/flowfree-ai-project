class BoardState:
    # paths represented by the negative colors
    # nodes represented by the positive colors
    # blank spaces represented by zero
    # color is a positive integer
    def __init__(self, size):
        self._board = [[0 for x in range(size)] for y in range(size)]
        self._colors = 0
        self._size = size

    def addNodes(self,x1,y1,x2,y2):
        #nodes always appear in pairs
        if x1 > size-1 or x2 > size-1 or y1 >size-1 or y2 > size-1 :
            raise RuntimeError("dots out of bounds")
        self._colors += 1

        self._board [x1][y1] = color
        self._board [x2][y2] = color

    def makeMove(self,x,y,color):
    #color would be the color number from addDots
        if !checkAdjancent(x,y,color):
            raise RuntimeError("invalid move")
        #note the negative in front of color, path is created
        self._board [x][y] = -color

    def checkAdjancent(self,x,y,color):
    # functon that checks if a position is adjancent to a node or path of a
    # specific color, returns true if adjancent

        check = False
        if(abs(self._board [x+1][y]) = color){
            check = True
        }
        if(abs(self._board [x-1][y]) = color){
            check = True
        }
        if(abs(self._board [x][y+1]) = color){
            check = True
        }
        if(abs(self._board [x][y-1]) = color){
            check = True
        }

        return check;
