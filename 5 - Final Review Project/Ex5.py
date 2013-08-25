def make_oh(k): #assignment function
    n = k-1 #set initial number of spaces
    b = k #set a temp variable so k isn't modified by the beginning
    x = 0 # set a count variable for extra x
    arr = [] #init array of beg
    temp = '' #temporary appending variable
    #beginning
    for i in range (k): #for each in k, create the lines leading up to middle
        temp = " "*n + "x"*x + "x"*b #create it
        print temp #print it
        arr.append(temp) #save it for later (in the end)
        n = n-1 #increment/decrement X's and spaces
        b = b+1
        x = x+1
    #middle
    for i in range(k): #for each in k, print a middle line
        print "x"*k + " " + "x"*k
    #end
    for i in reversed(arr): #print the reversed iteration of the beginning (for laziness)
        print i

#Test Program
make_oh(2)
make_oh(3)
