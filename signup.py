from form import Form
import time
class SignUp():

	def sign_up(self,email,driver):
		sign_in = driver.find_element_by_class_name('login')
		sign_in.click()

		email_field = driver.find_element_by_id('email_create')
		email_field.send_keys(email)

		create_account_btn = driver.find_element_by_id('SubmitCreate')
		create_account_btn.click()

		time.sleep(10)

		form_page = Form()
		form_page.fill_up_form(driver,'john','snow','json123',"15","february","2022","random company",
			"home","dhaka","dhaka","12050","01712345678","alias","reg")
		print('signup done with email:',email)