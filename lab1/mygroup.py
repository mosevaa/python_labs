

groupmates = [
     {
     "name": "Александр",
     "surname": "Иванов",
     "exams": ["Информатика", "ЭЭиС", "Web"],
     "marks": [4, 3, 5]
     },
     {
     "name": "Иван",
     "surname": "Петров",
     "exams": ["История", "АиГ", "КТП"],
     "marks": [4, 4, 4]
     },
     {
     "name": "Кирилл",
     "surname": "Смирнов",
     "exams": ["Философия", "ИС", "КТП"],
     "marks": [5, 5, 5]
     }
    ]

def print_students(students, need):
   print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
   for student in students:
       sred = sum(student["marks"])/len(student["marks"])
       if sred > need:
           print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates, 3.9)
