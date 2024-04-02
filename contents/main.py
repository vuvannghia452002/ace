import random
import string
import requests


def generate_random_text(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def create_user_name():
    username = generate_random_text(5)
    username += "@"
    username += generate_random_text(5)
    username += "."
    username += generate_random_text(5)

    return username


def register(username):
    print("Đăng ký:", end=" ")

    data = {
        'email': f'{username}',
        'password': f'{username}'
    }

    response = requests.post(
        'https://acenetwork.online/api/v1/passport/auth/register',
        data=data
    )

    if response.status_code == 200:
        print("Đăng ký thành công!")
        response_data = response.json()
        auth_data = response_data['data']['auth_data']
        return auth_data
    else:
        print("Đăng ký thất bại. Mã lỗi:", response.status_code)
        exit()


def order(auth):
    print("Đặt hàng:", end=" ")

    headers = {'Authorization': auth}

    data = {
        "period": "onetime_price",
        "plan_id": "17",
        "coupon_code": "FREE100"
    }

    response = requests.post(
        'https://acenetwork.online/api/v1/user/order/save',
        json=data,
        headers=headers
    )

    if response.status_code == 200:
        print("Đặt hàng thành công!")
        response_data = response.json()
        invoice = response_data['data']
        return invoice
    else:
        print("Đặt hàng thất bại. Mã lỗi:", response.status_code)
        exit()


def pay(auth, invoice):
    print("Thanh toán:", end=" ")

    headers = {'Authorization': auth}

    data = {
        "trade_no": invoice,
        "method": "1"
    }

    response = requests.post(
        'https://acenetwork.online/api/v1/user/order/checkout',
        json=data,
        headers=headers
    )

    if response.status_code == 200:
        print("Thanh toán thành công!")
    else:
        print("Thanh toán thất bại. Mã lỗi:", response.status_code)
        exit()


def log_in(username):
    print("Đăng nhập:", end=" ")

    data = {
        'email': f'{username}',
        'password': f'{username}'
    }

    response = requests.post(
        'https://acenetwork.online/api/v1/passport/auth/login',
        data=data
    )

    if response.status_code == 200:
        print("Đăng nhập thành công!")
        response_data = response.json()
        token = response_data['data']['token']
        return token
    else:
        print("Đăng nhập thất bại. Mã lỗi:", response.status_code)
        exit()

def save_token(username,token):
    print("Lưu token:", end=" ")
    with open("nghia.txt", "a") as file:
        file.write(username + "\n")
        file.write(
            f"https://acenetwork.online/api/v1/client/subscribe?token={token}" + "\n")
    print("Lưu token thành công!")


def main():
    try:
        username = create_user_name()
        auth = register(username)
        invoice = order(auth)
        pay(auth, invoice)
        token = log_in(username)
        save_token(username,token)
    except Exception as e:
        print("Đã xảy ra một lỗi:", e)


if __name__ == "__main__":
    main()
