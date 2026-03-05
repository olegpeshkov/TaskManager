from task import Task

def main():
    """Главная функция для тестирования класса Task"""
    print("=== СОЗДАНИЕ ЗАДАЧ ===\n")

    # Создаём несколько задач
    task1 = Task(
        "Купить продукты",
        "Молоко, хлеб, яйца, сыр",
        "высокий"
    )
    task2 = Task(
        "Сделать домашнее задание",
        "Решить задачи по математике",
        "средний"
    )
    task3 = Task(
        "Позвонить родителям",
        priority="низкий"
    )

    # Выводим краткую информацию
    print("Краткая информация:")
    print(task1)
    print(task2)
    print(task3)

    print("\n=== ТЕСТИРОВАНИЕ МЕТОДОВ ===\n")

    # Изменяем приоритет
    print(f"Старый приоритет task1: {task1.priority}")
    task1.priority = "средний"
    print(f"Новый приоритет task1: {task1.priority}")

    # Изменяем описание
    print(f"\nСтарое описание task1: {task1.description}")
    task1.description = "Новый список: молоко, хлеб, масло"
    print(f"Новое описание task1: {task1.description}")

    # Отмечаем задачу выполненной
    print("\n--- Отметка о выполнении ---")
    task2.mark_completed()
    task2.mark_completed()  # попытка отметить повторно

    # Проверка дат
    print(f"\nДата создания task2: {task2.created_at.strftime('%d.%m.%Y %H:%M:%S')}")
    if task2.completed_at:
        print(f"Дата выполнения task2: {task2.completed_at.strftime('%d.%m.%Y %H:%M:%S')}")

    # Проверяем, что повторная отметка не меняет дату выполнения
    first_completed = task2.completed_at
    task2.mark_completed()  # ещё раз
    if task2.completed_at == first_completed:
        print("Повторный вызов не изменил дату выполнения (OK)")
    else:
        print("Ошибка: дата выполнения изменилась!")

    print("\n=== ПОЛНАЯ ИНФОРМАЦИЯ ===\n")
    print(task1.get_info())
    print("\n" + "=" * 40 + "\n")
    print(task2.get_info())

    print("\n=== ПРОВЕРКА ВАЛИДАЦИИ ===\n")

    # Некорректный приоритет
    try:
        task3.priority = "очень высокий"
    except ValueError as e:
        print(f"Ошибка при смене приоритета: {e}")

    # Пустое название
    try:
        task3.title = ""
    except ValueError as e:
        print(f"Ошибка при смене названия: {e}")

if __name__ == "__main__":
    main()