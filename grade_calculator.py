'''
Code Challenge: Grade Calculator

See Readme.md for instructions

Problem Analysis

Inputs: grade

Outputs: average, letter grade, message 

Algorithm (Steps in Program): get the users grade, calculate the average, make sure the grade is valid,
figure out the letter grade, create messages applying to each letter grade, output the information


'''

'''
Calculate the Average
    - This should take the total and the count and return the average
Function Analysis
Inputs: The users grade
Outputs: The average of all of the users grades
Algorithm: Take all each grade that the user inputs and add them all together. Take the total and divide it by
the amount of grades the users inputted. The answer is the average.
'''
def calculate_avg(total,counter):
    avg = int(total/ counter)
    return avg
'''
Get the letter grade
    - This should take the average grade and return the letter grade
Function Analysis
Inputs: calculate_avg function
Outputs: Lgrade which is the letter grade.
Algorithm: Using the average of the number grades from the calculate_avg
function, use if statements to interpret the number and group it into 
certain letter grades. Return the letter grade at the end. 
'''
def get_letter_grade(avg):
    if avg <= 100 and avg >= 95:
        lgrade = "A"
    elif avg <= 94 and avg >= 90:
        lgrade = "A-"
    elif avg <= 89 and avg >= 85:
        lgrade = "B"
    elif avg <= 84 and avg >= 80:
        lgrade = "B-"
    elif avg <= 79 and avg >= 75:
        lgrade = "C"
    elif avg <= 74 and avg >= 70:
        lgrade = "C-"
    elif avg <= 69 and avg >= 65:
        lgrade = "D"
    elif avg <= 64 and avg >= 60:
        lgrade = "D-"
    elif avg <= 59 and avg >= 0:
        lgrade = "F"

           
    return lgrade
'''
Validate user input
    - This should take the input and return a boolean
Function Analysis
Inputs: the grade
Outputs: true or false
Algorithm: Change the grade into an int and if the grade is between 0 and 100 
return it as true, if not return it as false. 
'''
def validate_input(x):
    x = int(x)
    if x >= 0 and x <=100:
        return True
    else:
        return False 
   
    


'''
Get the inspirational message
    - This should receive the letter grade and return the message
Function Analysis
Inputs: the Letter grade
Outputs: string statement on what this grade means.
Algorithm: Several If statements that interprets the get_letter_grade function and returns a statement 
depending on what grade it is.
'''

def get_message(g):
    if g == "A":
        return "Excellent Work!"
    if g == "A-":
        return "Great Job!"
    if g == "B":
        return "Good Job!"
    if g == "B-":
        return "Ok Job!"
    if g == "C":
        return "Average"
    if g == "C-":
        return "Below Average"
    if g == "D":
        return "Unsatisfactory"
    if g == "D-":
        return "You really need to work harder!"
    if g == "F":
        return "You are failing!"




# Below is the main program, Some of it is written for you

print("CALCULATE YOUR GRADE!")
print("-"*21)


# You will need both of these variables for your function
counter = 0
total = 0

# Below this is a while loop, we will be covering these next week!
while True:
    grade = input("Please enter a grade (or q to quit): ")
    if grade.lower() == 'q':
        break # The look will stop when user enters q

    if validate_input(grade): # calling your function to validate!
        total = total + int(grade) # we should know what this does
        counter = counter + 1 # incrementing the counter, you will need this to calculate the average
    else:
        print("Please enter a valid grade!")

# This code will run once the loop breaks
# You should be able to finish the rest calling your functions!
# Depending on how you write your code, the rest should not be more than 6 lines!

# PUT THE REST OF YOU CODE HERE THAT PRODUCES THE OUTPUT!
ca = calculate_avg(total,counter)
w = get_letter_grade(ca)
get_message(w)

print("Your Average: {}".format(ca))
print("Your Letter Grade: {}".format(w))
print(get_message(w))

'''
Questions:

What is the benefit for using functions? Do you think they make your code easier to read?
Functions do make code easier to read. It makes all the code much more organized. Its much easier to just call a function than
to have to search for random code in a specific file.

Next week we will be covering loops, in your own words can you give me an ideas of why we use a loop?
Loops allow a specific task to keep happening until someone tells it to stop. This can be very useful 
when creating large programs that may need to solve several things at once or when you dont know how many 
times the user needs to enter something.

Why can we use the validate input function in an *if* statement? 
We can use it in a if statement because it a boolean function that returns true or false.

'''


