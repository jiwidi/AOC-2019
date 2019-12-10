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
        listI = [0 for u in range(5-len(i))] + i  #Make it to consistent length to decode the operation code
        p1mode = listI[2]
        p2mode = listI[1]
        p3mode = listI[0]
        opcode = int(str(listI[3]) + str(listI[4]))
        return p1mode,p2mode,p3mode,opcode

    def get_params(self, p1mode, p2mode, p3mode, opcode):
        p1, p2, p3 = 0,0,0
        if(opcode==99):
            return p1,p2,p3
        if(p1mode==2):
            if(opcode==3):
                p1 = self.relative_pointer + self.code[self.pointer+1]
            else:
                p1 = self.code[self.relative_pointer + self.code[self.pointer+1]]
        else:
            p1 = self.code[self.pointer+1] if p1mode else self.code[self.code[self.pointer+1]] 
        if(opcode in [1,2,5,6,7,8]):
            if(p2mode==2):
                p2 = self.code[self.relative_pointer + self.code[self.pointer+2]]
            else:
                p2 = self.code[self.pointer+2] if p2mode else self.code[self.code[self.pointer+2]]
        if(opcode in [1,2,7,8]):
            if(p3mode==2):
                p3 = self.relative_pointer + self.code[self.pointer+3]
            else:
                p3 = self.code[self.pointer+3]
        return p1,p2,p3

    def run(self,input):
        while not self.halt:
            p1mode, p2mode, p3mode, opcode = self.decode_op(self.code[self.pointer])
            #print(f"Doing op {opcode} with p1  on mode {p1mode} and p2 on mode {p2mode} and p3 on mode {p3mode} relative pointer to {self.relative_pointer} op {self.code[self.pointer:self.pointer+4]}")
            p1,p2,p3 = self.get_params(p1mode,p2mode,p3mode, opcode)
            if opcode==1:
                self.code[p3] = p1+p2
                self.pointer = self.pointer+4
            elif opcode==2:
                self.code[p3] = p1*p2
                self.pointer = self.pointer+4   
            elif opcode==3:
                self.code[p1] = input
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
                    self.code[p3] = 1
                else:
                    self.code[p3] = 0
                self.pointer = self.pointer + 4  
            elif opcode==8:
                if(p1==p2):
                    self.code[p3] = 1
                else:
                    self.code[p3] = 0
                self.pointer = self.pointer + 4   
            elif opcode==9:
                self.relative_pointer = self.relative_pointer + p1
                self.pointer = self.pointer+2  
            elif opcode==99:
                self.halt=True
            else:
                print(f"Unrecogniced code {opcode}")
                break
        return self.output

def read_input(path):
    return [int(x) for x in open(path).read().split(",")]

if __name__ == "__main__":
    #ask for user input
    #Read the input.txt
    content = read_input("input.txt") + [0 for u in range(10000)] #Make computer memory larger
    #Solve p1
    content_p1 = content.copy()
    comp = int_computer(content_p1)
    r = comp.run(1)
    print("--- Part One ---")
    print(r)
    content_p2 = content.copy()
    comp = int_computer(content_p2)
    r = comp.run(2)
    print("--- Part Two ---")
    print(r)