def calculate(expression: str) -> float:
    try:
        allowed_operators = {"**"}
        if any(op not in expression for op in allowed_operators):
            raise ValueError("Solo se permite la operación de potencia (**).")

        result = eval(expression, {"__builtins__": None}, {})
        return float(result)
    except Exception as e:
        print(f"Error: {e}")
        return 0.0
    pass