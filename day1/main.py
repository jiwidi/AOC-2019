#1 line solution for p1: sum(int(x)//3-2 for x in open('input.txt'))

def calculate_fuel(mass,recursive=False):
    result = int(mass/3)-2
    if (recursive):
        fuel = result
        while((int(fuel/3)-2)>0):
            fuel= int(fuel/3)-2
            result+= fuel
    return result

def read_input(path):
    return [int(x) for x in open('input.txt')]

if __name__ == "__main__":
    content = read_input("input.txt")
    content_p1 = [calculate_fuel(x) for x in content]
    print("Part 1 result: {}".format(sum(content_p1))) #Result for p1
    content_p2 = [calculate_fuel(x,recursive=True) for x in content]
    print("Part 2 result: {}".format(sum(content_p2))) #Result for p2





