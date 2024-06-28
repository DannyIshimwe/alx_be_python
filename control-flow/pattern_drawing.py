def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            raise ValueError("The number must be positive.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()
        row += 1
if __name__ == "__main__":
    main()
