class employee:
    def __init__(e,n,s,a):
        e.name = n
        e.salary = s
        e.age = a
        e.company = "LPU"
    def show(e):
        print(e.name)
        print(e.salary)
        print(e.age)
        print(e.company)
e1 = employee("Pushkar", 100000, 28)
e2 = employee("Kunal", 100000, 29)
e2.company="Angreno os"
e1.show()
e2.show()