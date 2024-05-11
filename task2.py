def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0 

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        # Якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # Якщо x менше за значення посередині списку, ігноруємо праву половину    
        elif arr[mid] > x:
            high = mid - 1

        # Якщо знайдено точне значення
        else:
            return (iterations, arr[mid]) 

    # Якщо елемент не знайдено, повертаємо найближчий більший елемент або None
    if low < len(arr):
        return (iterations, arr[low])
    else:
        return (iterations, None)

# Тестування
arr = [2.5, 3.4, 4.1, 10.2, 40.2]
x = 32.3
result = binary_search(arr, x)
print(f"{result}")
