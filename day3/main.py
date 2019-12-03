import numpy as np
from math import sqrt

def manhattan(x,y):
    x = np.array(x)
    y = np.array(y)
    diff = abs(x-y)
    return diff.sum()

def get_intersect(A, B, C, D):
    cx=0
    cy=0
    solved=False
    if( ((C[1] < A[1] and D[1] > B[1]) or (C[1] > A[1] and D[1] < B[1]) ) and ((C[0] > A[0] and D[0] < B[0]) or (C[0] < A[0] and D[0] > B[0]))  ):
            if(C[0] == D[0]):
                cx = C[0]
                cy = A[1]
            elif(C[1] == D[1]):
                cx = B[0]
                cy = C[1]
            solved=True
    return solved, cx, cy

def closest_intersection(wires):
    intersections=[]
    paths=[]
    for wire in wires:
        aux = []
        position=[0,0]
        for instruction in wire:
            code = instruction[0]
            steps = int(instruction[1:])
            if(code=='R'):
                move = [steps,0]
                newposition = [position[0]+move[0], position[1]+move[1]]
                aux.append([position,newposition])
                position = newposition
            elif(code=='L'):
                move = [-steps,0]
                newposition = [position[0]+move[0], position[1]+move[1]]
                aux.append([position,newposition])
                position = newposition
            elif(code=='D'):
                move = [0,-steps]
                newposition = [position[0]+move[0], position[1]+move[1]]
                aux.append([position,newposition])
                position = newposition
            elif(code=='U'):
                move = [0,steps]
                newposition = [position[0]+move[0], position[1]+move[1]]
                aux.append([position,newposition])
                position = newposition
        paths.append(aux)
    wire1 = paths[0]
    wire2 = paths[1]
    for path1 in wire1:
        A,B = path1
        for path2 in wire2:
            C,D = path2
            contained,x,y = get_intersect(A,B,C,D)
            if(contained and [x,y]!=[0,0]):
                intersections.append([[x,y], [A,B], [C,D]])
    return intersections,wire1,wire2

def steps_to_intersection(wire1,wire2,intersections):
    def distance(A, B):
        return sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
    beststeps = float('inf')
    for intersection,path1,path2 in intersections:
        steps1=0
        for path in wire1:
            A,B = path
            if(path==path1):
                steps1+=distance(A,intersection)
                break
            else:
                steps1+=distance(A,B)
        steps2=0
        for path in wire2:
            A,B = path
            if(path==path2):
                steps2+=distance(A,intersection)
                break
            else:
                steps2+=distance(A,B)
        r = steps1+steps2
        if(r<beststeps):
            beststeps=r
    return int(beststeps)

def read_input(path):
    return [x.split(',') for x in  open(path).readlines()]

if __name__ == "__main__":
    #Read the input
    wires = read_input("input.txt")
    #Solve p1
    intersections,wire1path,wire2path = closest_intersection(wires)
    r = min([manhattan(x[0],[0,0]) for x in intersections])
    print(f"--- Part One --- \n{r}")
    #Solve p2
    r = steps_to_intersection(wire1path,wire2path, intersections)
    print(f"--- Part Two --- \n{r}")



