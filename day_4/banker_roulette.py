# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#Get the total number of itemms in list
num_items = len(names)
#Generate random numbers between 0 and the last index
random_choice = random.randint(0, num_items -1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today")