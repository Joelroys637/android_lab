

tup=()

for i in range(3):
    pnr=int(input("Enter  a PNR number:"))
    name=input("Enter a  name:")
    age=int(input("Enter a Age:"))
    seatno=int(input("Enter a seat No:"))

    std=(pnr,name,age,seatno)
    tup=tup+(std,)
print("Senior Citizens")
for j in tup:
    if j[2]>60:
        print(f"Name:{j[1]}")
