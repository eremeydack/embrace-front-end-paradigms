
def generate_random_data():
    random_string = 'Yet or record administration.'
    random_number = 7

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Yet or record administration.")
        print(f"Random Number: 7")

if __name__ == "__main__":
    main()
