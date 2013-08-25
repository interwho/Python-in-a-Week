#Print story
print "As you know the inventor of the game chess was quite a clever fellow.  As the story goes, the inventor presented the game to the king and the king was quite pleased.  The king asked what the inventor wanted as payment. He asked for a grain of cereal for the first square and to have each of the next 63 squares double the previous square.  As the story goes the king agrees, but was not too pleased by the final payment."
print "\nThis is what the king had to pay:"
#start calculations (by grain)
i = 2
t = 1
print "1 grain for square 1" #print first square's result
while i < 65 :
    n = t * 2
    t = n
    print str(n) + " grains for square " + str(i) #print each square's result
    i = i + 1
#start calculations (by pound)
print "\nIn pounds, that's:"
i = 2
t = 1
print "0.00014285714 pounds of grain for square 1" #print first square's result
while i < 65 :
    n = t * 2
    t = n
    b = float(n)
    print str(b/7000) + " pounds of grain for square " + str(i) #print each square's result
    i = i + 1
print "\nThat's a lot of grain!"
raw_input("Press the return key to exit") #Exit pause
