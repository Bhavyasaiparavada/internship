class Developer:
    def work(self):
        print("Developer writes code")


class Tester:
    def work(self):
        print("Tester checks the program")


def assign_work(employee):
    employee.work()


assign_work(Developer())
assign_work(Tester())