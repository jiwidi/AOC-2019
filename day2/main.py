ops = {
    1: lambda x, y: x+y,
    2: lambda x, y: x*y
}

def int_code(code):
    i=0
    while(i+4<len(code)):
        if(code[i] in ops.keys()):
            code[code[i+3]] = ops[code[i]](code[code[i+1]],code[code[i+2]])
            i+=4
        else:
            i+=1
    return code

def read_input(path):
    return [int(x) for x in  open('input.txt').read().split(',')]

if __name__ == "__main__":
    #Read the input
    content = read_input("input.txt")
    #Solve p1
    ##Follow problem instructions to replace values
    content_p1 = content.copy()
    content_p1[1]=12
    content_p1[2]=2
    result = int_code(content_p1)
    print("Result for p1: {}".format(result[0])) 
    #Solve p2 brute force
    for noun in range(99):
        for verb in range(99):
            content_p2 = content.copy()
            content_p2[1]=noun
            content_p2[2]=verb
            r = int_code(content_p2)
            if(r[0]==19690720):
                print("Noun:{}  Verb:{}  Result for p2: {}".format(noun,verb,100*noun+verb))



