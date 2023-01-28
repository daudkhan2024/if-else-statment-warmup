def say_hi(name):
    print("Good evening!" + name )
say_hi("khan")

def greet_him(name , age ,address):
    print("Good Evening" + name + " your age is " + str(age) + "you are living on " +address )
greet_him("shayan khan", 30, "Nyewsorktreet")


#return statment
def cube(num):
    return num*num*num
print(cube(3))

def cube(num):
    return num*num*num
result = cube(4)
print(result)

#If else statment
is_male = False
is_tall  = True

if  is_male and is_tall:
    print("you are a male")

else:
    print("you are not a male or tall")




