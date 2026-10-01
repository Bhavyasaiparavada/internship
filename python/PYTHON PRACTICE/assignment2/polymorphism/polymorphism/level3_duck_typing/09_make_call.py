class AndroidPhone:
    def call(self):
        print("Android phone is calling")


class IPhone:
    def call(self):
        print("iPhone is calling")


def make_call(phone):
    phone.call()


make_call(AndroidPhone())
make_call(IPhone())