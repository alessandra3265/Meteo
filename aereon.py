from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = "http://clima.meteoam.it/RichiestaDatiGenerica.php"
value="Precipitazione cumulata|prec2|prec2^prec1|Precipitazioni cumulate 12-24 UTC^Precipitazioni cumulate 00-12 UTC|syr_stor|syr_stor|wmo|Syrep|validity|2|cl|COSTO_RIL_ALFA"
aquila ="495||16228|LIQI|L'Aquila Preturo"
session = HTMLSession()

def get_all_forms(url):
    res = session.get(url)
    res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Returns the HTML details of a form,
    including action, method and list of form controls (inputs, etc)"""
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

data = {}
for input_tag in form_details["inputs"]:
    if input_tag["type"] == "hidden":
        # if it's hidden, use the default value
        data[input_tag["name"]] = input_tag["value"]
    elif input_tag["name"] == None:
        data['categoria'] = "Precipitazioni"
        
data['parametri[]'] = value
data['messaggio'] = "syr_stor,syr_stor,wmo,Syrep,validity,2,cl,COSTO_RIL_ALFA"
data['wmo_station[]'] = "87||16230|LIBP|Pescara"
#print(data)


res2 = session.post(url, data=data)
res2.html.render()
soup2 = BeautifulSoup(res2.html.html, "html.parser")

print(soup2.text) 