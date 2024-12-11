def targil1():
    list2 = {1, 2, 3, 1, 2, 3}
    list1 = {1, 3, 3, 2, 1, 2}
    print(list2 == list1)
    return


def targil2():
    groups = set()
    for i in range(10):
        year = int(input(" כמה שנים אתה בצופים? "))
        groups.add(year)

    print(len(groups))

def targil3():
    tup = (13,20,"banana", "those who know","sigma","banana","banana")
    tup1 = ("hi","higgers")
    print(len(tup))
    print(tup[2])
    tup1 = tup[0:3]
    print(tup1)
    l1 = list(tup)
    l1.pop(3)
    tup = tuple(l1)
    print(tup)
    l2 = list(tup) + list(tup1)
    print(l2)
    print(tup.count("banana"))
    print(tup.index("banana"))






def phonebook():
    phone_book = dict()
    while True:
        answer = input("add or remove? exit to stop - ")
        if answer != "add" and answer != "remove" and answer != "exit":
            continue
        if answer == "exit":
            print(phone_book)
            break
        elif answer == "add":
            name = input("enter name - ")
            phone = int(input("enter phone - "))
            phone_book[name] = phone

        elif answer == "remove":
            while True:
                name = input("enter name - ")
                if name in phone_book:
                    phone_book.pop(name)
                    break
                else:
                    continue




while True:
    ans = input("what to run? 1/2/3/phonebook exit to stop - ")
    if ans == "1":
        targil1()
    elif ans == "2":
        targil2()
    elif ans == 3:
        targil3()
    elif ans == "phonebook":
        phonebook()
    elif ans == "exit":
        break

