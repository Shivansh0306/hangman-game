import time
time.sleep(1)
print("***********************GUESS THE WORD**************************************\n")
time.sleep(1)
print("you have 6 lifelines to guess the word")
l0="coding"
l1=list(l0)
l8=''.join(l1)
l9=l8.upper()
length=len(l1)
l2=[]
life=6
for i in range(length):
    l2.append('_')
print(l2)

while(l2!=l1 and life!=0):
    letter=input("enter a letter ")
    count=l1.count(letter)
    cnt=count
    if count==0:
        life=life-1;
        print("this letter is not in the word,you have only {} lifes remaining\n".format(life))
    else:
        l3=''.join(l1)
        l2=''.join(l2)
        if letter in l2:
            print(f"{letter} is already used once in the game\nenter a different letter")
        else:
            s=-1
            while count!=0:
                l4=l3.find(letter,s+1,len(l1))
                s=l4
                count-=1
                if s==-1:
                    break
                else:
                    l2=list(l2)
                    l2.pop(l4)
                    l2.insert(l4,letter)


            print(f"{letter} is in the word {cnt} times")
            print(l2)
l6=''.join(l2)
l7=l6.upper()
            
if(l1==l2):
    print(l9)
    print("hurrah you won the game")
else:
    print("GAME OVER")
    print(f"THE LETTER WAS {l9}")

        
