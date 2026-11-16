def convertir_romano_a_decimal(num_romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(num_romano) == 1:
        return valores[num_romano]
    else:
        if valores[num_romano[0]] < valores[num_romano[1]]:
            return -valores[num_romano[0]] + convertir_romano_a_decimal(num_romano[1:])
        else:
            return valores[num_romano[0]] + convertir_romano_a_decimal(num_romano[1:])

print(convertir_romano_a_decimal(num_romano))