import random

def find_min_max(arr, left=None, right=None):
    """
    Знаходить мінімальний та максимальний елемент у масиві за допомогою стратегії "розділяй і володарюй".
    
    Args:
        arr: Масив чисел
        left: Лівий індекс (опційно)
        right: Правий індекс (опційно)
        
    Returns:
        Кортеж (мінімум, максимум)
    """
    # Встановлюємо початкові значення left і right, якщо вони не передані
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    # Базовий випадок: якщо один елемент
    if left == right:
        return arr[left], arr[left]
    
    # Базовий випадок: якщо два елементи
    if right - left == 1:
        return min(arr[left], arr[right]), max(arr[left], arr[right])
    
    # Знаходимо середину масиву
    mid = (left + right) // 2
    
    # Рекурсивно знаходимо мінімум і максимум у лівій та правій половинах
    min_left, max_left = find_min_max(arr, left, mid)
    min_right, max_right = find_min_max(arr, mid + 1, right)
    
    # Об'єднуємо результати
    return min(min_left, min_right), max(max_left, max_right)


def test_algorithms():
    # Тестові масиви
    test_arrays = [
        [1, 5, 3, 8, 2, 9, 4],
        [100, 54, 78, 23, 11, 9, 45, 37],
        [5],
        [7, 2],
    ]
    
    print("Тестування пошуку мінімуму та максимуму:")
    for i, arr in enumerate(test_arrays):
        min_val, max_val = find_min_max(arr)
        print(f"Масив {i+1}: {arr}")
        print(f"Мінімум: {min_val}, Максимум: {max_val}")
        print("Перевірка:", min(arr) == min_val and max(arr) == max_val)
        print()
    
if __name__ == "__main__":
    test_algorithms()