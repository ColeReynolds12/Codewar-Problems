#https://www.codewars.com/kata/5ef2bc554a7606002a366006

from numpy import empty, vectorize
class Puzzle_solver:
    def __init__(self, pieces, width, height):
        self.height = height
        self.width = width
        self.pieces = pieces
        self.canvas = empty((height, width), dtype=tuple)
        self.edgeLayer = list(filter(lambda z: None in z[0] or None in z[1], pieces))
        self.bodyLayer = list(filter(lambda z: z not in self.edgeLayer, pieces))
        self.leftLayer = list(filter(lambda z: z[0][0]==z[1][0]==None, self.edgeLayer))
        self.rightLayer = list(filter(lambda z: z[0][1]==z[1][1]==None, self.edgeLayer))
        self.topLayerUnsorted = list(filter(lambda z: z[0]==(None, None), self.edgeLayer))
        self.bottomLayerUnsorted = list(filter(lambda z: z[1]==(None, None), self.edgeLayer))
    
    def makeCanvasBorder(self):
        self.canvas[0,0] = next(filter(lambda z: z in self.leftLayer, self.topLayerUnsorted))
        self.canvas[self.height-1,0]= next(filter(lambda z: z in self.leftLayer, self.bottomLayerUnsorted))
        for x in list(range(self.width-1)):
            self.canvas[0,x+1]=next(filter(lambda z: z[0][0]==self.canvas[0,x][0][1] and z[1][0]==self.canvas[0,x][1][1], self.topLayerUnsorted))
            self.canvas[self.height-1,x+1]=next(filter(lambda z: z[0][0]==self.canvas[self.height-1,x][0][1] and z[1][0]==self.canvas[self.height-1,x][1][1], self.bottomLayerUnsorted))
        for y in list(range(self.height-2)):
            self.canvas[y+1,0]=next(filter(lambda z: z[0]==self.canvas[y,0][1], self.leftLayer))
            self.canvas[y+1,self.width-1]=next(filter(lambda z: z[0]==self.canvas[y,self.width-1][1], self.rightLayer))
    
    def algorithm(self, piece):
        for x in self.canvas[self.y_top, self.x_min+1:self.x_max]:
            if piece[0]==x[1]:
                self.canvas[self.y_top+1, list(self.canvas[self.y_top]).index(x)]=piece
                self.bodyLayer.remove(piece)
                return
                
        for x in self.canvas[self.y_bottom, self.x_min+1:self.x_max]:
            if piece[1]==x[0]:
                self.canvas[self.y_bottom-1, list(self.canvas[self.y_bottom]).index(x)]=piece
                self.bodyLayer.remove(piece)
                return
                
        for y in self.canvas[self.y_top+1:self.y_bottom, self.x_min]:
            if piece[0][0]==y[0][1] and piece[1][0] == y[1][1]:
                self.canvas[list(self.canvas[:,self.x_min]).index(y), self.x_min+1]=piece
                self.bodyLayer.remove(piece)
                return
                
        for y in self.canvas[self.y_top+1:self.y_bottom, self.x_max]:
            if piece[0][1]==y[0][0] and piece[1][1] == y[1][0]:
                self.canvas[list(self.canvas[:,self.x_max]).index(y), self.x_max-1]=piece
                self.bodyLayer.remove(piece)
                return
    
    def recursion(self):
        self.x_max, self.x_min, self.y_top, self.y_bottom = self.width-1, 0, 0, self.height-1
        a, b = self.width-4, self.height-4 
        while a>0 and b>0:
            while len(self.bodyLayer)>a*b:
                for piece in self.bodyLayer:
                    self.algorithm(piece)
            a-=2
            b-=2
            self.x_max-=1
            self.x_min+=1
            self.y_top+=1
            self.y_bottom-=1
        for piece in self.bodyLayer:
            self.algorithm(piece)
# Uncomment this the second time, and youll see that the body layer has 1 piece in it.
#         for piece in self.bodyLayer:
#             self.algorithm(piece)
        return self.canvas
            
if __name__ == "__main__":
    x = Puzzle_solver("csv file goes here :D", 93, 94)
    x.makeCanvasBorder()
    x.recursion()
    print(x.bodyLayer)
   
