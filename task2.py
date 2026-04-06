orders = [
    (101, "Python для начинающих"),
    (101, "Алгоритмы и структуры данных"),
    (102, "Чистый код"),
    (101, "Python для начинающих"),
    (103, "Искусство программирования"),
    (102, "Python для начинающих"),
    (103, "Чистый код"),
    (101, "Грокаем алгоритмы"),
    (102, "Грокаем алгоритмы"),
    (103, "Алгоритмы и структуры данных"),
    (102, "Чистый код"),
    (104, "Python для начинающих")
]

# формируем словарь
def getUserBooksDict(orders):
    user_books = dict()
    for user_id, book in orders:
        if user_id not in user_books:
            user_books[user_id] = set()
        user_books[user_id].add(book)
    return user_books

user_books = getUserBooksDict(orders)
print(user_books)

# считаем сколько каждый юзер купил
def getBooksCount(user_id):
    return len(user_books[user_id])

# ищем кто больше всего купил уникальных книг
def getTopUser(user_books):
   return max(user_books, key=getBooksCount)

top_user = getTopUser(user_books)
print(top_user)
