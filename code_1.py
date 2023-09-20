
def generate_random_data():
    random_string = 'Relate leader production really.'
    random_number = 21

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Relate leader production really.")
        print(f"Random Number: 21")

if __name__ == "__main__":
    main()
