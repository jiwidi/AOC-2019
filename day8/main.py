wide=25
tall=6
def build_layers(raw_input, wide = 25, height= 6):
    return [raw_input[x:x+(wide*height)] for x in range(0,len(raw_input),(wide*height))]


def p1(layers):
    def count_chars(st,char='0'):
        result = 0
        for c in st:
            if c==char:
                result += 1     # same as result = result + 1
        return result
    counters = list(map(count_chars, layers))
    idx = counters.index(min(counters))
    return count_chars(layers[idx],'1')*count_chars(layers[idx],'2')
        
def p2(layers):
    r = ['2' for u in range(wide*tall)]
    for layer in layers:
        for idx, value in enumerate(layer):
            if(r[idx]=='2' and value!='2'):
                r[idx]=value
    for x in range(0,len(r),(wide)):
        print(r[x:x+wide])
    return r


def read_input(path):
    return open(path).read().replace('\n','')

if __name__ == "__main__":
    #ask for user input
    #Read the input.txt
    content = read_input("input.txt")
    layers = build_layers(content,wide,tall)
    c = p1(layers)
    #Solve p1
    print(f"--- Part One --- \n{c}")
    #Solve p2
    print(f"--- Part Two --- \n")
    r = p2(layers)