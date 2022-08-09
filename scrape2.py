import mechanicalsoup
from bs4 import BeautifulSoup

print()
url = "https://login.uci.edu/ucinetid/webauth?return_url=https://webreg2.reg.uci.edu:443/cgi-bin/wramia?page=login?call=0012&info_text=Reg+Office+Home+Page&info_url=https://www.reg.uci.edu/"
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)

# print(browser)
print()

form = browser.select_form()


browser.form.print_summary()   # prints out all of the form options

print()

browser["ucinetid"] = "wilhelaw"
browser["password"] = "PotatoRebel890!"


browser.launch_browser()
print()
print('===========================')
print()
#response = browser.submit_selected(btnName="login_button")

my_button = browser.get_current_page().find('input', value='Login')

response = browser.submit_selected(btnName=my_button)

# print(response.url)

print(response.text)

# browser2 = mechanicalsoup.StatefulBrowser()
# browser2.open(response.url)
# browser2.select_form('form[id="webauth_login_form_id"]')
# browser2["ucinetid"] = "wilhelaw"
# browser2["password"] = "PotatoRebel890!"

# #browser2.launch_browser()

# final = browser2.submit_selected()

# print()
# print('===========================')
# print()

# print(final.url)
# print(final.text)


# print()
# print("------------")
# tds = response.soup.find_all('td')
