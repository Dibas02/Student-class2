class Student:
    grade = '7'

    def __init__(self, name, id, city):
        self.name = name
        self.id = id
        self.city = city

dibas = Student("Dibas", "02", "Sylhet")
pranjol = Student("Pranjol", '03', 'Cumilla')
shaan = Student("Shaan", '05', 'Dhaka')

print("1st Student's name is ", dibas.name, 'his id is ', dibas.id, 'his city is ', dibas.city)
print("2nd Student's name is ", pranjol.name, 'his id is ', pranjol.id, 'his city is ', pranjol.city)
print("3rd Student's name is ", shaan.name, 'his id is ', shaan.id, 'his city is ', shaan.city)

        