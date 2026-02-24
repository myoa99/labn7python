import math

try:
    # Шаг 1: Чтение входных данных из файла
    with open('input.txt', 'r') as input_file:
        alpha = float(input_file.readline().strip())
        beta = float(input_file.readline().strip())

    # Шаг 2: Вычисления
    z1 = (math.cos(alpha) - math.cos(beta)) ** 2 - (math.sin(alpha) - math.sin(beta)) ** 2
    z2 = -4 * (math.sin((alpha - beta) / 2)) ** 2 * math.cos(alpha + beta)

    # Шаг 3: Запись результатов в файл
    with open('output.txt', 'w') as output_file:
        output_file.write(f"Входные данные:\n")
        output_file.write(f"α = {alpha}\n")
        output_file.write(f"β = {beta}\n\n")
        output_file.write(f"Результаты вычислений:\n")
        output_file.write(f"z₁ = {z1:.6f}\n")
        output_file.write(f"z₂ = {z2:.6f}\n")

    print("Вычисления завершены. Результаты записаны в output.txt")

except FileNotFoundError:
    print("Ошибка: файл input.txt не найден!")
except ValueError:
    print("Ошибка: в файле input.txt содержатся некорректные данные (не числа).")
except Exception as e:
    print(f"Произошла ошибка: {e}")
