
filename = "Temp_num_3.txt"
S = open(filename,"r")

mask = [False, True, True, True, False, True, True, True, False]

def isMask (i):
    for j in range(len(mask)):
        if (str.isupper(line[i+j]) != mask[j]):
            return False
    return True
        
for line in S:
    for i in range(len(line) - 9):
        if isMask(i):
            print(line[i + 4], end = "")
        
        
    













