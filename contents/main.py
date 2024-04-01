import requests
import datetime
from time import sleep


url_register = 'https://acenetwork.online/api/v1/passport/auth/register'
url_login = 'https://acenetwork.online/api/v1/passport/auth/login'
url_order = 'https://acenetwork.online/api/v1/user/order/save'
url_checkout = 'https://acenetwork.online/api/v1/user/order/checkout'







for i in range(2):
    #! Tạo acc
    acc = datetime.datetime.now()
    acc = acc.strftime("%Y_%m_%d_%H_%M_%S_%f")
    acc = f'{acc}@gmail.com'

    #! Đăng ký
    data = {'email': f'{acc}', 'password': f'{acc}'}

    response = requests.post(url_register, data=data)
    if response.status_code == 200:
        print("Đăng ký thành công!")
    else:
        print("Đăng ký thất bại. Mã lỗi:", response.status_code)
        exit()

    #! Đặt hàng
    response_data = response.json()
    auth_data = response_data['data']['auth_data']
    data = {"period": "onetime_price",
            "plan_id": "17",    "coupon_code": "FREE100"}
    headers = {'Authorization': auth_data}

    response = requests.post(url_order, json=data, headers=headers)
    if response.status_code == 200:
        print("Đặt hàng thành công!")
    else:
        print("Đặt hàng thất bại. Mã lỗi:", response.status_code)
        exit()

    #! Thanh toán
    response_data = response.json()
    invoice = response_data['data']
    data = {"trade_no": invoice, "method": "1"}
    headers = {'Authorization': auth_data}

    response = requests.post(url_checkout, json=data, headers=headers)
    if response.status_code == 200:
        print("Thanh toán thành công!")
    else:
        print("Thanh toán thất bại. Mã lỗi:", response.status_code)
        exit()

    #! Đăng nhập
    data = {'email': f'{acc}', 'password': f'{acc}'}

    response = requests.post(url_login, data=data)
    if response.status_code == 200:
        print("Đăng nhập thành công!")
    else:
        print("Đăng nhập thất bại. Mã lỗi:", response.status_code)
        exit()
    response_data = response.json()
    token = response_data['data']['token']

    with open("nghia.txt", "a") as file:
        file.write(acc + "\n")
        file.write(
            f"https://acenetwork.online/api/v1/client/subscribe?token={token}" + "\n")
