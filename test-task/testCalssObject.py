# class vs object
class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    @staticmethod
    def print_me():
        print(f'somethinh')

    def employee_info(self):
        print(f'Name {self.name}, {self.salary}')
        self.print_me()

print(Employee)

alice = Employee('Alice', 1000)
alice.employee_info()
print(alice)


bob  = Employee('Bob', 2000)
bob.employee_info()
bob.salary = 3000
print(bob.salary, bob.name)
print(bob)


# alice_2 = Employee('Alice2', 1900)
# print(alice_2)
#
# print(id(alice), id(alice_2))