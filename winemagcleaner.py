import heapq

class varietal:
    def __init__(self):
        self.variety = ""
        self.notes = []
        self.freqs = [0]*200
        self.match = []

    def setVariety(self, x):
        self.variety = x

    def appendNote(self, note):
        self.notes.append(note)
        
def removeVals(the_list, val):
   return [value for value in the_list if value != val]

f1 = "winemag_clean.csv"
data = open(f1,'r')
arg = data.readlines()
arr = []
for i in arg:
    arr.append(i.split(","))
master = []
varietals = []

#Populate object list
for i in arr[1:]:
    if i[0] not in varietals:
        varietals.append(i[0])
for i in varietals:
    v = varietal()
    v.setVariety(i)
    master.append(v)

#Computation
for j in master:
    for i in arr:
        if j.variety==i[0]:
            for x in range(1,5):
                if i[x] != " " and i[x] not in j.notes:
                    j.appendNote(i[x])
                    index = j.notes.index(i[x])
                    j.freqs[index] +=1
                elif i[x] != " " and i[x] in j.notes:
                    index = j.notes.index(i[x])
                    j.freqs[index] +=1
    j.freqs = removeVals(j.freqs, 0)
    
#Take input
i_args = ['apple','lemon zest']
compatible = []
compatibilities = []
for j in master:
    for i in i_args:
        if i in j.notes and j.variety not in compatible:
            compatible.append(j)
for j in compatible:
    for q in j.notes:
        for i in i_args:
            if q==i and q not in j.match:
                #j.match.append(q)
                j.match.append(j.freqs[j.notes.index(q)]/sum(j.freqs))
    compatibilities.append(sum(j.match))
#print(compatible[20].variety, compatible[20].match)
print("Best matching varietals are:")
highest = heapq.nlargest(5,compatibilities)
matches = []
for i in highest:
    for j in compatible:
        if sum(j.match)==i:
            print(j.variety, str(i/sum(highest))+"%")


        
    
        

                    
                    
                    
                
    




        
