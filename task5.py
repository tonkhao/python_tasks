employees = [
    {"name": "Анна Смирнова", "department": "IT", "salary": 120000, "age": 28, "experience": 5},
    {"name": "Иван Петров", "department": "Sales", "salary": 95000, "age": 35, "experience": 10},
    {"name": "Мария Иванова", "department": "HR", "salary": 85000, "age": 42, "experience": 15},
    {"name": "Дмитрий Сидоров", "department": "IT", "salary": 150000, "age": 31, "experience": 7},
    {"name": "Елена Козлова", "department": "Sales", "salary": 110000, "age": 29, "experience": 6},
    {"name": "Сергей Михайлов", "department": "IT", "salary": 90000, "age": 24, "experience": 2},
    {"name": "Ольга Новикова", "department": "HR", "salary": 95000, "age": 38, "experience": 12},
    {"name": "Алексей Федоров", "department": "Sales", "salary": 130000, "age": 33, "experience": 8},
    {"name": "Татьяна Морозова", "department": "IT", "salary": 140000, "age": 36, "experience": 9},
    {"name": "Константин Васильев", "department": "Sales", "salary": 88000, "age": 26, "experience": 3},
    {"name": "Наталья Павлова", "department": "HR", "salary": 105000, "age": 45, "experience": 18},
    {"name": "Максим Соколов", "department": "IT", "salary": 160000, "age": 29, "experience": 6}
]

def getAge(employee):
    return employee["age"]

def getSalary(employee):
    return employee["salary"]

def sortSalaryMaxToMin(employees):
    return sorted(employees, key=getSalary)

def sortAgeMinToMax(employees):
    return sorted(employees, key=getAge)

sortedBySalary = sortSalaryMaxToMin(employees)
sortedByAge = sortAgeMinToMax(employees)
print(sortedBySalary)
print(sortedByAge)