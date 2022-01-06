def primitive(l):
    """This Method Will return the Indexes and Values of the Primitive elements in a list """
    Values = []
    Indexes = []
    if type(l) == int or type(l) == bool or type(l) == str or type(l) == float:
        print("0")
    elif type(l) == list:
        for i in range(len(l)):
            if type(l[i]) == int or type(l[i]) == bool or type(l[i]) == str or type(l[i]) == float:
                Values.append(l[i])
                Indexes.append(i)
            elif type(l[i]) == tuple or type(l[i]) == str or type(l[i]) == list or type(l[i]) == complex or type(l[i]) == dict:
                continue
    a = dict(zip(Indexes, Values))
    return a
    
x = [5, 20.4, "Vamsi", [1,2,3], True, 3+6j]
print(primitive(x))
