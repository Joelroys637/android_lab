

tup=()

for i in range(2):
    ide=int(input("Enter a id:"))
    name=input("Enter a employee name:")
    des=input("Enter a designation:")
    salary=int(input("Enter a salary:"))

    std=(ide,name,des,salary)
    tup=tup+(std,)

for j in tup:
    if j[3]>50000:
        print(f"Name:{j[1]}")
