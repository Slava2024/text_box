import unittest
from selenium import webdriver
from main import wait_of_element_located
from main import auth_user


class MyTestCase(unittest.TestCase):
	
	def test_add_jacket_to_the_shopcart(self):
		driver = webdriver.Firefox()
		driver.get("https://www.saucedemo.com/")
		
		# Аутентификация пользователя
		auth_user("standard_user", "secret_sauce", driver=driver)
		
		# Поиск и проверка попадания на главную страницу
		self.assertEqual("PRODUCTS", wait_of_element_located(
			xpath='//*[@id=\"header_container\"]/div[2]/span', driver=driver).text)
		
		# Поиск ссылки элемента позиции магазина и клик по ссылке
		item_name = driver.find_element("xpath", "//*[@id=\"item_1_title_link\"]/div")
		self.assertEqual("Sauce Labs Bolt T-Shirt", item_name.text)
		item_name.click()
		
		# Поиск кнопки коризины и клик по этой кнопке
		wait_of_element_located(xpath='//*[@id=\"add-to-cart-sauce-labs-bolt-t-shirt\"]', driver=driver).click()
		
		wait_of_element_located(xpath='//*[@id=\"shopping_cart_container\"]/a', driver=driver).click()
		
		# Еще один поиск ссылки элемента позиции магазина
		item_name = driver.find_element("xpath", "//*[@id=\"item_1_title_link\"]/div")
		self.assertEqual("Sauce Labs Bolt T-Shirt", item_name.text)
		
		continue_shop = driver.find_element("id", "continue-shopping")
		continue_shop.click()
		
		# Добовляем в корзину Sauce Labs Fleece Jacket
		wait_of_element_located(xpath="//*[@id=\"add-to-cart-sauce-labs-fleece-jacket\"]", driver=driver).click()
		
		wait_of_element_located(xpath='//*[@id=\"shopping_cart_container\"]/a', driver=driver).click()
		self.assertEqual('2', wait_of_element_located(
			xpath='//*[@id=\"shopping_cart_container\"]/a/span', driver=driver).text)
		
		wait_of_element_located(xpath='//*[@id=\"remove-sauce-labs-bolt-t-shirt\"]', driver=driver).click()
		
		self.assertEqual('1', wait_of_element_located(
			xpath='//*[@id=\"shopping_cart_container\"]/a/span', driver=driver).text)
		
		self.assertEqual("Sauce Labs Fleece Jacket", wait_of_element_located(
			xpath='//*[@id=\"item_5_title_link\"]/div', driver=driver).text)
		
		wait_of_element_located(xpath='//*[@id=\"react-burger-menu-btn\"]', driver=driver).click()
		
		driver.find_element("id", "logout_sidebar_link").click()
		wait_of_element_located(xpath='//*[@id=\"login-button\"]', driver=driver).click()
		
		# Проверка на обработку ошибки, так как не задано имя и пароль
		self.assertEqual("Epic sadface: Username is required", wait_of_element_located(
			'//*[@data-test=\"error\"]', driver=driver).text)
		
		# Аутентификация пользователя
		auth_user("standard_user", "", driver=driver)
		
		self.assertEqual("Epic sadface: Password is required", wait_of_element_located(
			'//*[@data-test=\"error\"]', driver=driver).text)
		
		auth_user("standard_user", "1111", driver=driver)
		
		self.assertEqual("Epic sadface: Username and password do not match any user in this service",
		                 wait_of_element_located('//*[@data-test=\"error\"]', driver=driver).text)
		
		driver.close()


if __name__ == '__main__':
	unittest.main()
