def concat(*lsts):
    a = []
    for i in range(len(lsts)):
        a.extend(lsts[i])
    return a
    
print(concat([1,2,3,4],[9,5,9],[60,4,7],[6,9.6,5],[87,65,4]))
