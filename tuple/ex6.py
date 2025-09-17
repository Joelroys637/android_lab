

tup=()

for i in range(3):
    movie_name=input("Enter a movie name:")
    ticket_no=int(input("Enter a ticket number:"))
    seat_no=int(input("Enter a seat number:"))

    std=(ticket_no,movie_name,seat_no)
    tup=tup+(std,)
sp=input("Enter  a specified movie search the seat number:")
print(sp)
for j in tup:
    if j[1]==sp:
        print(f"seat:{j[2]}")
    
