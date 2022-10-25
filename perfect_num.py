print("|-------------------------EXPERIMENT NO.21-----------------------------|")
print("|           FINIDING IF THE NUMBER IS PERFECT OR NOT                   |")
print("|----------------------------------------------------------------------|")
total=0
num=int(input("                  Enter a number : "))
print()
for factor in range(1,num+1):
    if num%factor==0:
        if factor==1:
            print("                 ",factor,end="")
            total+=factor
        elif factor>1 and factor<num:
            print("  + ",factor,end="")
            total+=factor
        else:
            print("  =",factor)
    else:
        continue
print("-"*72)
if total==num:
    print("|                  ",num," is a perfect number                             |")
else:
    print("|                  ",num," is not a perfect number                         |")
print("-"*72)

















