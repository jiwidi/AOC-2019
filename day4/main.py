def next_number_p1(number):
    number+=1
    #Check if is ascending, otherwise return the next asceding number
    if(isAsc(number)==0):
        number = nextAsc(number)
    #Check if it contains double digits, otherwise return next number containing double digits
    if(hasDD(number)==0):
        number = nextDD(number)
    return number

def next_number_p2(number):
    number+=1
    if number==177889:
        print("yo")
    #Check if is ascending, otherwise return the next asceding number
    if(isAsc(number)==0):
        number = nextAsc(number)
    #Check if it contains double digits, otherwise return next number containing double digits
    if(not hasDDstrict(number)):
        number = nextDD(number)
        if(not hasDDstrict(number)):
            number =next_number_p2(number)
    return number

def isAsc(i):
    listIn = [int(n) for n in str(i)]
    r=0
    previous=listIn[0]
    for n in listIn[1:]:
        if(n<previous):
            return False
        previous=n
    return True

def nextAsc(i):
    listIn = [int(n) for n in str(i)]
    previous = 0
    c=0
    for n in listIn:
        if(n<previous):
            listIn[c]=previous
        else:
            previous=n
        c+=1
    return int(''.join(map(str, listIn)))

def nextAsc(i):
    listIn = [int(n) for n in str(i)]
    previous = listIn[0]
    c=1
    for n in listIn[1:]:
        if(n<previous):
            listIn = listIn[:c] + [previous for u in range(len(listIn)-c)]
            break
        else:
            previous=n
        c+=1
    return int(''.join(map(str, listIn)))

def hasDD(i):
    listIn = [int(n) for n in str(i)]
    r=0
    previous=listIn[0]
    for n in listIn[1:]:
        if(n==previous):
            r+=1
        else:
            previous=n
    return r 

def hasDDstrict(i):
    listIn = [int(n) for n in str(i)]
    r={}
    for u in range(10):
        r[u]=0
    
    previous=listIn[0]
    for n in listIn[1:]:
        if(n==previous):
            r[n]+=1
        else:
            previous=n
    return (1 in r.values())

def nextDD(i):
    listIn = [int(n) for n in str(i)]
    listIn[-2] = listIn[-1]
    return int(''.join(map(str, listIn)))

def read_input(path):
    return [int(x) for x in open(path).read().split("-")]


if __name__ == "__main__":
    #Read the input
    small,big = read_input("input.txt")
    # #Solve p1
    c=0
    words1 = []
    minN,maxN = small,big
    while(minN<maxN):
        minN = next_number_p1(minN)
        if(minN<maxN):
            words1.append(minN)
            c+=1

    print(f"--- Part One --- \n{c}")
    # #Solve p2 
    c=0
    words2 = []
    minN,maxN = small,big
    while(minN<maxN):
        minN = next_number_p2(minN)
        if(minN<maxN):
            words2.append(minN)
            c+=1
    print(f"--- Part Two --- \n{c}")