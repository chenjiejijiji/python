from Casepage import Basepage
class Createpage(Basepage):
	
	def __init__(self,driver):
		super(Createpage,self).__init__(driver)
		self.url = 'http://localhost/wordpress/wp-admin/post-new.php'
		self.get()

	def send_tiltle(self):
		return self.by_id("title")

	def send_text(self,text):
		set_info = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='%s'"%(text)
		return self.driver.execute_script(set_info)

	def Click(self):
		return self.by_id("publish")

	def get_pen(self):
		return self.by_id("sample-permalink")

	def Create(self,title,text):
		self.send_tiltle().send_keys(title)
		self.send_text(text)
		self.Click().click()
		return  self.get_pen().text.split('=')[-1]
