class SignOut():

	def sign_out(self, driver):
		driver.get("http://automationpractice.com/index.php?mylogout=")
		print('successful signout.')