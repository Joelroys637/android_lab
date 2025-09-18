emp={}
sa=[]
for i in range(3):
    item=input("Enter a item Name:")
    price=int(input("Enter a price of the item:"))
    emp[item]=price
    


for j in emp.values():
    sa.append(j)

print("Total bill:",sum(sa))
gst=int(input("Enter a gst persentage:"))
print("Final bill with gst:",(sum(sa)+((sum(sa))*(gst/100))))
    
