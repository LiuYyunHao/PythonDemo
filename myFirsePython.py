#!/usr/bin/python3

"""
def save_books():
    books = []
    book_id = input("请输入编号,以空格分隔")

    book_name = input("请输入书名,以空格分隔")
    book_number = input("请输入编号,以空格分隔")
    id_list = book_id.split(" ")
    name_list = book_name.split(" ")
    number_list = book_number.split(" ")

    input_book = list(zip(id_list, name_list, number_list))
    for book in input_book:
        dic = {"编号": book[0], "书名": book[1], "位置": book[2]}
        books.append(dic)
        pass

    enumerate_list = enumerate(input_book)
    for index, item in enumerate_list:
        print(index, item)
        pass


save_books()
"""


def sum_range(start, end):
    return sum(range(start, end + 1))


print(sum_range(20, 30))
print(sum_range(35, 45))

li = [1, 3, 4, 3, 3, 5, 2, 4, 2, 5, 2, 1, 6]
for x in li:
    if li.count(x) == 1:
        print(x)
        break
