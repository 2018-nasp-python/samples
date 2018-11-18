import simple_module

def main():
    values = [[2,1], [3,4], [5,6]]

    for num_pair in values:
        total = simple_module.adder(num_pair[0],  num_pair[1])
        print(total)

    simple_module.main()

if __name__ == "__main__":
    main()