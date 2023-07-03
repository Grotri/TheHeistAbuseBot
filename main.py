import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mnemonic import Mnemonic
from multiprocessing import Pool


def getdata(words):
    try:
        options = Options()
        options.add_extension('phantom1.crx')
        options.add_argument("--window-size=1280,960")
        driver = webdriver.Chrome(options=options)
        driver.get('https://google.com')
        driver.switch_to.window(driver.window_handles[1])
        wallet_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[2]/div/div[2]/button[2]')))
        wallet_button.click()
        time.sleep(0.5)
        word1 = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/form/div/div[2]/div[1]/input')
        word1.send_keys(words)
        time.sleep(0.3)
        import_wallet = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/form/button')
        import_wallet.click()
        import_check = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[2]/form/button[2]')))
        import_check.click()
        passw = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[2]/form/div[1]/div[2]/input')))
        passw.send_keys('12345678')
        pass_check = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/form/div[1]/div[2]/div/div/input')
        pass_check.send_keys('12345678')
        agree_check = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/form/div[2]/span/input')
        agree_check.click()
        time.sleep(0.3)
        continue_wallet = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/form/button')
        continue_wallet.click()
        time.sleep(0.7)
        final_wallet = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/form/button')
        final_wallet.click()
        time.sleep(0.5)
        finish_wallet = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/form/button')
        finish_wallet.click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.get('https://theheist.game')
        connect = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/header/div[3]/button')))
        connect.click()
        connect_phantom = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/header/div[3]/ul/li[1]/button')))
        connect_phantom.click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        connect_in_phantom = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div[2]/div/button[2]')))
        connect_in_phantom.click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        approve = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/div[2]/div/button[2]')))
        approve.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        hub_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[3]/div/div[1]/div[2]/button[1]')))
        hub_button.click()
        time.sleep(1)
        rewards_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[7]/button')))
        rewards_button.click()
        time.sleep(3)
        claim_ticket = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/button')))
        claim_ticket.click()
        time.sleep(3)
        # throw_ticket = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[4]/button[2]')))
        # throw_ticket.click()
        time.sleep(3)
        log = open('log.txt', mode='a')
        log.write(words + '\n')
        log.close()
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


total_tickets = int(input("Enter number of total tickets to process: "))
threads_num = int(input("Enter number of treads: "))
mnems = []
for i in range(1, math.ceil(total_tickets/threads_num)):
    for i in range(1, threads_num):
        mnemo = Mnemonic("english")
        words = mnemo.generate(strength=128)
        mnems.append(words)
    if __name__ == '__main__':
        p = Pool(processes=threads_num)
        p.map(getdata, mnems)



