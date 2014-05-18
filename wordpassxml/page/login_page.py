from base_page import BasePage

class LoginPage(BasePage):

	def __init__(self,driver):
		super(LoginPage,self).__init__(driver)
		self.url = 'http://localhost/wordpress/wp-login.php'
		self.navigate()

	def user_text_fild(self):
		return self.driver.find_element_by_id('user_login')

	def password_text_fild(self):
		return self.driver.find_element_by_id('user_pass')

	def login_btn(self):
		return self.driver.find_element_by_id('wp-submit')

	def login(self,username,password):
		self.user_text_fild().send_keys(username)
		self.password_text_fild().send_keys(password)
		self.login_btn().click()