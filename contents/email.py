def create_user_name():
    from faker import Faker
    fake = Faker()
    username = fake.user_name() + "@" + fake.user_name() + "." + fake.user_name()
    return username


print("Tên người dùng ngẫu nhiên:", create_user_name())
