from Casepage import Basepage
class Revisepage(Basepage):
	def __init__(self,driver,pen):
		super(Revisepage,self).__init__(driver)
		self.url="http://localhost/wordpress/wp-admin/post.php?post="+pen+"&action=edit"
		self.get()

	def send_revise_text(self,revise_text):
		set_info = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='%s'"%(revise_text)
		return self.driver.execute_script(set_info)

	def Click(self):
		return self.by_id("publish")

	def Revise(self,revise_text):
		self.send_revise_text(revise_text)
		self.Click().click()
		return revise_text





