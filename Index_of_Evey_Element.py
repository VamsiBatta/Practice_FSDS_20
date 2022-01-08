def index(l):
    """This function prints the indexes of every element in a list even if the list contain the repetitive elements"""
    
    for i in range(len(l)):
        print("Index of ",l[i],"is ", i)
        


lst = [5,0,7,3,0,6,2,7]
print(index(lst))
