from Casepage import Basepage
class Loginpage(Basepage):
	def __init__(self,driver):
		super(Loginpage,self).__init__(driver)
		self.url = 'http://localhost/wordpress/wp-login.php'
		self.get()

	
	def send_username(self):
		return self.by_id("user_login")
	

	def send_password(self):
		return self.by_id("user_pass")

	def Click(self):
		return self.by_id("wp-submit")

	def Login(self,username,password):
		self.send_username().send_keys(username)
		self.send_password().send_keys(password)
		self.Click().click()
		

