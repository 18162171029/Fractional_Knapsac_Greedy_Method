W=int(input('Enter the weight of knapsac: '))
profits=[int(i) for i in input('Enter the profit of different items: ').split(' ')]
weights=[int(i) for i in input('Enter the weights of different items: ').split(' ')]

ratio=[]
for i in range(len(weights)):
    ratio.append(profits[i]/weights[i])
 
knapsac=[]
for j in range(len(ratio)):
    ind=ratio.index(max(ratio))
    if (W-weights[ind])>=0:
        W=W-weights[ind]
        knapsac.append(profits[ind])
        ratio[ind]=0
    else:
        if W>=0:
            frac=W/weights[ind]
            W=W-(weights[ind]*frac)
            value=frac*profits[ind]
            knapsac.append(value)
            ratio[ind]=0
    
if 0 in knapsac:
    knapsac.remove(0)
    
print('\nHence choosen profits are: ', *knapsac)
print('\nTherefore total profit is: ', sum(knapsac))

