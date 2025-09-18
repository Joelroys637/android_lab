


dic=[]
value=[]
for i in range(2):
    name=input("Enter a name:")
    mark=int(input("Enter a mark:"))
    detail={name:mark}
    dic.append(detail)
for j in dic:
    
    va=list(j.values())[0]
    value.append(va)
    
print("Maximum mark of the student:",max(value))
print("Minimum mark of the student:",min(value))
print("Average mark of the class:",(sum(value)/len(value)))
