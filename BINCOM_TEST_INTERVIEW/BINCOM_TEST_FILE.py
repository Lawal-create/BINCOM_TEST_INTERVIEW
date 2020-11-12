import re

color={}
days_of_the_week=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"]
#Extract the colors from the html file provided ‘python_class_test.html’, using regular expression
with open("python_class_test.html","r") as file:
    line=file.read()
    colors=re.findall(r"<td>(.+?)</td>",line)

#Store them in a dictionary, using color as key and their frequency as values.
for val in days_of_the_week:
    colors.remove(val)

for value in colors:
    vals=value.split(",")
    for i in vals:
        i=i.strip()
        color[i]=color.get(i,0)+1
color.pop("")
print(color)

#Which color of shirt is the mean color?
def mean(colo):
    mean_value=sum(colo.values())/len(colo)
    mean_value=round(mean_value,0)
    for k,v in colo.items():
        if v==mean_value:
            return k
        elif v==mean_value+1 or v==mean_value-1:
            return k
print(mean(color))

#Which color is mostly worn throughout the week?
def maxvalue(colo):
    v=list(colo.values())
    k=list(colo.keys())
    return k[v.index(max(v))]

print(maxvalue(color))

def getMedianIndex(colo):
    sum_val=0
    sorted_values=sorted(colo.values())
    middle_values=round(sum(sorted_values)/2,0)
    for i in range(0,len(sorted_values)):
        sum_val+=sorted_values[i]
        if(sum_val)>=middle_values:
            return sorted_values[i]

#Which color is the median?
def Median(x):
    for k,v in x.items():
        if v==getMedianIndex(x):
            return k

print(Median(color))
#BONUS Get the variance of the colors
def variance(colo):
    listed=[]
    list1=[]
    mean_value=sum(colo.values())/len(colo)
    mean_value=round(mean_value,0)
    for k,v in colo.items():
        x=v-mean_value
        listed.append(x)
    for i in listed:
        y=i**2
        list1.append(y)
    return sum(list1)/len(colo)
        
print(variance(color))

#if a colour is chosen at random, what is the probability that the color is red?
def probability(string_value,colo):
    total=sum([i for i in colo.values()])
    for k,v in colo.items():
        if k==string_value:
            prop=round(v/total,4)
    return prop


print(probability("RED",color))

#write a recursive searching algorithm to search for a number entered by user in a list of numbers
def recursivesearch(list1,low,high,value):
    if high<1:
        return -1
    if list1[low]==value:
        return 1
    if list1[high]==value:
        return  high
    return recursivesearch(list1,low+1,high-1,value)


import random
#To get the gray code of 4 digits with only 0's and 1's
def bits_of_gray(n):
    """Takes an integer and return the gray code sequence for it."""
    
    if (n<=0):
        return None
    
    array=list()
    array.append("0")
    array.append("1")
    i=2
    j=0
    while(True):
        if i>=1<<n:
            break
        for j in range(i-1,-1,-1):
            array.append(array[j])

        for j in range(i):
            array[j]="0"+array[j]

        for j in range(i,2*i):
            array[j]="1"+array[j]
        i=i<<1

    return array
#Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10
def generate(n):
    if n==4:
        random_list=bits_of_gray(n)
        random_number=random.choice(random_list)
        return (random_number,int(random_number,base=2))

print(generate(4))


#Write a program to sum the first 50 Fibonacci sequence
def fibonnaci_num(x):
    assert x>=5000000000 and x<=6000000000
    assert type(x)==int
    """"Takes in an integer and finds out the fibonnaci sequence of the integer: """
    a,b=0,1
    fibo=[a,b]
    while True:
        a,b=b,a+b
        fibo.append(b)
        if b>=x:
            break

    return sum(fibo) if len(fibo)==50 else len(fibo)

print(fibonnaci_num(5000000000))







