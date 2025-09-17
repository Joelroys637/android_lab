

tup=()
de=()
cr=()
for i in range(4):
    date=input("Enter a tranction date like(20/01/2021):")
    amount=int(input("Enter a amount:"))
    types=input("Enter a which type of transaction like(debit or credit):")
    fi_type=types.lower()
    std=(date,amount,fi_type)
    tup=tup+(std,)

for j in tup:
    if j[2] in 'debit':
        
        dat=f"date:{j[0]}"
        am=f"amount:{j[1]}"
        ty=f"type:{j[2]}"
        deb=(dat,am,ty)
        de=de+(deb,)
    elif j[2] in 'credit':
        dat=f"date:{j[0]}"
        am=f"amount:{j[1]}"
        ty=f"type:{j[2]}"
        cre=(dat,am,ty)
        cr=cr+(cre,)
    elif j[2] not in 'debit' and 'credit':
        print("Invalid transaction occure")

print("Display in Debit transaction")
for k in de:  
    print(k)
    
print("Display in Credit transaction")
for h in cr:
    print(h)




