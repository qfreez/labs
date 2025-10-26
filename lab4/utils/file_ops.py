def create_file(filename: str):
    """Создаёт пустой файл с указанным именем."""
    try:
        with open(filename, "x"):
            pass
    except FileExistsError:
        print(f"Файл '{filename}' уже существует.")