
def hefresh(list):
    alist = []
    for i in range(len(list)-1):
        alist.append( (list[i+1]) - (list[i]) )
    return alist 
def fib(list):
    if len(list) < 4:
        return False
    for a in range (len(list)-2):
        if list[a] + list[a+1] != list[a+2]:
            return False
    return True 
def multi(list):
    if len(list) < 4:
        return 0
    length = len(list) -1 
    dif = float(list[1]) / list[0]
    for a in range (length - 1):
    
        if list[a] * float(dif) != float(list[a+1]):            
            
            return 0
    
    number = float(list[length])
    nlist = []
    for a in range(2):
        number = float(number) * float(dif)
        nlist.append(float(number))

    return nlist 
def finish(list,alist,cs):
    length = len(list) - 1
    
    
    end = ( length - (length)%cs ) 
    
    number = list[end]
    #print number 
    nlist = []

    for a in range(0,cs):
        number = number + alist[a]
        nlist.append(number) 
    return nlist

def checker(list): #this program checks if we got a repetetive pattern, 
                    #if there is a pattern, the program returns the number of spaces between each time the pattern repeats itself
                    # Returns the pattern (one time only)
    
    for stc in range(1, (len(list)/2) + 1): #stc space to check (couldn't come up with something better than this)) (it's half which might make it one before the end, but on the other hand the length is the full length (not including zeros))
        if list[0] == list[stc]:
            if patt(list,0,stc): #patt checks if this pattern is consistant throughout the entire list
                alist = []

                for i in range(stc):
                    alist.append(list[i])
                return stc,alist

                
            else:
                pass
        else:
            pass
    return 0,0 #This means that we got nothing 

def patt(alist,cs,stc): #Checks if the pattern given is consistant
    for i in range(cs, (len(alist)-(stc-cs) -1) ): #we go though the entire 
        if alist[cs+i] == alist[stc+i]:
            pass
        else:
            return False 
    print "We have confirmed that the sequence starts at " + str(cs)  + " and at: " + str(stc) + " and repetetive from there until the end. "

    return True 