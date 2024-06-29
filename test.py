from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os
from pyfiglet import Figlet
from termcolor import colored

# Tạo đối tượng Figlet
figlet = Figlet(font='standard')

# Tạo chuỗi văn bản để in ra
text = figlet.renderText('Tool Tiktok - NĐT')

# Đóng khung văn bản ASCII art
lines = text.split('\n')
max_length = max(len(line) for line in lines)
frame = colored('┌' + '─' * (max_length + 2) + '┐', 'yellow') + '\n'
for line in lines:
    frame += colored('│ ' + line.ljust(max_length) + ' │', 'yellow') + '\n'
frame += colored('└' + '─' * (max_length + 2) + '┘', 'yellow')

# Thêm thông tin bên dưới trên cùng một dòng
info = (
    colored("Made by: Nguyễn Đình Trưng", 'red') + colored(' │ ', 'yellow') +
    colored("zalo: 0889541507", 'green') + colored(' │ ', 'yellow') +
    colored("Phiên bản: NĐT PC V0.1 ☘", 'blue')
)

# Kết hợp văn bản và thông tin
output = frame + "\n" + info

# In ra kết quả
print(output)

# Lấy đường dẫn thư mục hiện tại
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ghép đường dẫn thư mục hiện tại với tên thư mục "accounts"
accounts_dir = os.path.join(current_dir, 'accounts')

chrome_options = webdriver.ChromeOptions()

# Kiểm tra nếu thư mục "accounts" chưa tồn tại
if not os.path.exists(accounts_dir):
    # Yêu cầu người dùng nhập tên đăng nhập và mật khẩu
    print("\nVui lòng nhập tài khoản và mật khẩu để đăng nhập")
    email = input("Nhập tên đăng nhập: ")
    matkhau = input("Nhập mật khẩu: ")

    # Tạo đối tượng WebDriver
    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Mở trang và thực hiện đăng nhập
    driver.get('https://app.golike.net/login/')
    sleep(2)

    # Sử dụng By.CSS_SELECTOR
    element = driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(email)
    sleep(2)
    element = driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(matkhau)
    sleep(2)

    # Hoặc sử dụng By.XPATH
    # element = driver.find_element(By.XPATH, "//input[@type='text']").send_keys(email)
    # sleep(2)
    # element = driver.find_element(By.XPATH, "//input[@type='password']").send_keys(matkhau)
    # sleep(2)

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/form/div[3]/button")
    element.click()
    sleep(2)

    # Kiểm tra xem đăng nhập thành công hay không
    if driver.current_url == "https://app.golike.net/home":
        print("Đăng nhập thành công !")
    else:
        print("Đăng nhập thất bại !")
        driver.quit()
        exit()

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/div/div/div/div/button")
    element.click()
    sleep(2)

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]")
    element.click()
    sleep(2)

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/span/div[4]/div/div/div[2]/div[2]")
    element.click()
    sleep(2)

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]")
    element.click()
    sleep(2)

    # Tạo thư mục "accounts" sau khi đăng nhập thành công
    os.makedirs(accounts_dir)

else:
    print("\nChạy tài khoản đã được lưu !")
    # Tạo đối tượng WebDriver và chạy vào thư mục "accounts"
    chrome_options.add_argument(f"user-data-dir={accounts_dir}")
    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Mở trang
    driver.get('https://app.golike.net/login/')
    sleep(2)

sleep(200)

# Vòng lặp vô hạn để giữ chương trình chạy
while True:
    pass
