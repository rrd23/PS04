from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_wikipedia(query):
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Ждем загрузки страницы

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == '1':
            paragraphs = driver.find_elements(By.TAG_NAME, "p")
            for i, para in enumerate(paragraphs):
                print(f"Параграф {i + 1}: {para.text[:200]}...")  # Показываем первые 200 символов параграфа
                more = input("Показать следующий параграф? (да/нет): ")
                if more.lower() != 'да':
                    break

        elif choice == '2':
            links = driver.find_elements(By.CSS_SELECTOR, "#bodyContent a")
            for i, link in enumerate(links[:10]):  # Показываем первые 10 ссылок
                print(f"{i + 1}. {link.text} ({link.get_attribute('href')})")
            link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
            if 0 <= link_choice < len(links):
                driver.get(links[link_choice].get_attribute('href'))
                time.sleep(2)  # Ждем загрузки страницы

        elif choice == '3':
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

    driver.quit()

if __name__ == "__main__":
    query = input("Введите запрос для поиска на Википедии: ")
    search_wikipedia(query)
