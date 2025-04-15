def calculate(expression: str) -> float:
    # Dividimos la expresión en partes: ['8', '/', '2']
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Formato inválido. Usa: 'a / b'")

    a, op, b = parts
    a = float(a)
    b = float(b)

    if op == '/':
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return a / b
    else:
        raise ValueError(f"Operador no soportado: {op}")
