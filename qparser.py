from selenium import webdriver


def main():
    driver = webdriver.Firefox()
    driver.get('https://partyinfo.ru/event=17573')
    btn_elem = driver.find_element_by_link_text('Контакты')
    btn_elem.click()
    print(btn_elem)

if __name__ == '__main__':
    main()
