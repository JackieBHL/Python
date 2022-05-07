CLS = [['P','notQ','R'],['notP','Q','R']]
CHEM = [['notCO2','notH2O','H2CO3'],['notC','notO2','CO2'],
        ['notMgO','notH2','Mg'],['notMgO','notH2','H2O'],
        ['MgO'],['H2'],['O2'],['C'],['notH2CO3']]
GOV = [['T','notE','D'],['notT','C'],['E','notD','I'],
        ['notG','notD','I'],['T','C','notD','G'],['notC'],
        ['notI','notG'],['D'],['E']]

def try_resolvent(count,c1,c2):
    res = None
    for lit1 in c1:
        for lit2 in c2:
            if is_complement(lit1,lit2):
                print("\n[%d.] Resolving %s and %s ...." % (count,c1,c2))
                print("... found compl lits (%s,%s)" % (lit1,lit2))
                res = c1[:]
                res.remove(lit1)
                for x in c2:
                    if not x in res and x != lit2:
                        if complement(x) in res:
                            return True
                        else:
                            res.append(x)
                return res
    print("No resolvent")
    return res

def is_complement(x,y):
    if len(x) >= 4 and x[:3] =='not':
        return x[3:]==y
    elif len(y) >= 4 and y[:3] =='not':
        return x==y[3:]    
    else: 
        return False

def complement(x):
    if len(x) >= 4 and x[:3] =='not':
        return x[3:]
    else:
        return 'not'+x

def same_clause(c1,c2):
    if not len(c1) == len(c2):
        return False
    for x in c1:
         if not x in c2:
             return False
    return True


def new_clause(labcls,cl):
    for x in list(labcls.values()):    #  .... in Python3 make it list(labcls.values())
        if same_clause(x,cl):
            return False
    return True

def show_and_select(labcls):
    select = None
    print ("\n")
    for i in list(labcls.keys()):           #   ... in Python3 make it list(labcls.keys())
        print ("[%d] %s" % (i, labcls[i]))
    print ("\n")
    print ("Pick two clauses by their number ...")
    first = int(input("First clause: "))
    second = int (input("Second clause: "))
    return (first,second)

def interact_resolve(cls):
    count = 1
    labelled_cls = {}  # will be contain pairs  number:clause, e.g., {1:['A','notB'], 2:[B,C],...}
    no = 1
    
    for x in cls:
        labelled_cls[no] = x
        no+=1

    while True and count <= 100:
        (i,j) = show_and_select(labelled_cls)
        res = try_resolvent(count,labelled_cls[i],labelled_cls[j])

        if res == None:
            continue
        
        if res == []:
            print ("... empty new clause []")
            print ("\nUNSATISFIABLE :-)")
            return  'UNSAT'

        if res != True:
            if new_clause(labelled_cls,res):
                labelled_cls[no] = res
                no+=1
                print ("... new clause %s added" % res)
            else:
                print ("... this clause already exists")
        count+=1

    if count > 100:
        print ("100 resolutions tried without Contradiction")
        print ("We have no answer :-|")
    return

if __name__ == "__main__":
#    print("________Test function__Try_resolvent___compements_______")
#   print("CHEM list: ")
#    for c in CHEM:
#        print(c)
#    print("\nGOV list: ")
#    for c in GOV:
#        print(c)
#    print("\nCLS list: ")
#    for c in CLS:
##        print(c)
#    print("\n___default__testing___functions___USING LIST CHEM_")    
#    print("is_complement('C','notC'):")
#    print(is_complement('C','notC'))
#    print("\n")

#    print("is_complement('C','C'):")
 #   print(is_complement('C','C'))
 #   print("\n")

 #   print("comp = complement('C')")
#    comp = complement('C')
#    print(comp)
#    print("\n")

#    print("comp = complement('notH2CO3')")
#    comp = complement('notH2CO3')
#    print(comp)
#    print("\n")

 #   print('c1 = CHEM[4]')
#    c1 = CHEM[4]
#    print(c1)
#    print("\n")

 #   print('c2 = CHEM[2]')
 #   c2 = CHEM[2]
 #   print(c2)
#    print("\n")

 #   print("try_resolvent(1,c1,c2)")
 #   try_resolvent(1,c1,c2)
 #   print("\n")

  #  print("\n c0 = CHEM[0]")
 #   c0 = CHEM[0]
 #   print(c0)
 #   print("\n")

 #   print("try_resolvent(1,c0,c2)")
 #   try_resolvent(1,c0,c2)
#    print("\n")

#    print("res=try_resolvent(1,c0,c2)")
#    res=try_resolvent(1,c0,c2)
#    print('res')
#    print(res)
#    print("___default__testing___functions____")    
#    print("________Test function__Try_resolvent___compements_______\n")
    
    print("_____interact recolve________")
    test = 1
    while(test == 1):
        types = input("Choose one of the types: CHEM , CLS, GOV: ")
        if(types == 'CHEM' or types == 'CLS'  or types == 'GOV' ):
            test = 0
            if(types == 'CHEM'):
               list_to_use = CHEM
            if(types == 'CLS'):
                list_to_use = CLS
            if(types == 'GOV'):
                list_to_use = GOV
        else:
           print("choose the correct one!")

    print("interact recolve: %s" % types)

    interact_resolve(list_to_use)

