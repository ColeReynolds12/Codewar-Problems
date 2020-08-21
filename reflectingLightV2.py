def reflecting_light(max_x, max_y, point, num_reflections):
    def gcd(a, b):
#   Needed for later. Finds greatest common demon. between 2 numbers
        while b:
            a, b = b, a % b
        return a

    def refToList(n):
#   If there are an odd number of reflections in x (or y),
#   gives the extra reflection to right (or top)
        if n<=0:
            return [0,0]
        elif n%2==0:
            return [n/2, n/2]
        else:
            return [(n+1)/2, (n-1)/2]

    def mainMethod():
#   Tries to solve it efficiently (using coprimes) if it will hit a corner.
#   Otherwise, counts all the reflections until the light vanishes.
        gcds=gcd(max_x, max_y)*gcd(point[0], point[1])
        xTotal = max_y*point[0]/gcds
        yTotal = max_x*point[1]/gcds
        xRed = xTotal/gcd(xTotal,yTotal)-1
        yRed = yTotal/gcd(xTotal,yTotal)-1
        if (xRed + yRed) <= num_reflections:
            print(num_reflections)
            print((refToList(yRed)[0], refToList(xRed)[0], refToList(yRed)[1], refToList(xRed)[1]))
            return (refToList(yRed)[0], refToList(xRed)[0], refToList(yRed)[1], refToList(xRed)[1])
        else:
            return altMethod()
    
    def altMethod():
        slope = point[1]/point[0]
        finish = [max_x, max_y]
        start = [0,0]
        tally = []
        d2p = [max_x-start[0], max_y-start[1]]
        s2p = d2p[1]/d2p[0]
        while len(tally) < num_reflections:
            d2p = [max_x-start[0], max_y-start[1]]
            s2p = d2p[1]/d2p[0]
            if s2p > slope:
                tally.append(0)
                start[1]+=d2p[0]*slope
                start[0]=0
            elif s2p < slope:
                tally.append(1)
                start[0]+=d2p[1]/slope
                start[1]=0
            else:
                tally.append(1)
                tally.append(0)
                start=[0,0]
        xTotal = num_reflections - sum(tally)
        yTotal = sum(tally)
        return (refToList(yTotal)[0], refToList(xTotal)[0], refToList(yTotal)[1], refToList(xTotal)[1])
    
    return mainMethod()
