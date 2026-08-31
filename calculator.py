OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def calculate(a: float, op: str, b: float) -> float:
    if op not in OPERATIONS:
        raise ValueError(f"Unknown operation: {op}")
    if op == "/" and b == 0:
        raise ZeroDivisionError("Division by zero")
    return OPERATIONS[op](a, b)


def main() -> None:
    print("Simple calculator. Operations: + - * /. Type 'q' to quit.")
    while True:
        expr = input("Enter expression (e.g. 3 + 4): ").strip()
        if expr.lower() == "q":
            break
        parts = expr.split()
        if len(parts) != 3:
            print("Invalid format. Use: <number> <op> <number>")
            continue
        a_str, op, b_str = parts
        try:
            a, b = float(a_str), float(b_str)
            result = calculate(a, op, b)
            print(f"= {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
