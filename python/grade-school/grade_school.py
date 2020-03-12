class School:
    def __init__(self):
        self.estudiantes = []

    def add_student(self, name, grade):
        self.estudiantes.append((grade, name))

    def roster(self):
        return [x[1] for x in sorted(self.estudiantes)]

    def grade(self, grade_number):
        return [x[1] for x in sorted(self.estudiantes) if x[0] == grade_number]
