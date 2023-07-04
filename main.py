import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mnemonic import Mnemonic
from multiprocessing import Pool


def setupDriver():
    options = Options()
    options.add_extension('phantom1.crx')
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,960")
    options.page_load_strategy = 'eager'
    options.add_argument("--no-sandbox")
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.get('https://google.com')
    return driver


def waitUntil(xpath: str, time: int, driver):
    return WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, '/html/body/' + xpath)))


def findElement(xpath: str, driver):
    return driver.find_element(By.XPATH, '/html/body/' + xpath)


def getdata(words):
    driver = setupDriver()
    try:
        timer = 30
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        wallet_button = waitUntil(xpath='div/main/div[2]/div/div[2]/button[2]', time=timer, driver=driver)
        wallet_button.click()
        time.sleep(0.5)

        word1 = waitUntil(xpath='div/main/div[2]/form/div/div[2]/div[1]/input', time=timer, driver=driver)
        word1.send_keys(words)
        time.sleep(0.3)

        import_wallet = waitUntil(xpath='div/main/div[2]/form/button', time=timer, driver=driver)
        import_wallet.click()
        import_check = waitUntil(xpath='div/main/div[2]/form/button[2]', time=timer, driver=driver)
        import_check.click()

        passw = waitUntil(xpath='div/main/div[2]/form/div[1]/div[2]/input', time=timer, driver=driver)
        passw.send_keys('12345678')

        pass_check = waitUntil(xpath='div/main/div[2]/form/div[1]/div[2]/div/div/input', time=timer, driver=driver)
        pass_check.send_keys('12345678')
        time.sleep(0.3)

        agree_check = findElement(xpath='div/main/div[2]/form/div[2]/span/input', driver=driver)
        agree_check.click()
        time.sleep(0.3)

        continue_wallet = waitUntil(xpath='div/main/div[2]/form/button', time=timer, driver=driver)
        continue_wallet.click()
        time.sleep(0.7)

        final_wallet = waitUntil(xpath='div/main/div[2]/form/button', time=timer, driver=driver)
        final_wallet.click()
        time.sleep(1)

        driver.get('https://theheist.game')
        driver.switch_to.window(driver.window_handles[0])

        connect = waitUntil(xpath='div/div[2]/header/div[3]/button', time=timer, driver=driver)
        connect.click()

        connect_phantom = waitUntil(xpath='div/div[2]/header/div[3]/ul/li[1]/button', time=timer, driver=driver)
        connect_phantom.click()
        time.sleep(1)

        driver.switch_to.window(driver.window_handles[1])

        connect_in_phantom = waitUntil(xpath='div/div/div[1]/div[2]/div/button[2]', time=timer, driver=driver)
        connect_in_phantom.click()
        time.sleep(3)

        driver.switch_to.window(driver.window_handles[1])

        approve = waitUntil(xpath='div/div/div[1]/div/div[2]/div/button[2]', time=timer, driver=driver)
        approve.click()
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[0])

        hub_button = waitUntil(xpath='div/div[2]/div[3]/div/div[1]/div[2]/button[1]', time=timer, driver=driver)
        hub_button.click()
        time.sleep(1)

        rewards_button = waitUntil(xpath='div[2]/div[3]/div/div[1]/div/div[7]/button', time=timer, driver=driver)
        rewards_button.click()
        time.sleep(3)

        claim_ticket = waitUntil(xpath='div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button', time=timer, driver=driver)
        claim_ticket.click()
        time.sleep(3)
        print('Ticket claimed successfully!')

        throw_ticket = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[4]/button[2]')))
        throw_ticket.click()
        time.sleep(3)

        9
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    total_tickets = int(input("Enter number of total tickets to process: "))
    threads_num = int(input("Enter number of treads: "))
    mnems = []
    for i in range(0, math.ceil(total_tickets / threads_num)):
        for n in range(0, threads_num):
            mnemo = Mnemonic("english")
            words = mnemo.generate(strength=128)
            mnems.append(words)
        p = Pool(processes=threads_num)
        p.map(getdata, mnems)
        mnems = []
