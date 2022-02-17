class Form():

	def fill_up_form(self, driver, first_name_val,last_name_val, password, days, month, year, company_field_name,
		address_field_val,city_name,state_name,post_val,mobile_num,add_alias,register_btn):
		
		radio_button = driver.find_element_by_id('id_gender1')
		radio_button.click()

		first_name = driver.find_element_by_id("customer_firstname")
		first_name.send_keys(first_name_val)

		last_name = driver.find_element_by_id("customer_lastname")
		last_name.send_keys(last_name_val)

		password_field = driver.find_element_by_id("passwd")
		password_field.send_keys(password)

		days_field = driver.find_element_by_id("days")
		days_field.send_keys(days)

		month_field = driver.find_element_by_id("months")
		month_field.send_keys(month)

		year_field = driver.find_element_by_id("years")
		year_field.send_keys(year)

		newslatters_field = driver.find_element_by_id("newsletter")
		newslatters_field.click()

		partners_field = driver.find_element_by_id("optin")
		partners_field.click()

		company_field = driver.find_element_by_id("company")
		company_field.send_keys(company_field_name)

		address_field = driver.find_element_by_id("address1")
		address_field.send_keys(address_field_val)

		city_field = driver.find_element_by_id("city")
		city_field.send_keys(city_name)

		state_field = driver.find_element_by_id("id_state")
		state_field.send_keys(state_name)

		postcode_field = driver.find_element_by_id("postcode")
		postcode_field.send_keys(post_val)

		mobile_field = driver.find_element_by_id("phone_mobile")
		mobile_field.send_keys(mobile_num)

		addressalias_field = driver.find_element_by_id("alias")
		addressalias_field.send_keys(add_alias)

		register_field = driver.find_element_by_id("submitAccount")
		register_field.click()

		print('form fill up done.')