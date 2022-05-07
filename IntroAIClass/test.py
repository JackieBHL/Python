
puzz1 = {(1,1):1, (1,2):2, (1,3):3,\
 (2,1):4, (2,2):'B', (2,3):5,\
 (3,1):6, (3,2):7, (3,3):8}
puzz2 = {(1,1):3, (1,2):2, (1,3):1,\
 (2,1):8, (2,2):7, (2,3):6,\
 (3,1):4, (3,2):'B',(3,3):5}

# "flip" key and value roles of a dictionary structure
# example: flip({(1,1):5, (2,1):7}) returns {5:(1,1), 7:(2,1)}
def flip(x):
    y = {}
    for k in x.keys():
        y[x[k]] = k
    return y
def H(p1, p2):
 flip1 = flip(p1)
 flip2 = flip(p2)
 d = 0
 for tile in flip1.keys():
    if tile != 'B':
        d += abs(flip1[tile][0] - flip2[tile][0]) +\
        abs(flip1[tile][1] - flip2[tile][1])
 return d
if __name__ == '__main__':
 result = H(puzz1,puzz2)
 print(result)