

c=0

dic={'what is your name':'leo','In python who developed':'vimal'}


for i,j in dic.items():
    print(i)
    user_an=input("Enter a answer:")
    if user_an==j:
        c=c+1
print(c)
