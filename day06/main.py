def build_graph(content):
    graph = {}
    for line in content:
        B,A = line.split(')')
        graph[A] = B
    return graph

def find_path_planet(graph,value):
    r = []
    todo = value
    while True:
        r.append(graph[todo])
        todo = graph[todo]
        if todo=="COM":
            break
    return r        

def p1(graph):
    return sum([len(find_path_planet(graph,planet)) for planet in graph.keys() ])
        
def p2(graph):
    you = set(find_path_planet(graph,"YOU"))
    san = set(find_path_planet(graph,"SAN"))
    return len(you ^ san)


def read_input(path):
    return [x.replace("\n","") for x in open(path).readlines()]

if __name__ == "__main__":
    #ask for user input
    #Read the input.txt
    content = read_input("input.txt")
    graph = build_graph(content)
    #Solve p1
    print(f"--- Part One --- \n{p1(graph)}")
    #Solve p2
    print(f"--- Part Two --- \n{p2(graph)}")