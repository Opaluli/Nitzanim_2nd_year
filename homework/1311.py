import math

#מבני נתונים
def practice():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print(set_a.intersection(set_b))
def question1_set():
    sets = [set(),set()]
    final_set = set()
    for i in range(0,2):
        while True:
            inp = input("enter something... DONE to stop - ")
            if inp == "DONE":
                break
            else:
                sets[i].add(inp)

    for item in sets[0]:
        if item in sets[0] and item not in sets[1]:
            final_set.add(item)
    for item in sets[1]:
        if item in sets[1] and item not in sets[0]:
            final_set.add(item)
    print(final_set)
def question2_set():
    sets = [set(),set()]
    final_set = set()
    for i in range(0,2):
        while True:
            inp = input("enter something... DONE to stop - ")
            if inp == "DONE":
                break
            else:
                sets[i].add(inp)

    for item in sets[0]:
        if item in sets[0] and item not in sets[1]:
            final_set.add(item)

    print(final_set)
def question1_tuple():
    my_tuple = (4, 5, 3, 3, 4, 7, 6)
    print(math.exp(math.fsum(math.log(x) for x in my_tuple) / len(my_tuple)))
def question2_tuple():
    coordinates = []
    for i in range(5):
        x = int(input("enter x - "))
        y = int(input("enter y - "))
        coordinates.append((x,y))
    print(coordinates)

    for i in range(len(coordinates)):
        coord = list(coordinates[i])
        coord[1] += 1
        coordinates[i] = tuple(coord)

    print(coordinates)
def question1_dict():
    dictionary = {'ABC': 37, 'XQW': 89, 'POZ': 15, 'LMN': 72, 'BGT': 53}
    dict_list = []
    for key in dictionary:
        new_tuple = (key, dictionary[key])
        dict_list.append(new_tuple)
    print(dict_list)
def question2_dict():
    dict1 = {'ABC': 37, 'XQW': 89, 'POZ': 15, 'LMN': 72, 'BGT': 53}
    dict2 = {'key_1': 13.24, 'key_2': 48.67, 'key_3': 22.91, 'key_4': 5.33, 'key_5': 37.18}
    new_dict = dict1.copy()
    new_dict.update(dict2)
    print(new_dict)
def question3_dict():
    keys = ["I", "the","who"]
    values = ["am", "one", "knocks."]
    dictionary = {}
    for i in range(3):
        dictionary[keys[i]] = values[i]
    print(dictionary)
def question4_dict():
    stars_dict = {}

    while len(stars_dict) < 7:
        num = int(input("Enter a number: "))

        if num in stars_dict:
            stars_dict[num] += '*'
        else:
            stars_dict[num] = '*' * num

    print(stars_dict)

#מילון
def add_student(grade_book):
    while True:
        name = input("Enter a new student name: ")
        if name not in grade_book:
            grades = []
            while True:
                grade_input = input("Enter a grade (or type 'STOP' to stop): ")
                if grade_input.upper() == "STOP":
                    break
                try:
                    grade = int(grade_input)
                    grades.append(grade)
                except ValueError:
                    print("Invalid grade. Please enter a number.")

            grade_book[name] = grades
            return grade_book  # Return once a student is added with grades
        else:
            print("Student already exists. Please enter a different name.")
def view_student_grades(grade_book):
    while True:
        name = input("Enter a new student name: ")
        if name in grade_book:
            print(grade_book[name])
        else:
            break

def average_class_grade(grade_book):
    average = 0
    grade_amount = 0
    for grades in grade_book.values():
        for grade in grades:
            average = average + grade
            grade_amount = grade_amount + 1
    print("The average grade in class: ", str(average/grade_amount))
def highest_grade(grade_book):
    max_grade = 0
    for grades in grade_book.values():
        for grade in grades:
            if grade > max_grade:
                max_grade = grade
    print("The highest grade in class: ", str(max_grade))

def perfect_score_students(grade_book):
    perfect_students = []
    for student, grades in grade_book.items():
        if all(grade == 100 for grade in grades):
            perfect_students.append(student)
    print(perfect_students)

def find_failed_students(grade_book):
    perfect_students = []
    for student, grades in grade_book.items():
        if any(grade < 56 for grade in grades):
            perfect_students.append(student)
    print(perfect_students)


def grade_system():
    grade_book = dict()
    while True:
        print(" - MENU - ")
        print("1. add student")
        print("2. view grades")
        print("3. view class average")
        print("4. highest grade in class")
        print("5. perfect score students")
        print("6. failed students")
        answer = input("enter a number... EXIT to stop ")

        if answer == "1":
            grade_book = add_student(grade_book)
        elif answer == "2":
            view_student_grades(grade_book)
        elif answer == "3":
            average_class_grade(grade_book)
        elif answer == "4":
            highest_grade(grade_book)
        elif answer == "5":
            perfect_score_students(grade_book)
        elif answer == "6":
            find_failed_students(grade_book)
        elif answer == "EXIT":
            break
        else:
            print("Invalid option. Please try again.")


def practice1():
    word = "banana"
    dici = {}
    for w in word:
        if w in dici:
            dici[w] = dici[w] + 1
        else:
            dici[w] = 1
    print(dici)

grade_system()