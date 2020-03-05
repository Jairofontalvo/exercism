class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade

    def roster(self):
        return list(self.students.keys())

    def grade(self, grade_number):
        return [name for name, grade in self.students.items() if grade == grade_number]
