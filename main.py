from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Функция ожидания элементов
def wait_of_element_located(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


# Вынесем аутентификацию юзера в отдельную функцию
def auth_user(user_name, password, driver):
    # Поиск и ожидание элементов и присваивание к переменным.
    input_username = wait_of_element_located(xpath='//*[@id=\"user-name\"]', driver=driver)
    input_password = wait_of_element_located(xpath='//*[@id=\"password\"]', driver=driver)
    login_button = wait_of_element_located(xpath='//*[@id=\"login-button\"]', driver=driver)

    # Действия с формами
    input_username.send_keys(user_name)
    input_password.send_keys(password)
    login_button.send_keys(Keys.RETURN)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

