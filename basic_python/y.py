"""lst=[1,2,3,4]

emptylst=[]

for x in lst:

    emptylst.append(x*x)

print(emptylst)

######################

print({x:x*x for x in lst })

###########################

lst1=[[1,2],[2,4],[3,6],[4,98]]

emptylst1=[]

for x in lst1:

    for y in x:

        emptylst1.append(y*y)

print(emptylst1)

#########################

print([y*y for x in lst1 for y in x ])

########################"""
 
'''##########################

x = lambda a,b: [x*x for x in range(a,b)]
 
print(x(0,6))

##########################'''



"""##########################

lst=[1,2,3,4]
 
def triplenum(x):

    if (x>2):

        return x*3

print(list(map(triplenum,lst)))
 
"""

def is_even(n):

    return False
 
# Define a list of numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# Use filter to filter out even numbers

even_numbers = filter(is_even, numbers)

even_numbers1 = map(is_even, numbers)

print("Even numbers:", list(even_numbers))  

print("Even numbers:", list(even_numbers1))
 
 
 
 
 