from faker import Faker

fake = Faker()

def get_random_user_details():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }


if __name__ == "__main__":
    print(get_random_user_details())
