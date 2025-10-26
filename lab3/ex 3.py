def read_example_file(method: str = "all"):
    """
    Параметры:
        - "all"           -> прочитать весь файл сразу
        - "line_by_line"  -> построчное чтение через цикл
    """
    try:
        with open("lab3/example.txt", "r") as file:
            if method == "all":
                content = file.read()
                print(f"Весь файл целиком:\n{content}")

            elif method == "line_by_line":
                for line in file:
                    print(line)
    except FileNotFoundError:
        print("Файл не найден.") 
      
read_example_file("all")