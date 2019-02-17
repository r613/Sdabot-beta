#v1.2.1
from create import create 
from stf import finish 
from stf import checker
from stf import patt
from stf import hefresh
import time

def finder(list):
    
    if len(list) == 0:
        print "We got no answer"
        return 0
    else:
        pass
    print "Just started a new round and here is the list:"
    print list
    alist = hefresh(list)
    print alist
    print "Stuff:"
    spc,pat = checker(alist) #spc resembles the amount of spaces between each time the pattern repeats itself
    
    if spc == 0:
        print "We are doing one extra round!"
        return finder(alist)
        #we got no answer and we need to figure out what piece of code to stick in here
    else:#we got an answer and were going to deal with that right now
        return finishl(list,pat,spc)
def finishl(list,pat,cs): #gets the list, the pattern, and the length of the pattern 
    
    length = len(list) - 1 
    
    
    end = ( length - (length)%cs )  # The end of the last full pattern
    
    number = list[end]
    #print number 
    nlist = []

    for a in range(0,cs):
        number = number + pat[a]
        nlist.append(number) 
    return nlist





def searcher(list):
    alist = hefresh(list)
    dif = checker(alist)
    if dif == 0: #we got no answer
        print "We got nothing!"
    else: #in any other case - (therefore we got an answer) 
        text = ""
        for i in list:
            text = str(text) + str(i) + " "
        print text
        finish(list,alist,dif)

list = create()
print finder(list)
#list = create()
#print checker([])
#searcher(list)

# 