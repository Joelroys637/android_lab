

tup=()

for i in range(2):
    name=input("Enter a student name:")
    rollno=int(input("Enter a Roll number:"))
    mark=int(input("Enter a total mark of the student:"))

    std=(name,rollno,mark)
    tup=tup+(std,)

for j in tup:
    if j[2]>80:
        print(f"Name:{j[0]},Roll no:{j[1]},Mark:{j[2]}")
