class Basepage(object):
	url = None
	dr = None

	def __init__(self,driver):
		self.driver = driver

	def title(self):
		return self.driver.get_title()

	def url(self):
		return self.url

	def get(self):
		self.driver.get(self.url)

	def by_id(self,data):
		return self.driver.find_element_by_id(data)

	def css_selector(self,element):
		return self.driver.find_element_by_css_selector(element)



