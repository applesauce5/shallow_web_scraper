from bs4 import BeautifulSoup
import requests
import re
import wget
import urllib.parse
import urllib.request
from lxml import html

def scrape_data(url, destination):
	comp_dom = re.compile("https:\/\/[.a-zA-Z0-9]+|http:\/\/[.a-zA-Z0-9]+")
	domain = comp_dom.findall(url)
	if domain:
		domain = domain[0]
		req = requests.get(url)
		content = req.text
		soup = BeautifulSoup(content, "html.parser")

		for link in soup.find_all("a"):
			link_url = str(link.get("href"))
			file_ext = re.compile("xls|xlsx|csv|zip")
			b_list = file_ext.findall(link_url)
			if b_list:
				c = link_url
				if not re.search("http.*|https.*", link_url):
					c = domain+link_url
				c = c.replace(" ", "%20")
				match_comp = re.compile("[_a-zA-Z0-9]+.xls|[_a-zA-Z0-9]+.xlsx|[_a-zA-Z0-9]+.csv|[_a-zA-Z0-9]+.zip")
				match_fl = match_comp.findall(c)
				print(c)
				if match_fl:
					filename_loc = match_fl[0]
					print("=====", destination, str(filename_loc), c)
					local_filename, headers = urllib.request.urlretrieve(c, filename = destination+"/" +str(filename_loc))
					print(local_filename)

if __name__ == "__main__":
	destination = "./output"
	url = "https://chiarasabatti.su.domains/data.html"
	scrape_data(url, destination)
