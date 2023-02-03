class Person:
    """The class that describes persons."""

    name = 'n'
    age = 0
    eye_color = 'blue'
    nationality = 'Polish'
    sex = 'W'

    def get_name(self):
        return self.name

    def get_eye_color(self):
        return self.eye_color


d = Person()
d.name = 'Adam'
d.eye_color = 'Green'

print(d.get_name())
print(d.get_eye_color())

d2 = Person()
d2.name = 'Ewa'
d2.eye_color = 'Brown'
print(d2.get_name())
print(d2.get_eye_color())
