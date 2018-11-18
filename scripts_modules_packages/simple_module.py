def adder(val1, val2):
    return int(val1)+ int(val2)

def main():
    print(__name__)
    val1, val2 = input("Please enter 2 values: ").split()
    print("The sum is {}".format(adder(val1, val2)))

if __name__ == "__main__":
    main()


