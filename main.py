from selenium import webdriver
import time

from signup import SignUp
from signin import SignIn
from signout import SignOut
from form import Form
from casual import Casual
from select_blue import SelectBlue
from checkout import Checkout

driver = webdriver.Chrome("E:\projects\python\AD\chromedriver")

def main():
	driver.get("http://automationpractice.com/index.php")
	sign_out_obj = SignOut()

	sign_up_page = SignUp()
	sign_up_page.sign_up('test1fshgyf55@gmail.com',driver)

	sign_out_obj.sign_out(driver)

	time.sleep(3)
	sign_up_page.sign_up('test1sdddsdf55@gmail.com',driver)
	sign_out_obj.sign_out(driver)

	time.sleep(3)
	sign_in_page = SignIn()
	sign_in_page.sign_in(driver, 'test1shersdf55@gmail.com','json123')
	time.sleep(3)

	casual_page = Casual()
	casual_page.select_casual_dress(driver)

	select_blue_page = SelectBlue()
	select_blue_page.select_blue_tshirt(driver)

	checkout_page = Checkout()
	checkout_page.checkout_payment(driver)

	sign_out_obj.sign_out(driver)

main()

print('done.')
