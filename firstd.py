def question_1(matrix):
    total_sum = 0
    for row in matrix:
        for value in row:
            total_sum += value
    print("שאלה 1: סכום כל הערכים במטריצה הוא", total_sum)

def question_2():
    guests = [
        ["סטטיק", "נועה קירל", "סטפן לוגר"],
        ["פדי", "מיטל"],
        ["דני", "דנה", "עומר"]
    ]
    print("שאלה 2: רשימת המוזמנים -", guests)
    guests[0].remove("נועה קירל")
    guests[1].append("יובל")
    print("רשימת המוזמנים המעודכנת:", guests)


def question_3(matrix):
    rows, cols = len(matrix), len(matrix[0])
    path = []
    step = 1


    def find_path(x, y):

        if x == rows - 1 and y == cols - 1:
            path.append((x, y))
            return True

        if 0 <= x < rows and 0 <= y < cols and matrix[x][y] == "O":
            path.append((x, y))
            matrix[x][y] = "X"

            if find_path(x + 1, y) or find_path(x, y + 1):
                return True

            path.pop()
            matrix[x][y] = "O"

        return False

    if find_path(0, 0):
        for x, y in path:
            print(f"{step}) ({x}, {y})")
            step += 1
    else:
        print("No path found")

def question_4(matrix):
    problem_pixels = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "problem":
                problem_pixels.append((i, j))
    print("שאלה 4: אינדקסים של פיקסלים בעייתיים:", problem_pixels)


def question_5(matrix):
    hit_count = 0
    while hit_count < 3:
        print(f"נשארו {3 - hit_count} פגיעות")
        row = int(input("הכנס את השורה שבה תרצה לפגוע (1-5): ")) - 1
        col = int(input("הכנס את העמודה שבה תרצה לפגוע (1-5): ")) - 1
        if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]):
            if matrix[row][col] == 'X':
                print(f"פגיעה מוצלחת ב({row + 1}, {col + 1})!")
                hit_count += 1
                matrix[row][col] = "O"  # עדכון המטריצה לפגיעה
            else:
                print("לא פגעת בצוללת.")
        else:
            print("המיקום שהוזן אינו תקין.")

    print("סה\"כ פגיעות נדרשות הושגו!")


def question_6():
    inventory = []
    while True:
        item = input("הכנס שם מוצר או 'done' כדי לסיים: ")
        if item == "done":
            break
        stock_status = input("האם '" + item + "' במלאי? (Yes/No): ")
        inventory.append((item, stock_status))
    for item, status in inventory:
        if status == 'Yes':
            print("המוצר", item, "במלאי")
        else:
            print("המוצר", item, "לא במלאי")

def main():
    matrix_1 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    question_1(matrix_1)
    question_2()
    matrix_3 = [
        ["O", "O", "X", "X", "X"],
        ["X", "O", "X", "X", "X"],
        ["X", "O", "O", "O", "X"],
        ["X", "X", "X", "O", "X"],
        ["X", "X", "X", "O", "O"]
    ]

    question_3(matrix_3)
    matrix_4 = [
        ["work", "work", "problem", "work", "work"],
        ["work", "problem", "work", "work", "work"],
        ["work", "work", "work", "problem", "work"],
        ["problem", "work", "work", "work", "problem"],
        ["work", "work", "work", "work", "work"]
    ]
    question_4(matrix_4)
    matrix_5 = [
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["X", "O", "O", "O", "O"],
        ["X", "O", "O", "O", "O"],
        ["X", "O", "O", "O", "O"]
    ]
    question_5(matrix_5)
    question_6()

main()
