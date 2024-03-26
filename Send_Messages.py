def send_message(contact_list, message):
    import time
    from selenium.webdriver.common.keys import Keys
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from selenium.webdriver.chrome.service import Service
    # Specify the path to the user data directory of the existing Chrome profile
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--user-data-dir=/path/to/your/chrome/profile')
    service = Service
    driver = webdriver.Chrome(options=chrome_options)
    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    try:
        # Wait for an element to appear on the WhatsApp Web page (e.g., chat list)
        print("Ppening web Whatsapp ")
        wait = WebDriverWait(driver, 60)
        chat_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_2vDPL')))

        print(chat_list.text)
        # print("element have been found ")
        for contact in contact_list:
            new_message = driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div/div[2]/div[3]/header/div[2]/div/span/div[4]/div")
            new_message.click()
            time.sleep(1)
            search_bar = driver.find_element(By.XPATH,
                                             value="/html/body/div[1]/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]")
            search_bar.click()
            time.sleep(1)
            # Now you can interact with the chat list or other elements on the page
            # For example, you can print the chat list's text
            # print(chat_list.text)
            search_bar.send_keys(contact)
            time.sleep(1)
            user = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='{}']".format(contact))))
            user.click()
            time.sleep(1)
            # message_filed = wait.until(EC.presence_of_element_located((By.XPATH, "_3Uu1_")))
            message_input = driver.find_element(By.XPATH,
                                                value="//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
            message_input.send_keys(message)
            message_input.send_keys(Keys.ENTER)
            time.sleep(2)


    except Exception as e:
        "error you should scan the qrcode "
        print("An error occurred:", e)
        driver.quit()

    # Remember to close the driver when you're done
    driver.quit()
