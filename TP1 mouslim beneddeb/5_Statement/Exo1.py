count = 0
for i in range(1,30):
    if i%3==0 :
        print(f"{i} Divisible by 3")
        count =count+1
    else:
        print(f"{i} Not Divisible by 3")

print(count)