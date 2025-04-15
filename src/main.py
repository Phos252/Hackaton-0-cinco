def calculate(expression: str) -> float:
    # Dividimos la expresión en partes: ['8', '/', '2']
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Formato inválido. Usa: 'a / b'")

    a, op, b = parts
    a = float(a)
    b = float(b)

    if(op == "/"):
         division(a,b)

    if(op == "+"):
         suma(a,b)

    if(op == "-"):
         resta(a,b)

    if(op == "*"):
         suma(a,b)

    if(op == "^"):
         suma(a,b)
         
    pass

def division(a,b):
    if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

def suma(a,b):
    print("suma")


def resta(a,b):
    print("suma")

def suma(a,b):
    print("suma")


def multiplicacion(a,b):
    print("suma")


def potencia(a,b):
    print("suma")