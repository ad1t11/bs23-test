import time

class Checkout():

	def checkout_payment(self,driver):
		time.sleep(2)
		checkout_element = driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a')
		checkout_element.click()

		time.sleep(2)
		proceed_checkout_element = driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]')
		proceed_checkout_element.click()

		time.sleep(2)
		proceed_checkout_element = driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button')
		proceed_checkout_element.click()
		
		time.sleep(2)
		i_agree_element = driver.find_element_by_id('cgv')
		i_agree_element.click()

		time.sleep(2)
		proceed_checkout_element = driver.find_element_by_xpath('//*[@id="form"]/p/button')
		proceed_checkout_element.click()
		
		pay_by_check_element = driver.find_element_by_xpath('//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a')
		pay_by_check_element.click()
		print('checkout done.')
