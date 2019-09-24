import random
import heapq

#Get data
file = "ffm_cond.txt"
data = open(file, "r")
holder = []
for i in data.readlines():
    holder.append(i.split("\t"))
data.close()

#Important parameters
n_ingredients = 3
setsize = 15
mutrange = 100
ev_set = []

#Generate random set
ingredients = [4, 17, 8]
    #4, 17, 8 = game, baking spices, root vegetables
    #3, 16, 11 = seafood, dried herbs, fruiting vegetables
for i in range(setsize):
    x = random.randrange(1,len(holder), step=1)
    templist = []
    templist.append(holder[x][0])
    for q in ingredients:
        templist.append(int(holder[x][q]))
    ev_set.append(templist)

#Get fitnesses
for i in ev_set:
    i.append(sum(i[1:]))

print("You get: ")

#Get 5 highest
fits = [i[n_ingredients+1] for i in ev_set]
highest = heapq.nlargest(5, fits)
hindexes = []
for x in highest:
    tracker = 0
    while (x!=ev_set[tracker][n_ingredients+1]):
        tracker += 1
    if tracker in hindexes:
        tracker += 1
        while (x!=ev_set[tracker][n_ingredients+1]):
            tracker += 1 
    hindexes.append(tracker)
    print("\t", ev_set[tracker][0])


