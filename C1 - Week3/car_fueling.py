#Python3
#Fibonacci- week -3 - assign3

def calRefill(distance,capacity,stops):
    currentFill = 0
    lastFill = 0
    count = 0
    i=0
    while i <len(stops):
        while i <len(stops) and stops[i] - lastFill <= capacity:
            currentFill = stops[i]
            i = i+1
        if currentFill == lastFill:
            return -1
        if currentFill < distance:
            count = count+1
            lastFill = currentFill
    return count
    
distance = int(input())
capacity = int(input())
noOfStops = int(input())
stops = list(map(int,input().split()))
stops.append(distance)
print(calRefill(distance,capacity,stops))

