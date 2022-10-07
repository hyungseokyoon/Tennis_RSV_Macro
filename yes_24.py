from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chromeDirec = "C:/ChromeTemp/Default"
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=socks5://127.0.0.1:9150')
#options.add_argument("user-data-dir=" + chromeDirec) # 쓰던 크롬으로 열게 설정
#options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
url_login = "https://www.yes24.com/Templates/FTLogin.aspx?ReturnURL=http://ticket.yes24.com/Special/42449"
driver.get(url_login)

try:
    id = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "SMemberID"))
    )
finally:
    id.send_keys("yhs0414")
    pw = driver.find_element(By.ID, "SMemberPassword")
    pw.send_keys("!roka0728")
    login_btn = driver.find_element(By.XPATH, "//*[@id='btnLogin']/span/em")
    login_btn.click()
    driver.implicitly_wait(4)

while True:
    try:
        pic = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CLASS_NAME, "rn-product-imgbox"))
        )
    finally:
        notice_list = driver.find_elements(By.ID, "divNoticeTicketOpen")
        if len(notice_list) != 0:
            driver.refresh()
            driver.implicitly_wait(2)
        else:
            try:
                start_btn = WebDriverWait(driver, 50).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "rn-bb03"))
                )
            finally:
                start_btn.click()

            while True:
                list = driver.window_handles
                if len(list) >= 2:
                    break
            print(driver.window_handles)
            driver.switch_to.window(driver.window_handles[-1])

            try:
                date_btn = WebDriverWait(driver, 50).until(
                    EC.presence_of_element_located((By.ID, "2022-07-16"))
                )
            finally:
                date_btn.click()

            try:
                time_btn = WebDriverWait(driver, 50).until(
                    EC.presence_of_element_located((By.ID, "ulTime"))
                )
            finally:
                time_btn2 = driver.find_element(By.ID, "ulTime").find_elements(By.TAG_NAME, "li")
                time_btn2[1].click()

            try:
                seatselect_btn = WebDriverWait(driver, 50).until(
                    EC.presence_of_element_located((By.ID, "btnSeatSelect"))
                )
            finally:
                seatselect_btn.click()

            print(driver.window_handles)

            try:
                seat_area = driver.find_element(By.ID, "grade_R석")
            finally:
                seat_area.click()