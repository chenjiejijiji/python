import commernt

def set_variables(dr,variables):
	set_info = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='%s'"%(variables)
	dr.execute_script(set_info)
	dr.find_element_by_id("publish").click()

def get_text(dr,element):
	return dr.find_element_by_css_selector(element).text

# def send_info(dr,data,text):
# 	dr.get(commernt.URL() + "wp-admin/post-new.php")
# 	print data
# 	dr.find_element_by_name("post_title").send_keys(data)
# 	set_variables(dr,text)
# 	number = dr.find_element_by_id("sample-permalink").text.split('=')[-1]
# 	return number

def find(dr,data,tltle_element):
	dr.get(commernt.URL())
	dr.find_element_by_id("s").send_keys(data)
	dr.find_element_by_id("searchsubmit").click()
	get_info = get_text(dr,tltle_element)
	print get_info
	return get_info

