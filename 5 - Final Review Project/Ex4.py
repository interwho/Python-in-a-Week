def build_range(start,finish,pts): #Assignment Function
    beg = 0 #initialize new start and finish variables for swapping in case of reversal (ie. start > finish)
    end = 0
    brange = [] #init return array
    if start > finish: #check for a reversed array, append the real start and end to the new variables
        beg  = finish
        end = start
    elif finish > start:
        beg = start
        end = finish
    else:
        for i in pts:
            brange.append(start)
        return brange #Same number, no increment, so just return it pts number of times
    #begin logic
    div = end-beg
    den = pts - 1
    npts = float(div)/float(den) #get the increment to divide by
    while beg < end: #while the beg is less than the end, append it to the return and increment by even amount
        brange.append(beg)
        beg = beg + npts
    brange.append(end) #append the last number manually
    return brange #return

#Test Program
print build_range(2,3,5)
