import time

class Casual():

	def select_casual_dress(self,driver):
		dresses_element = driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[2]/a")
		dresses_element.click()

		casual_element = driver.find_element_by_xpath('//*[@id="categories_block_left"]/div/ul/li[1]/a')
		casual_element.click()

		add_to_cart_element = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]')
		add_to_cart_element.click()

		time.sleep(3)

		cross_element = driver.find_element_by_class_name('cross')
		cross_element.click()
		print('casual dress selected.')