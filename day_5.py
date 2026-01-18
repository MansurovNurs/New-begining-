


def show_element(iterable):
    length = len(iterable)
    print(f"Работаем с объектом: {iterable}")
    print(f"Допустимые индексы: от 0 до {length - 1}")
    print("Для выхода введите: exit")

    while True:
        user_input = input("Введите индекс: ")

        if user_input.lower() == "exit":
            print("Выход из программы.")
            break


        try:
            index = int(user_input)
            print("Элемент:", iterable[index])

        except ValueError:
            print("Ошибка! Нужно ввести целое число.")

        except IndexError:
            print(f"Ошибка! Введите индекс от 0 до {length - 1}")
        return show_element(iterable)
e = show_element([4, 3, 4, 5, 6, 5])


