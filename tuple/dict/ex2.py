emp={}
sa=[]
for i in range(3):
    empname=input("Enter a NAme:")
    salary=int(input("Enter a salary:"))

    emp[empname]=salary
print(emp)
up_emp=input("Enter a emp name to update a salary:") 
up_salary=int(input("ENter a update salary:"))
emp[up_emp]=up_salary
print("Update salary list:",emp)
for j in emp.values():
    sa.append(j)

print("total salary expense of the company:",sum(sa))
    
