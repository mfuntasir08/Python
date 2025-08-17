# print('*' * 11)

#  VARIABLE
 
# name = 'John Smith'

# is_new_patient = True
# print(name,age,is_new_patient)

# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print(name  + ' likes ' +  color)

# birth_year = input("Enter your birth year: ")

# age = 2025 - int(birth_year)

# print(age)
 
# name = input("What is your name? ")


# weight = input("Enter your weight in lbs: ")
# weight_kgs = float(weight) * 0.45
# print( weight_kgs)

# name = "John Smith"
# # print(name[1:-1])

# text = "My name is " f'{name} ,' + " i am " f'{age}'" year old."
# print(text)

# password = input("Enter your password: ")

# if len(password) < 6:
#     print("Password must be at least 6 characters long.")
# else :
#     print("Password is valid.")

# course = 'python for newbies'
          
# print(course.find('e'))

# is_hot = False
# is_cold = False
# if is_hot:
#   print("It's a warm day.")
#   print("Drink plenty of water.")
# elif is_cold:
#   print("It's a cold day.")
#   print("Wear warm clothes.")
# else:
#   print("It's a lovely day.")

# print("Enjoy your day!")


#   print('You need to put down 10%')
#   print("Down payment :$" + str (f'{house_price} * 0.1'))
# else:
#     print('You need to put down 20%')
#     print("Down payment :$" + str(f'{house_price * 0.2}'))

# price = 1000000
# has_good_credit = False
# if has_good_credit:
#   down_payment = price * 0.1
# else:
#   down_payment = price * 0.2
# print(f"Down payment: ${down_payment}")

# name = 'JOHN SMITH'
# age = 20
# print(f"My Name Is {name} And I Am {age} Years Old.")
 
# name = input("Enter Your Name: ")
# if len(name) < 3 :
#   print("Name must be at least 3 characters")
# elif len(name) > 50:
#   print("Name can be a maximum of 50 characters")   
# else :
#   print("Name looks good!")

# weight = input("Enter your weight: ")

# unit = input("(L)bs or (K)gs: ")

# if unit.upper() == "L":
#    print(f"You are {float(weight) * 0.45} kilos.")
# elif unit.upper() == "K":
#    print(f"You are {float(weight) * 2.20462} pounds.")
 
# secret_number = 47
# guess_count = 0
# guess_limit =3
# while guess_count < guess_limit :
#      guess = int(input("Guess: "))
#      guess_count += 1
#      if guess == secret_number:
#           print("You won!")
#           break
         
# else:
#  print("Sorry, you failed.")   

# key_word1 = "help"
# key_word2 = "start"
# key_word3 = "stop"
# key_word4 = "quit"
# is_started = False

# while True:
#     key_word = input("> ").lower()

#     if key_word == key_word1:
#         print("start - to start the car")
#         print("stop  - to stop the car")
#         print("quit  - to exit")
#     elif key_word == key_word2:
#      if is_started :
#         print("Car is already started")
#      else:
#         is_started = True
#         print("Car started... Ready to go!")
#     elif key_word == key_word3:  
#       if not is_started:       
#         print("Car is already stopped")
#       else:  
#         is_started = False                   
#         print("Car stopped.")

#     elif key_word == key_word4:
#         print("Exiting game...")
#         break    
#     else:
#         print("I don't understand.")

#  for loop
# prices = [10, 20, 30, 40, 50]
# sum = 0

# for price in prices :
#   sum += price
# print(sum)

# numbers = [1, 1, 1, 6]
# for x_count in numbers:
#    output = ''
#    for count in range(x_count):
#     output += 'X'
#    print(output) 

# numbers = [3,6,9,3,4,0,1]
# max = numbers[0]
# for number in numbers :
#   if number > max :
#     max = number
# print(max)

# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# for row in matrix :
#   for item in row:
#     print(item)

# numbers =[2,6,23,56,87,2,45,87]
# unique = []
# for number in numbers:
#   if number not in unique:
#     unique.append(number)
# print(unique)

# phone_number = input("enter your phone number")
# digits={
#   "1":"one","2":"two","3":"three","4":"four",
#   "5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"
# }
# output = ""
# for ch in phone_number:
#  output += digits.get(ch,) + " "
# print(output)

