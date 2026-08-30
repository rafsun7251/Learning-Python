#Modules  has 2 version 
#1. Built in modules
#2. External modules

import math 
import mymodule 
import requests

print(math.sqrt(17))
mymodule.Hello()
r = requests.get("https://www.facebook.com/jawadshahriar.toha")
#print("Jawad Shahriar profile: : ", r.text) 
css_url = "https://www.facebook.com/jawadshariar.toha"
css_response = requests.get(css_url)
print("CSS code: ", css_response.text)