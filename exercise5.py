# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {'name': 'Jose', 'school': 'Milton', 'grades': (66,77,88)}
students = [
              {'name': 'Jose', 'school': 'Milton', 'grades': (66,77,88)}, 
              {'name': 'Richard', 'school': 'Latin', 'grades': (74,81,93)}, 
              {'name': 'Tim', 'school': 'Prep', 'grades': (85,96,100)}
             ]

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(**data):
    grades = data['grades']
        
    return sum(grades) / len(grades)

# Implement the function below
# Given a list of students (dictionaries), calculate the average grade of the class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])

    return total / count

  
def main():
    grades_average = average_grade(**student)
    print("Grades average = {}".format(grades_average))
    
    average_grade_all = average_grade_all_students(students)
    print("Average grade all = {}".format(average_grade_all))

if __name__ == "__main__":
    main()
