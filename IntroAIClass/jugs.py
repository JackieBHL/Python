max_jug = [3,4]

#start with empty two jug

def jugs_goal_fct(jugs,goal):       
    return jugs==goal

def jugs_eval_fct(jugs,goal):
    return 0

def jugs_successor_fct(jugs):
    succs =[]
    moves = [fill_jug3(jugs),\
             fill_jug4(jugs),\
             dump_jug3(jugs),\
             dump_jug4(jugs),\
             pour_jug34(jugs),\
             pour_jug43(jugs)]
    for x in moves:
        if x != None:
            succs.append(x)
    return succs

def show_jugs(jugs):
    if jugs == None:
        return
    i=1
    print (jugs) 
    for i in range(1,3):
        print("jugs %s : "% i , end = '')
        if i==1:
            for j in range(0,jugs[0]):
                print ("@ ",end = '') #end = '' prevent from going to next line
        if i==2:
            for j in range(0,jugs[1]):
                print ("@ ",end = '') #end = '' prevent from going to next line
        print ("")
    return jugs

#three sequence 
#fill --- fill all 
def fill_jug3(jugs):
       newjugs = jugs[:]   # [:] creates a copy of list
       newjugs[0]=3
       return newjugs
def fill_jug4(jugs):
       newjugs = jugs[:]   # [:] creates a copy of list
       newjugs[1]=4
       return newjugs
#dump --- dump all

def dump_jug3(jugs):
    newjugs = jugs[:]   # [:] creates a copy of list
    newjugs[0]=0
    return newjugs
def dump_jug4(jugs):
    newjugs = jugs[:]   # [:] creates a copy of list
    newjugs[1]=0
    return newjugs
#pour --- dump all to to other jug, if over maximum of jug limit stop

def pour_jug34(jugs):
    #from x to y 
    newjugs = jugs[:]   # [:] creates a copy of list
    for i in range(0,3):
        if newjugs[0]==0:
            break
        if newjugs[1]==4:
            break
        newjugs[0] = newjugs[0]-1
        newjugs[1] = newjugs[1]+1
        i += 1

    return newjugs
def pour_jug43(jugs):
    #from x to y 
    newjugs = jugs[:]   # [:] creates a copy of list
    for i in range(0,3):
        if newjugs[1]==0:
            break
        if newjugs[0]==3:
            break
        newjugs[0] = newjugs[0]+1
        newjugs[1] = newjugs[1]-1
        i += 1

    return newjugs

#result two jug with different size only jug with 4 L contain 2Liter 3L jug is empty 

