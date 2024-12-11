number = int(input("please input a whole number: "))

note1 = number//100
note2 = (number%100)//50
note3 = ((number%100)%50)//10

print("note1",note1)
print("note2",note2)
print("note3",note3)
