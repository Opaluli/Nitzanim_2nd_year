class Employee:
    def __init__(self, name, year_of_birth, salary):
        self.name = name
        self.year_of_birth = year_of_birth
        self.salary = salary

    def get_age(self):
        return 2024 - self.year_of_birth

    def do_work(self):
        print(f"{self.name} is working!")
