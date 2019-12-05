

def code_one(code,pointer,p1mode,p2mode, input):
    p1 = code[pointer+1] if p1mode else code[code[pointer+1]] #Handle position or inmediate modes
    p2 = code[pointer+2] if p2mode else code[code[pointer+2]]
    code[code[pointer+3]] = p1+p2
    return pointer+4 #Return how many instructions jump

def code_two(code,pointer,p1mode,p2mode, input):
    p1 = code[pointer+1] if p1mode else code[code[pointer+1]] 
    p2 = code[pointer+2] if p2mode else code[code[pointer+2]]
    code[code[pointer+3]] = p1*p2
    return pointer+4 

def code_three(code,pointer,p1mode,p2mode, input):
    code[code[pointer+1]] = input
    return pointer+2 

def code_four(code,pointer,p1mode,p2mode, input):
    p1 = code[pointer+1] if p1mode else code[code[pointer+1]]
    output = p1
    print(f"output {output}") #(?)
    return pointer+2 

def code_five(code,pointer,p1mode,p2mode, input):
    p1 = code[pointer+1] if p1mode else code[code[pointer+1]] 
    p2 = code[pointer+2] if p2mode else code[code[pointer+2]]
    if(p1!=0):
        return p2
    return pointer+3 

def code_six(code,pointer,p1mode,p2mode, input):
    p1 = code[pointer+1] if p1mode else code[code[pointer+1]] 
    p2 = code[pointer+2] if p2mode else code[code[pointer+2]]
    if(p1==0):
        return p2
    return pointer+3

def code_seven(code,pointer,p1mode,p2mode, input):
    p1 = code[pointer+1] if p1mode else code[code[pointer+1]] 
    p2 = code[pointer+2] if p2mode else code[code[pointer+2]]
    if(p1<p2):
        code[code[pointer+3]] = 1
    else:
        code[code[pointer+3]] = 0
    return pointer+4 

def code_eight(code,pointer,p1mode,p2mode, input):
    p1 = code[pointer+1] if p1mode else code[code[pointer+1]] 
    p2 = code[pointer+2] if p2mode else code[code[pointer+2]]
    if(p1==p2):
        code[code[pointer+3]] = 1
    else:
        code[code[pointer+3]] = 0
    return pointer+4 


def decode_op(i):
    i = [int(n) for n in str(i)]
    listI = [0 for u in range(4-len(i))] + i  #Make it to consistent length to decode the operation code
    p1mode = listI[1]
    p2mode = listI[0]
    opcode = int(str(listI[2]) + str(listI[3]))
    return p1mode,p2mode,opcode

ops = { #This functions are assign by reference, so they will modify the code without returning the new version
    1: code_one,
    2: code_two,
    3: code_three,
    4: code_four,
    5: code_five,
    6: code_six,
    7: code_seven,
    8: code_eight
}

def int_code(code,input):
    i=0
    while(i<len(code)):
        p1mode, p2mode, opcode = decode_op(code[i])
        if(opcode in ops.keys()):
            i = ops[opcode](code,i,p1mode,p2mode,input)
        else:
            if(opcode==99):
                break
            i+=1
    return code

def read_input(path):
    return [int(x) for x in open(path).read().split(",")]

if __name__ == "__main__":
    #ask for user input
    val = int(input("Enter your value: ").strip())
    #Read the input.txt
    content = read_input("input.txt")
    #Solve p1
    content_p1 = content.copy()
    result = int_code(content_p1,val)