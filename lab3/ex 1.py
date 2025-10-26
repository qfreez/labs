def read_example_file(method: str = "all"):
    """
    Параметры:
        - "all"           -> прочитать весь файл сразу
        - "line_by_line"  -> построчное чтение через цикл
    """
    with open("lab3/example.txt", "r") as file:
        if method == "all":
            content = file.read()
            print(f"Весь файл целиком:\n{content}")

        elif method == "line_by_line":
            for line in file:
                print(line)

        
read_example_file("all")