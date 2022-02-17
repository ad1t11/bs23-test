class SignIn():

	def sign_in(self,driver,email,password_val):

		sign_in = driver.find_element_by_class_name('login')
		sign_in.click()

		login_field = driver.find_element_by_id("email")
		login_field.send_keys(email)

		pass_field = driver.find_element_by_id("passwd")
		pass_field.send_keys(password_val)

		signin_field = driver.find_element_by_id("SubmitLogin")
		signin_field.click()
		print('signin:', email)