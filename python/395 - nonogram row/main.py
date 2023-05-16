def nonogramrow(arr):
    """ Outputs the amount of consecutive 1's in an array """
    out = [] # output array
    length = 0 # number of consecutive 1's
    for i in arr:
        if i == 0:
            if length > 0:
                out.append(length)
                length = 0
            
            continue
        length += 1
    
    if length > 0: out.append(length)
    return out

def main():
    arr = [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1] # Input array
    print(nonogramrow(arr))

main()