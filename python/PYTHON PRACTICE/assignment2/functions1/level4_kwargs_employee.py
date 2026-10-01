def show_employee(**employee):
    for key, value in employee.items():
        print(key, ":", value)


show_employee(name="Alex", role="Developer", department="IT")
