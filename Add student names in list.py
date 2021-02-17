#Program to add no of students name in empty list
result=[]  #created an empty list
n=int(input("Number of student entry you want:\n"))  #enter whatever no. of entry's you want to make
a=0   #a is o here to initalialise counter
while a<n:
    Name = input("Please enter student name :\n")
    result.append(Name)     #name will append in the result list
    a = a + 1
print()
print("Hers is your list of students",result)