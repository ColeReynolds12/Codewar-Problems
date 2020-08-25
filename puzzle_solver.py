puzzle=[((21, None), (None, None), 6), ((None, 8), (None, 21), 3), ((8, None), (21, None), 1), ((None, None), (None, 8), 2), ((None, 21), (None, None), 5), ((None, None), (8, None), 4)]

from numpy import empty, vectorize
def puzzle_solver(pieces, width, height):
    canvas = empty((height, width), dtype=tuple)
    canvas[0,0] = pieces.index(lambda x: x[0]==(None, None) and x[1][0]==None)
    pieces.remove(canvas[0,0])
    for x in list(range(width-1)):
        canvas[0,x+1]=next(filter(lambda z: z[0][0]==canvas[0,x][0][1] and z[1][0]==canvas[0,x][1][1], pieces))
        pieces.remove(canvas[0,x+1])
        for y in list(range(height-1)):
            canvas[y+1,x]=next(filter(lambda z: z[0]==canvas[y,x][1], pieces))
            pieces.remove(canvas[y+1,x])
    for y in list(range(height-1)):
        canvas[y+1,width-1]=next(filter(lambda z: z[0]==canvas[y,width-1][1], pieces))
        pieces.remove(canvas[y+1,width-1])
    solution = vectorize(lambda t: t[2])
    return list(map(tuple, solution(canvas)))

# Algorithm 2
from numpy import empty, vectorize
def puzzle_solvernp(pieces, width, height):
    canvas = empty((height, width), dtype=tuple)
    edgeLayer = list(filter(lambda z: None in z[0] or None in z[1], pieces))
    bodyLayer = list(filter(lambda z: z not in edgeLayer, pieces))
    
    leftLayer = list(filter(lambda z: z[0][0]==z[1][0]==None, edgeLayer))
    rightLayer = list(filter(lambda z: z[0][1]==z[1][1]==None, edgeLayer))
    topLayerUnsorted = list(filter(lambda z: z[0]==(None, None), edgeLayer))
    bottomLayerUnsorted = list(filter(lambda z: z[1]==(None, None), edgeLayer))
    
    canvas[0,0] = next(filter(lambda z: z in leftLayer, topLayerUnsorted))
    canvas[height-1,0]= next(filter(lambda z: z in leftLayer, bottomLayerUnsorted))
    for x in list(range(width-1)):
        canvas[0,x+1]=next(filter(lambda z: z[0][0]==canvas[0,x][0][1] and z[1][0]==canvas[0,x][1][1], topLayerUnsorted))
        canvas[height-1,x+1]=next(filter(lambda z: z[0][0]==canvas[height-1,x][0][1] and z[1][0]==canvas[height-1,x][1][1], bottomLayerUnsorted))
    for y in list(range(height-2)):
        canvas[y+1,0]=next(filter(lambda z: z[0]==canvas[y,0][1], leftLayer))
        canvas[y+1,width-1]=next(filter(lambda z: z[0]==canvas[y,width-1][1], rightLayer))
    
    def algorithm(piece):
    #This def here draconic
        for x in canvas[y_top, x_min+1:x_max]:
            if piece[0]==x[1]:
                canvas[y_top+1, list(canvas[y_top]).index(x)]=piece
                bodyLayer.remove(piece)
                return
                
        for x in canvas[y_bottom, x_min+1:x_max]:
            if piece[1]==x[0]:
                canvas[y_bottom-1, list(canvas[y_bottom]).index(x)]=piece
                bodyLayer.remove(piece)
                return
                
        for y in canvas[y_top+1:y_bottom, x_min]:
            if piece[0][0]==y[0][1] and piece[1][0] == y[1][1]:
                canvas[list(canvas[:,x_min]).index(y), x_min+1]=piece
                bodyLayer.remove(piece)
                return
                
        for y in canvas[y_top+1:y_bottom, x_max]:
            if piece[0][1]==y[0][0] and piece[1][1] == y[1][0]:
                canvas[list(canvas[:,x_max]).index(y), x_max-1]=piece
                bodyLayer.remove(piece)
                return
                
    x_max, x_min, y_top, y_bottom = width-1, 0, 0, height-1
    a, b = width-4, height-4 
    while a>0 and b>0:
        while len(bodyLayer)>a*b:
            for piece in bodyLayer:
                algorithm(piece)
        a-=2
        b-=2
        x_max-=1
        x_min+=1
        y_top+=1
        y_bottom-=1

    
    solution = vectorize(lambda t: t[2])
    return list(map(tuple, solution(canvas)))
