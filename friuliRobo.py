import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser

url = "https://www.osmer.fvg.it/archivio.php?ln=&p=dati"
br = RoboBrowser(parser="html.parser")
br.open(url)
form = br.get_form()

print(form)

form['stazione'] = "ARI@Ariis@syn@45.878300@13.090000@13"
form['tipo'] = "H_3"

print(form)

br.submit_form(form)

soup = br.parsed

print(soup)