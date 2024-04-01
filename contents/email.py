# import random

# def generate_random_email():
#     # Tách phần đầu của email từ tên
#     # email_prefix = name.lower().replace(" ", "") + str(random.randint(100, 999))

#     # Tách phần cuối của email từ ngày tháng năm sinh

#     # Tạo email hoàn chỉnh
#     email = "email_prefix" + "@" +  "gmail" + ".com"
#     return email

# random_email = generate_random_email()
# print("Email ngẫu nhiên của bạn là:", random_email)
import random
import string

def generate_random_email():
    # Tạo một danh sách các từ khóa và phụ họa
    keywords = ["hello", "world", "python", "programming", "code", "email", "random", "generator"]
    suffixes = ["com", "net", "org", "info", "io"]

    # Chọn một từ khóa và một phụ họa ngẫu nhiên
    keyword = random.choice(keywords)
    suffix = random.choice(suffixes)

    # Tạo một phần đuôi email ngẫu nhiên
    random_digits = ''.join(random.choices(string.digits, k=3))

    # Tạo email hoàn chỉnh
    email = keyword + random_digits + "@" + suffix
    return email

# Tạo email ngẫu nhiên
random_email = generate_random_email()
print("Email ngẫu nhiên là:", random_email)
