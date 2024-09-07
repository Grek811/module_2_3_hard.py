def generate_password(n):
    if n < 3 or n > 20:
        return "Число должно быть в диапазоне от 3 до 20."
    pairs = []
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))
    for pair in pairs:
        pair_sum = sum(pair)
        if n % pair_sum == 0:
            result += f"{pair[0]}{pair[1]}"
    return result
n = int(input("Введите число от 3 до 20: "))
password = generate_password(n)
print(f"Нужный пароль для числа {n}: {password}")