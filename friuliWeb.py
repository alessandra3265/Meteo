from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = "https://www.osmer.fvg.it/archivio.php?ln=&p=dati"

session = HTMLSession()

"""

def get_all_forms(url):
    res = session.get(url)
    res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    
    details = {}
    # get the form action (requested URL)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, DELETE, etc)
    # if not specified, GET is the default in HTML
    method = form.attrs.get("method", "get").lower()
    # get all form inputs
    inputs = []
    for input_tag in form.find_all("input"):
        # get type of input form control
        input_type = input_tag.attrs.get("type", "text")
        # get name attribute
        input_name = input_tag.attrs.get("name")
        # get the default value of that input tag
        input_value =input_tag.attrs.get("value", "")
        # add everything to that list
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


forms = get_all_forms(url)

#get the first form
first_form = get_all_forms(url)[0]

#get form details 
form_details = get_form_details(first_form)

print(form_details)


"""

data = {}
data['a'] = "2020"
data['m'] = "6"
data['g'] = "21"
data['s'] = "ARI@Ariis@syn@45.878300@13.090000@13"
data['t'] = "H_2"
data['ln'] = ""
data['o'] = "visualizza"

action = "/archivio.php"

url = url + action

res2 = session.post(url, data=data)
res2.html.render()
soup2 = BeautifulSoup(res2.html.html, "html.parser")

print(soup2.prettify) 

