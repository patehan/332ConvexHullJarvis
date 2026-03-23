'''
Han Pate
CSCI 332 Spring 2026
Programming Assignment | Convex Hull Jarvis
I acknowledge that I have worked on this assignment independently, except
where explicitly noted and referenced. Any collaboration or use of external
resources has been properly cited. I am fully aware of the consequences of
academic dishonesty and agree to abide by the university's academic integrity
policy. I understand the importance the consequences of plagiarism.
'''

Point = tuple[float,float] #Point is capitalized bc its a type not a variable

def orientation(p: Point,q: Point,r: Point): #this function uses the convex hull formula & calculates it
    val = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]) #the formula for convex hull
    return val #return the value

def convex_hull_jarvis(points: List[Point]) -> List[Point]:
    if len(points) < 3: #if there are less than 3 pts
        return [] #return an empty list
    hull = [] # a list to store the points
    start = min(points, key=lambda p: (p[0], p[1])) #find the leftmost point, look at formula
    current = start

    while True:
        hull.append(current)
        next_point = points[0] if points[0] != current else points[1]

        for candidate in points:
            if orientation(current, next_point, candidate) > 0: #pts will be > 0 if they're counterclockwise
                next_point = candidate

        current = next_point
        if current == start: #if the current point is now the start
            break #breaks out of the loop
    return hull



points = [(0,3), (2,2), (1,1), (2,1), (3,0), (0,0), (3,3)]
hull = convex_hull_jarvis(points)
print('Convex hull:', hull)
#Should print: Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]
#output should be a list of pts forming the convex in counter clockwise orderfrom typing import List, Tuple


#Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]