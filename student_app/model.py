class Student:
    FILE = "data.txt"

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def save(self):
        with open(self.FILE, "a") as f:
            f.write(f"{self.name},{self.roll},{self.marks}\n")

    @classmethod
    def view_all(cls):
        try:
            with open(cls.FILE, "r") as f:
                data = f.readlines()
                if not data:
                    print("No records found.")
                for line in data:
                    name, roll, marks = line.strip().split(",")
                    print(f"Name: {name} | Roll: {roll} | Marks: {marks}")
        except FileNotFoundError:
            print("File not found.")

    @classmethod
    def search(cls, roll):
        found = False
        with open(cls.FILE, "r") as f:
            for line in f:
                name, r, marks = line.strip().split(",")
                if r == roll:
                    print("Student Found:")
                    print(f"Name: {name}, Roll: {r}, Marks: {marks}")
                    found = True
                    break
        if not found:
            print("Student not found.")