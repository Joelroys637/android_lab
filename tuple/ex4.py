

tup=()
to=()
for i in range(2):
    name=input("Enter a player name:")
    run=int(input("Enter a Run:"))
    wicket=int(input("Enter a Wicket:"))
    
    std=(name,str(run),wicket)
    tup=tup+(std,)

for j in tup:
    t=j[1]
    de=(t)
    to=to+(de,)
high_run=max(to)
print(high_run)
for k in tup:
    if k[1]==high_run:
        print(f"High runer Name:{k[0]}")
