def twothreeorfive(n) : #function definition
    i=1 #init the number variable
    a = [] #init the number array
    while i < n+1: #starting from 1, go through each number until n
        if i % 2 == 0: #divisible by 2?
            a.append(i)
        elif i % 3 == 0: #divisible by 3?
            a.append(i)
        elif i % 5 == 0: #divisible by 5?
            a.append(i)
        i = i+1 #incr. i
    return a #return the newly-minted array of numbers

#Program Test
x = raw_input("Enter a positive int")
x = int(x)
print twothreeorfive(x)
