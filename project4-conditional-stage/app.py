def greet(name):
    if not isinstance(name, str):
        raise TypeError("name must be a string")

    name = name.strip()

    if not name:
        raise ValueError("name cannot be empty")

    return f"Hello, {name}"


if __name__ == "__main__":
    print(greet("Student"))