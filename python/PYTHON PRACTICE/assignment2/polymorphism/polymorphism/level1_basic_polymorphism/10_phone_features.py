class Android:
    def show_features(self):
        print("Android: customizable home screen")


class IPhone:
    def show_features(self):
        print("iPhone: Face ID")


class WindowsPhone:
    def show_features(self):
        print("Windows Phone: live tiles")


android = Android()
iphone = IPhone()
windows_phone = WindowsPhone()
android.show_features()
iphone.show_features()
windows_phone.show_features()