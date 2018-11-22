"""
Code Challenge #10

See README.md for instructions

"""



# Your code here
import csv


class AnimalSearchApp():
    Animal = []
    def __init__(self):
        with open('animal_IO_Data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.Animal.append(row)

    def search_by_id(self,identify):
        #self.identify = identify 
        info = []
       
        for row in self.Animal:
            x = row['AnimalID']
            if identify == x:
                return row
            else: 
                return None    
        return info



    def search_by_type(self,typical):
        info = []
       
        for row in self.Animal:
            x = row['AnimalType']
            if typical == x:
                info.append(row)

        return info[:24]

    def search_by_breed(self,breed):
        info = []
       
        for row in self.Animal:
            x = row['PrimaryBreed']
            if breed == x:
                info.append(row)

        return info[:24]

    def search_by_color(self,color):
        info = []
       
        for row in self.Animal:
            x = row['PrimaryColor']
            if color == x:
                info.append(row)
        return info[:24]



print("Welcome to AnimalSearchApp")
print("-"*30)

#user_input = input("Please select a number to search by: \n[1]ID\n[2]Type\n[3]Breed\n[4]Color\n[5]to quit ")
while True:
    user_input = input("Please select a number to search by: \n[1]ID\n[2]Type\n[3]Breed\n[4]Color\n[5]to quit\n ")
   
    if user_input == '1':
        doggie = input("Please enter the ID of the animal: ")
        print(AnimalSearchApp().search_by_id(doggie))
    

    if user_input == '2':
        pets = input("Please enter the animal type: ")
        pets = pets.upper()
        print(AnimalSearchApp().search_by_type(pets))
    

    if user_input == '3':
        lock = input("Please enter a breed: ")
        print(AnimalSearchApp().search_by_breed(lock))

    if user_input == '4':
        co = input("Please enter a color: ")
        print(AnimalSearchApp().search_by_breed(co))

        
    if user_input == '5':
        break
    
    
    

"""
Questions:

What is the first argument for each method you create on the AnimalSearchApp class, what is the value of this argument?
The argument for each method is the self argument. It acts like a place holder for anything related to the class. 

With object oriented programming we can encapsulate data and behavior into a class definition. Whey is this a good idea?
This allows us to build our own class so that we can apply to the program that is being written. It keeps everything organized while also
providing easy access to things we build.

If I wanted to write another program that uses the functionality provided by your AnimalSearchApp class, 
but I wanted to modify it to suit my needs, how would I accomplish this?
You would need to create a sub class. A way to do this would be putting the parent class in the parentheses 
after naming the sub class. An example would be: Dogs(AnimalSearchApp).
"""