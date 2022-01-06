lst_values = []
def dict_list(d):
    """This method will return the values of a dictionary even if it has the nested dictionary's"""
    for i in d.values():
        if type(i) == dict:
            dict_list(i)
        else:
            lst_values.append(i)
    return lst_values

x = {1:"Vamsi", 2:"2.56", 3:{1:2,6:0}, 4:6+3j}
if type(x) == dict:
    print(dict_list(x))
else:
    print("Enter the Values in Dict Format")
