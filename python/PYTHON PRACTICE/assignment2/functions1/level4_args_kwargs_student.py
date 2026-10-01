def show_student(*details, **marks):
    print("Student details:")
    for detail in details:
        print(detail)

    print("Student marks:")
    for subject, mark in marks.items():
        print(subject, ":", mark)


show_student("Alex", 18, math=90, science=85)
