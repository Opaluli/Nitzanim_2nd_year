def question_1(matrix):
    total_sum = sum(sum(row) for row in matrix)
    print(f"שאלה 1: סכום כל הערכים במטריצה הוא {total_sum}")

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
    path = []
    row, col = 0, 0
    while row < len(matrix) and col < len(matrix[0]):
        path.append((row, col))
        row += 1
        col += 1
    print("שאלה 3: המסלול דרך אינדקסי המטריצה:", path)

def question_4(matrix):
    problem_pixels = [(i, j) for i, row in enumerate(matrix) for j, pixel in enumerate(row) if pixel != "work"]
    print("שאלה 4: אינדקסים של פיקסלים בעייתיים:", problem_pixels)

def question_5(matrix):
    hit_count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'X':
                print(f"פגיעה בז ({row + 1}, {col + 1})")
                hit_count += 1
    print(f"סה\"כ פגיעות נדרשות: {hit_count}")

def question_6():
    inventory = []
    while True:
        item = input("הכנס שם מוצר או 'done' כדי לסיים: ")
        if item == "done":
            break
        stock_status = input(f"האם '{item}' במלאי? (Yes/No): ")
        inventory.append((item, stock_status))
    for item, status in inventory:
        print(f"המוצר {item} {'במלאי' if status == 'Yes' else 'לא במלאי'}.")

def main():
    matrix_1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    question_1(matrix_1)
    question_2()
    matrix_3 = [["O", "O", "O", "O", "X"], ["O", "O", "X", "O", "O"], ["O", "X", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["X", "O", "O", "O", "O"]]
    question_3(matrix_3)
    matrix_4 = [["work", "work", "problem", "work", "work"], ["work", "problem", "work", "work", "work"], ["work", "work", "work", "problem", "work"], ["problem", "work", "work", "work", "problem"], ["work", "work", "work", "work", "work"]]
    question_4(matrix_4)
    matrix_5 = [["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["X", "O", "O", "O", "O"], ["X", "O", "O", "O", "O"], ["X", "O", "O", "O", "O"]]
    question_5(matrix_5)
    question_6()

main()
