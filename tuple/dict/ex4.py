emp = {}

for i in range(2):
    bookid = input("Enter a book id: ")
    title = input("Enter a book title: ")
    emp[bookid] = title

search = input("Enter a book id: ")

if search in emp.keys():
    print(emp[search])

else:
    print("book is not found")
