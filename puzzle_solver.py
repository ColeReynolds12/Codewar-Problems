puzzle=[((21, None), (None, None), 6), ((None, 8), (None, 21), 3), ((8, None), (21, None), 1), ((None, None), (None, 8), 2), ((None, 21), (None, None), 5), ((None, None), (8, None), 4)]

import numpy as np
def puzzle_solver(keys, width, height):
    pieces = keys
    answer=[]
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
