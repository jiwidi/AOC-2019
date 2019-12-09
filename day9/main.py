def code_one(code,pointer,p1,p2, input):
    code[code[pointer+3]] = p1+p2
    return pointer+4 #Return how many instructions jump

def code_two(code,pointer,p1,p2, input):
    code[code[pointer+3]] = p1*p2
    return pointer+4 

def code_three(code,pointer,p1,p2, input):
    code[code[pointer+1]] = input
    return pointer+2 

def code_four(code,pointer,p1,p2, input):
    output = p1
    print(f"output {output}") #(?)
    return pointer+2 

def code_five(code,pointer,p1,p2, input):
    if(p1!=0):
        return p2
    return pointer+3 

def code_six(code,pointer,p1,p2, input):
    if(p1==0):
        return p2
    return pointer+3

def code_seven(code,pointer,p1,p2, input):
    if(p1<p2):
        code[code[pointer+3]] = 1
    else:
        code[code[pointer+3]] = 0
    return pointer+4 

def code_eight(code,pointer,p1,p2, input):
    if(p1==p2):
        code[code[pointer+3]] = 1
    else:
        code[code[pointer+3]] = 0
    return pointer+4 

def code_nine(code,pointer,p1,p2, input):
    if(p1==p2):
        code[code[pointer+3]] = 1
    else:
        code[code[pointer+3]] = 0
    return pointer+2

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
    8: code_eight,
    9: code_nine
}

class int_computer:
    def __init__(self, code):
        self.code             = code[:]
        self.output           = [0]
        self.input_counter    = 0
        self.halt             = False
        self.output           = []
        self.pointer          = 0
        self.relative_pointer = 0

    def decode_op(self, i):
        i = [int(n) for n in str(i)]
        listI = [0 for u in range(4-len(i))] + i  #Make it to consistent length to decode the operation code
        p1mode = listI[1]
        p2mode = listI[0]
        opcode = int(str(listI[2]) + str(listI[3]))
        return p1mode,p2mode,opcode

    def get_params(self, p1mode, p2mode, opcode):
        if(opcode==99):
            return 0,0
        if(p1mode==3):
            p1 = self.code[self.code[self.relative_pointer+1]]
        else:
            p1 = self.code[self.pointer+1] if p1mode else self.code[self.code[self.pointer+1]] 
        if(p2mode==3):
            p2 = self.code[self.code[self.relative_pointer+2]]
        else:
            p2 = self.code[self.pointer+2] if p2mode else self.code[self.code[self.pointer+2]]
        return p1,p2

    def run(self,input):
        while not self.halt:
            p1mode, p2mode, opcode = self.decode_op(self.code[self.pointer])
            p1,p2 = self.get_params(p1mode,p2mode, opcode)
            print(f"Doing op {opcode} with p1 {p1} on mode {p1mode} and p2 {p2} on mode {p2mode} pointer at {self.pointer}")
            # self.pointer = ops[opcode](self.code,self.pointer,p1mode,p2mode,input,self.output)
            # if(opcode==4):
            #     return self
            if opcode==1:
                self.code[self.code[self.pointer+3]] = p1+p2
                self.pointer = self.pointer+4
            elif opcode==2:
                self.code[self.code[self.pointer+3]] = p1*p2
                self.pointer = self.pointer+4   
            elif opcode==3:
                self.code[self.code[self.pointer+1]] = input
                self.pointer = self.pointer+2
            elif opcode==4:
                self.output = self.output + [p1]
                self.pointer = self.pointer+2
            elif opcode==5:
                if(p1!=0):
                    self.pointer = p2
                else:
                    self.pointer = self.pointer + 3
            elif opcode==6:
                if(p1==0):
                    self.pointer = p2
                else:
                    self.pointer = self.pointer + 3  
            elif opcode==7:
                if(p1<p2):
                    self.code[self.code[self.pointer+3]] = 1
                else:
                    self.code[self.code[self.pointer+3]] = 0
                self.pointer = self.pointer + 4  
            elif opcode==8:
                if(p1==p2):
                    self.code[self.code[self.pointer+3]] = 1
                else:
                    self.code[self.code[self.pointer+3]] = 0
                self.pointer = self.pointer + 4   
            elif opcode==9:
                self.relative_pointer = self.relative_pointer + p1
                self.pointer = self.pointer+2  
            elif opcode==99:
                self.halt=True
            else:
                print(f"Unrecogniced code {opcode}")
        return self.output

def read_input(path):
    return [int(x) for x in open(path).read().split(",")]

if __name__ == "__main__":
    #ask for user input
    val = int(input("Enter your value: ").strip())
    #Read the input.txt
    content = read_input("input.txt")
    #Solve p1
    content_p1 = content.copy()
    comp = int_computer(content_p1)
    r = comp.run(val)
    print(r)