import selenium.webdriver.common.service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime

def findDay(wanted_date):
    year = int(wanted_date[:4])
    month = int(wanted_date[4:6])
    day = int(wanted_date[6:])
    return datetime.datetime(year, month, day).weekday()

def changeNumtoZeroTime(time):
    zeroTime = "0"+str(time)+"00" if time < 10 else str(time)+"00"
    return zeroTime

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

## google login
#C:\>cd C:\Program Files (x86)\Google\Chrome\Application chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/CHROMETEMP"

## login page
url_login = "https://www.ycs.or.kr/page/etc/login.php?referer=https%3A%2F%2Fwww.ycs.or.kr%2Fyeyak%2Ffmcs%2F43%3Ffacilities_type%3DT%26base_date%3D20221005%26rent_type%3D1001%26center%3DYCS04%26part%3D02%26place%3D14%23proc_list_tab"
driver.get(url_login)

## required parameter
wanted_date = "20221014"
wanted_courtnum = "15"
wanted_date_day = findDay(wanted_date)
end_or_not = "평일" if wanted_date_day < 5 else "주말"
want_time = 15

try:
    id = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "id"))
    )
finally:
    id.send_keys("")
    pw = driver.find_element(By.ID, "pw")
    pw.send_keys("")
    login_btn = driver.find_element(By.XPATH, "//*[@id='content']/form/div/input[3]")
    login_btn.click()

    while(datetime.datetime.now()<datetime.datetime(2022,10,6,9,30,0,0)) :
        driver.refresh()
        driver.implicitly_wait(0.5)

    driver.get("https://www.ycs.or.kr/yeyak/fmcs/43?facilities_type=T&center=YCS04&part=02&base_date="
               + wanted_date
               + "&action=write&place="
               + wanted_courtnum
               + "&comcd=YCS04&part_cd=02&place_cd="
               + wanted_courtnum
               + "&time_no="
               + str(want_time+577)
               + "%3B"
               + end_or_not
               + "%" + str(192 + want_time)
               + "회%3B"
               + changeNumtoZeroTime(want_time)
               + "%3B"
               + changeNumtoZeroTime(want_time+1)
               + "%3B1&rent_type=1001&rent_date="
               + wanted_date
               )

    try:
        team_name = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, "team_nm"))
        )
    finally:
        team_name.send_keys("윤형석")
        users = driver.find_element(By.ID, "users")
        users.send_keys("2")
        purpose = driver.find_element(By.ID, "purpose")
        purpose.send_keys("연습")
        tel = driver.find_element(By.ID, "tel")
        tel.clear()
        tel.send_keys("070-7114-3313")
        agree = driver.find_element(By.ID, "agree_use1")
        agree.click()

        try :
            capchaframe = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        finally:
            driver.switch_to.frame(capchaframe)
            try :
                capchaagree = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "recaptcha-checkbox-border")))
            finally:
                driver.execute_script("document.getElementsByClassName('recaptcha-checkbox-border')[0].click();")
                driver.switch_to.default_content()
                try:
                    result = driver.switch_to.alert()
                    result.accept()
                except:
                    pass
                finally:
                    driver.execute_script("document.getElementsByClassName('button action_write')[0].style.display='inline-block';")
                    driver.execute_script("document.getElementsByClassName('button action_write')[0].click();")
                    try:
                        result = driver.switch_to.alert()
                        result.accept()
                    except:
                        pass
                    finally :
                        driver.execute_script("document.getElementsByClassName('button action_write')[0].click();")



