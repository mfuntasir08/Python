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
 
secret_number = 47
guess_count = 0
guess_limit =3
while guess_count < guess_limit :
     guess = int(input("Guess: "))
     guess_count += 1
     if guess == secret_number:
          print("You won!")
          break
         
else:
 print("Sorry, you failed.")   
   









