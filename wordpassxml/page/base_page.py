class BasePage(object):
	url =None
	dr = None

	def __init__(self,driver):
		self.driver = driver

	def title(self):
		return self.driver.get_title()

	def url(self):
		return self.url

	def fill_from_by_css(self,form_css,value):
		elem = self.driver.find(form_css)
		elem.send_keys(value)

	def fill_from_by_id(self,form_element_id,value):
		return self.fill_from_by_css('#%s' %form_element_id,value)

	def navigate(self):
		self.driver.get(self.url)



