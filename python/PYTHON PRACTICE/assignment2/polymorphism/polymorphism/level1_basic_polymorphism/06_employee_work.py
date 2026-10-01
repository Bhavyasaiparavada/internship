class Developer:
    def work(self):
        print("Developer writes code")


class Tester:
    def work(self):
        print("Tester checks the software")


class Manager:
    def work(self):
        print("Manager plans the project")


developer = Developer()
tester = Tester()
manager = Manager()
developer.work()
tester.work()
manager.work()