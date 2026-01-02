import math
import time

def menu():
    print("Will you like to, \n 1. add \n 2. subtract \n 3. multiply \n 4. divide \n 5. root \n 6. index")

    option = int(input())
    if option <= 0 or option >= 7:
     print("Option not found" '\n')
  

    else:
        print('enter your value(s)')

        num1 = float(input())
        num2 = float(input())

        if option == 1:
         print ("your sum is:")
         time.sleep(2)
         print (num1 + num2)
        elif option == 2:
         print ("your differnce is:")
         time.sleep(2)
         print (num1 - num2)
        elif option == 3:
         print ("your product is:")
         time.sleep(2)
         print (num1 * num2)
        elif option == 4:
         print ("each person gets:")
         time.sleep(2)
         print (num1 / num2)
        elif option == 5:
         print (math.sqrt (num1))
         time.sleep(2)
         print ("is it a perfect square?")
        elif option == 6:
         print (num1 ** num2)
        

    
print('Start time: %s' %time.ctime())
time.sleep(1)

print ("\nHey there, Let's get calculating")
print ("Input your name:")




print ("Hello %s" % (str.upper(input())))
print ("This basic calculator works with two or less values per operation at a time. \nI hope you enjoy it.")

menu()
time.sleep(2)

print('WILL YOU LIKE TO TRY AGAIN? \n \nPRESS Y FOR YES AND N FOR NO')
choice =str.upper(input())

while choice =="Y":
    menu()
    time.sleep(2)
    print('WILL YOU LIKE TO TRY AGAIN? \n \nPRESS Y FOR YES AND N FOR NO')
    choice = str.upper(input())
if choice == "N":
    print("THANK YOU FOR YOUR TIME \n \nPRESS ENTER TO EXIT")
    input()




      
      
