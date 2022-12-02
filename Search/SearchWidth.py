"""
Алгоритм 'Поиск в ширину' работает с графами.
Он помогает ответить на вопросы двух типов:
    тип 1: существует ли путь от узла А к узлу В?
    тип 2: как выглядит кратчайший путь от узла А к узлу В?


Реализация:
    1. Создать очередь с проверяемыми элементами
    Цикл:
        2. Извлечь из очереди очередной элемент
        3. Проверить является ли элемент искомым
        4.A. Если да, то завершить
        4.B. Если нет, то добавить все элементы этого элемента в очередь
    5. Если очередь пуста - нет того, что искали.
"""

from collections import deque  # двусторонняя очередь

graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(person):
    pass


def search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # Этот массив испопьзуется дпя отспеживания уже проверенных пюдей
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:  # Человек проверяется топько в том спучае, еспи он не проверяпся ранее
            if person_is_seller(person):
                print(person + "is а mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)  # Человек помечается как уже проверенный
    return False


search(graph, "you")
