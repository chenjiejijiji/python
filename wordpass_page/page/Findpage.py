from Casepage import Basepage
class Findpage(Basepage):
	def __init__(self,driver):
		super(Findpage,self).__init__(driver)
		self.url="http://localhost/wordpress/"
		self.get()

	def send_search_title(self):
		return self.by_id("s")

	def Click(self):
		return self.by_id("searchsubmit")

	def get_search_text(self):
		return self.css_selector(".entry-summary p")
	
	def get_search_title(self):
		return self.css_selector(".entry-title a")

	def Find(self,title):
		info = []
		self.send_search_title().send_keys(title)
		self.Click().click()
		a = self.get_search_title().text
		b = self.get_search_text().text
		info.append(a)
		info.append(b)
		return info

	# def Find_serch_title(self,title):
	# 	self.send_search_title().send_keys(title)
	# 	self.Click().click()
	# 	return self.




