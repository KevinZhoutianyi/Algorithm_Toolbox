# Uses python3
def edit_distance(s, t):
    dynProArray = [[100 for i in range(0,len(s)+1)] for j in range(0,len(t)+1)]
    for i in range(0,len(s)+1):
        dynProArray[0][i] = i
    for i in range(0,len(t)+1):
        dynProArray[i][0] = i
    
    for i in range(1,len(t)+1):
        for j in range(1,len(s)+1):
            if t[i-1]==s[j-1] and dynProArray[i-1][j-1]<dynProArray[i][j]:
                dynProArray[i][j] = dynProArray[i-1][j-1]
            if t[i-1]!= s[j-1] and dynProArray[i-1][j-1]+1<dynProArray[i][j]:
                dynProArray[i][j] = dynProArray[i-1][j-1]+1
            if dynProArray[i-1][j]+1<dynProArray[i][j]:
                dynProArray[i][j] = dynProArray[i-1][j]+1
            if dynProArray[i][j-1]+1<dynProArray[i][j]:
                dynProArray[i][j] = dynProArray[i][j-1]+1
        
    return dynProArray[len(t)][len(s)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
