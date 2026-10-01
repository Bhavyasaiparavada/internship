from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def work(self):
        pass


class Developer(Employee):
    def work(self):
        return "Developer writes code."


class Tester(Employee):
    def work(self):
        return "Tester checks software."


print(Developer().work())
print(Tester().work())