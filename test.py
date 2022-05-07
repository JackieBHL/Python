trps = [4,2,0,3,2,5]


class Solution(object):
    def trap(self, height):
        if len(height)==3:
            temp = self.withintrap(0,2,height)
            return temp
        temp = 0
        starting = 0
        end = 0
        #set initial
        for i in range(1,len(height)-1):
            if height[starting] <= height[i]:
                starting =  i
            else:
                if height[i+1] >= height[starting]:
                    end=i+1
                    print('in')
                    temp = temp+ self.withintrap(starting,end,height)
                    starting = end

        while starting < len(height)-1:
            newarray = []
            for i in range(starting,len(height)):
                newarray.append(i)
                maximum = max(newarray)
            for i in range(starting,len(height)):
                if height[i] == maximum:
                    maxloc = i
            extra = self.withintrap(starting,maxloc,height)
            temp = temp+ extra
            starting = maxloc
        return temp
    def withintrap(self,boundery0,boundery1,array):
        amount = 0
        minimum = min(array[boundery0],array[boundery1])
        for i in range(boundery0+1,boundery1):
            amount = amount + (minimum - array[i])
        if amount < 0:
            amount = 0
        return amount
        
        

trapwater(trps)
