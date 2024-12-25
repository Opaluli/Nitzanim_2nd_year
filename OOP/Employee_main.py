from Employee import *


def main():
    new_employee = Employee("Opal", 2008, 69934)
    print(str(new_employee.get_age()))
    print(new_employee.do_work())


if __name__ == '__main__':
    main()
