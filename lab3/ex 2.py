def append_to_file(text: str):
    with open("lab3/example.txt", "a") as file:
        file.write("\n" + text)
    print("Текст добавлен в файл example.txt")
    
append_to_file(input("Введите текст для добавления: "))