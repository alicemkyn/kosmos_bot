import os
import random
import time
from datetime import datetime

import pywhatkit as kit
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium_recaptcha_solver import RecaptchaSolver

import ssdate

tckn_no = ""
mobile_no = ""
index = 0
counter = 0
text = ""
text_concat = ""


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
]

ua = UserAgent()
user_agent = ua.random

# Proxy Setup
# proxy_ip = '103.130.145.169'
# proxy_port = '80'
# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = f'{proxy_ip}:{proxy_port}'
# #proxy.ssl_proxy = f'{proxy_ip}:{proxy_port}'
# capabilities = webdriver.DesiredCapabilities.CHROME
# proxy.add_to_capabilities(capabilities)


# Service and Options
service = Service(
    executable_path="/Users/alicemkoyun/Downloads/chromedriver-mac-arm64/chromedriver"
)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=3456,2234")
# options.add_argument(f'--user-agent={random.choice(user_agents)}')
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
options = Options()
options.add_argument("--window-size=3456,2234")
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
)
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")


while True:
    driver = webdriver.Chrome(service=service, options=options)
    try:
        # Google Part
        driver.get("https://google.com")
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
        )
        input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
        input_element.clear()
        input_element.send_keys("kosmos randevu al" + Keys.ENTER)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a/h3')
            )
        )

        link = driver.find_element(
            By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a/h3'
        )
        link.click()

        # Pop-up Close
        wait = WebDriverWait(driver, 10)
        popup_close_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#popupOverlay > div > div > a > img")
            )
        )
        action = ActionChains(driver)
        action.move_to_element(popup_close_btn).click(popup_close_btn).perform()

        # Randevu Al Tikla
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/form/div[3]/div[2]/div/div/div/div/div/div/div/ul/li[2]/a",
                )
            )
        ).click()

        # Cookie Accept
        accept_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#cookieBanner > button"))
        )
        accept_btn.click()

        # IFrame Sec
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        iframe_1 = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe_1)

        # Scroll IFrame
        element = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]",
                )
            )
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)
        # driver.execute_script('arguments[0].click()', element)

        # Dropdown City Menu Click
        dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "cities"))))
        time.sleep(random.uniform(0.5, 1.5))
        # driver.execute_script('arguments[0].click()', dropdown)
        dropdown.select_by_visible_text("Izmir")

        # Scroll to Bodrum and Select
        element = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[4]/div[2]/div[2]/div[2]/div/div[2]/div",
                )
            )
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(random.uniform(1.5, 2.2))
        driver.execute_script("arguments[0].click()", element)

        # Sonraki Button Scroll and Click
        element = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div[3]/div[2]/span/button",
                )
            )
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(random.uniform(1.1, 1.8))
        driver.execute_script("arguments[0].click();", element)

        # Basvuru Tipi, Basvuru Sekli Select and TCKN Fill
        basvuru_tipi = Select(
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="__BVID__123"]/div/span/select')
                )
            )
        )
        driver.execute_script(
            "arguments[0].scrollIntoView();",
            driver.find_element(By.XPATH, '//*[@id="__BVID__123"]/div/span/select'),
        )
        time.sleep(random.uniform(1.4, 2.1))
        basvuru_tipi.select_by_visible_text("Bireysel")
        basvuru_sekli = Select(
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="__BVID__130"]/div/span/select')
                )
            )
        )
        basvuru_sekli.select_by_visible_text("Standart")
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__BVID__129"]')))
        tckn = driver.find_element(By.XPATH, '//*[@id="__BVID__129"]')
        tckn.clear()
        for i in tckn_no:
            tckn.send_keys(i)
            time.sleep(random.uniform(0.05, 0.1))

        # I am not robot Iframe switch, scroll and click.
        # iframe_2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="BilgileriniziGirin1"]/form/div/div[6]/span/div/div/div/iframe')))
        # driver.switch_to.frame(iframe_2)
        # element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rc-anchor-container"]')))
        # driver.execute_script('arguments[0].scrollIntoView();', element)
        # driver.execute_script('arguments[0].click();', element)
        recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
        time.sleep(random.uniform(0.5, 1.5))
        solver = RecaptchaSolver(driver=driver)

        try:
            solver.click_recaptcha_v2(iframe=recaptcha_iframe)
        except Exception as e:
            if e.args[0] == "Google has detected automated queries. Try again later.":
                print(e)
                if index < len(user_agents):
                    driver.quit()
                    service = Service(
                        executable_path="/Users/alicemkoyun/Downloads/chromedriver-mac-arm64/chromedriver"
                    )
                    options = Options()
                    options.add_argument("--window-size=3456,2234")
                    options.add_argument(f"user-agent={user_agents[index]}")
                    options.add_argument("--no-sandbox")
                    options.add_argument("--disable-extensions")

                    print(user_agents[index])
                    print("INDEX: ", index)
                    index += 1
                    continue
                else:
                    index = 0
                    driver.quit()
                    continue

            else:
                print(e)
                driver.quit()
                continue

        # Sonraki button IFrame switch and click
        driver.switch_to.default_content()
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/form/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/iframe",
                )
            )
        )
        iframe_1 = driver.find_element(
            By.XPATH,
            "/html/body/form/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/iframe",
        )
        driver.switch_to.frame(iframe_1)
        sonraki_btn = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div[3]/div[2]/span/button",
                )
            )
        )
        driver.execute_script("arguments[0].scrollIntoView();", sonraki_btn)
        sbtn = wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#app > div.horizontal-layout.vertical-overlay-menu.menu-hide.navbar-floating.footer-static > div.app-content.content.pt-0 > div > div > div > div:nth-child(3) > div > div > div.wizard-card-footer.clearfix > div.wizard-footer-right > span > button",
                )
            )
        )
        # action.move_to_element(sbtn).click(sbtn).perform()
        sbtn.click()

        # Finding the date
        calendar = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "vdp-datepicker__calendar"))
        )
        month_picker = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div[3]/form/div/div[1]/fieldset/div/span/div/div[2]/header/span[2]",
        )
        time.sleep(random.uniform(6.1, 6.9))
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".vdp-datepicker__calendar .cell.day")
            )
        )
        date_cells = driver.find_elements(
            By.CSS_SELECTOR, ".vdp-datepicker__calendar .cell.day"
        )
        # Aylarin gozukmesi icin scroll

        driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            driver.find_element(By.XPATH, '//*[@id="RandevuTarihiSeçimi2"]/form/h2'),
        )

        # Next Btn Locate
        time.sleep(random.uniform(1.1, 2.1))
        next_btn = driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div[3]/form/div/div[1]/fieldset/div/span/div/div[2]/header/span[3]",
        )

        # Tarih hücrelerinin arasında aktif bir tarih olup olmadığını kontrol edin
        now = datetime.now()
        h = now.hour
        m = now.minute
        s = now.second

        for cell in date_cells:
            if (
                cell.get_attribute("class") == "cell day"
                and not cell.get_attribute("class").isspace()
            ):
                print(cell.text + " " + month_picker.text)
                text += cell.text + month_picker.text.replace(" ", "")
        if text:
            driver.get_screenshot_as_file(f"{month_picker.text}.jpg")
            time.sleep(1)
        print(month_picker.text)
        # Info screenshot
        ss_name = f"ss_{month_picker.text}_{h}_{m}_{s}.jpeg"
        driver.get_screenshot_as_file(ss_name)
        ssdate.ss_add_date(ss_name, month_picker.text, tckn_no)

        now = datetime.now()
        h = now.hour
        m = now.minute
        s = now.second
        # Tarih iframe next >
        while next_btn.get_attribute("class") == "next":
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(random.uniform(1.5, 1.99))
            date_cells = driver.find_elements(
                By.CSS_SELECTOR, ".vdp-datepicker__calendar .cell.day"
            )

            for cell in date_cells:
                if (
                    cell.get_attribute("class") == "cell day"
                    and not cell.get_attribute("class").isspace()
                ):
                    print(cell.text + " " + month_picker.text)
                    text_concat += cell.text + month_picker.text + "_".replace(" ", "")
            if text_concat:
                driver.get_screenshot_as_file(f"{month_picker.text}.jpg")
                text += text_concat
                text_concat = ""
            print(month_picker.text)
        # Info screenshot
        time.sleep(1)
        ss_name = f"ss_{month_picker.text}_{h}_{m}_{s}.jpeg"
        driver.get_screenshot_as_file(ss_name)
        ssdate.ss_add_date(ss_name, month_picker.text, tckn_no)

        counter += 1
        print("COUNTER: ", counter)

        driver.quit()

        if text:
            print("TEXT: ", text)
            break
        else:
            jpeg_list = [i for i in os.listdir() if i.endswith(".jpeg")]
            for jpeg in jpeg_list:
                caption = jpeg.split("_")[1].replace(" ", "")
                kit.sendwhats_image(
                    mobile_no,
                    jpeg,
                    caption=caption + "_Tarihi_Icin_Randevu_Yok",
                    tab_close=True,
                )
                os.remove(jpeg)

        # time.sleep(90)
        break

    except Exception as e:
        print(str(e))
        if isinstance(e, NoSuchWindowException):
            driver.quit()
            break
        driver.quit()
        time.sleep(5)

# Whatsapp Part
if text:
    text = text.replace(" ", "_")
    img_list = [i for i in os.listdir() if i.endswith(".jpg")]
    list(map(ssdate.ss_found, img_list))
    kit.sendwhatmsg_instantly(mobile_no, text, tab_close=True)
    for image in img_list:
        kit.sendwhats_image(
            mobile_no,
            image,
            caption=text + "_Tarihi-Icin-Randevu-Bulundu",
            tab_close=True,
        )
for i in os.listdir():
    if i.endswith((".jpg", ".png", ".jpeg")):
        os.remove(i)

