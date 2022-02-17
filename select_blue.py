import time

class SelectBlue():

	def select_blue_tshirt(self,driver):
		tshirt_element = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[3]/a')
		tshirt_element.click()

		blue_element = driver.find_element_by_xpath('//*[@id="color_2"]')
		blue_element.click()

		time.sleep(8)
		
		add_to_cart_element = driver.find_element_by_xpath('//*[@id="add_to_cart"]/button')
		add_to_cart_element.click()

		time.sleep(10)

		cross_element = driver.find_element_by_class_name('cross')
		cross_element.click()
		print('blue tshirt selected.')