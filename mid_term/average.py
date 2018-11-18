def main():
    num_strings = input("Enter numbers to average: ").split()
    num_floats = [float(num) for num in num_strings]
    average = sum(num_floats) / len(num_floats)
    print(average)

if __name__ == "__main__":
    main()