

dic={'USD':82.2,'EUR':89.5,'JPY':0.56}


cu=input("Enter a currency like(USD,EUR,JPY):").upper()
amount=int(input("Enter a amount:"))

if cu in dic:
    tot=amount*dic[cu]
    print(f"convert amount in {cu} into IND:",tot)
else:
    print("Not available currency")
