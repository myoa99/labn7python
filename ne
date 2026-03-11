import math

def compute_z1(alpha, beta):
    """Вычисляет z1 по формуле: (cos α - cos β) - (sin α - sin β)^2"""
    part1 = math.cos(alpha) - math.cos(beta)
    part2 = (math.sin(alpha) - math.sin(beta)) ** 2
    return part1 - part2

def compute_z2(alpha, beta):
    """Вычисляет z2 по формуле: -4 * sin^2((α - β)/2) * (cos α - cos β)/2"""
    delta = (alpha - beta) / 2
    sin_delta = math.sin(delta)
    numerator = math.cos(alpha) - math.cos(beta)
    return -4 * (sin_delta ** 2) * (numerator / 2)

def main():
    # Конкретные значения углов
    alpha = 0.5  # радианы
    beta = 1.0   # радианы

    z1 = compute_z1(alpha, beta)
    z2 = compute_z2(alpha, beta)

    print(f"Для α = {alpha}, β = {beta}:")
    print(f"z1 = {z1:.10f}")
    print(f"z2 = {z2:.10f}")

if __name__ == "__main__":
    main()
