print("hello world")

plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]

print(plateformes_sociales)

plateformes_sociales.append("TikTok")

print(plateformes_sociales)

plateformes_sociales.remove("Snapchat")

print(plateformes_sociales)

print(len(plateformes_sociales))

plateformes_sociales.sort()

print(plateformes_sociales)

plateformes_sociales_tuple = ("Facebook", "Instagram", "TikTok", "Twitter")

print(plateformes_sociales_tuple)

nouvelle_campagne = {
    "responsable_de_campagne": "Jeanne d'Arc",
    "nom_de_campagne": "Campagne nous aimons les chiens",
    "date_de_début": "01/01/2020",
    "influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

print(nouvelle_campagne)

taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

print(taux_de_conversion)

infos_labradoodle = {
    "poids": "13 à 16 kg",
    "origine": "États-Unis"
}

infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris"

print(infos_labradoodle)

infos_labradoodle.pop("origine")

print(infos_labradoodle)

print("poids" in infos_labradoodle)
print("poids2" in infos_labradoodle)

ensoleille = False

if ensoleille:
    print("On va à la plage")
else:
    print("on reste à la maison")

races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

for x in range(5):
    print(x)

for x in range(100):
    print(f"{x} bouteilles de bières au mur !")

capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1

def add(a, b):
    return a + b

print(add(1,2))

import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

titres_bs = soup.find_all("a", class_="gem-c-document-list__item-title")
titres = []
for titre in titres_bs:
    titres.append(titre.string)

descriptions_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = []
for desc in descriptions_bs:
    descriptions.append(desc.string)

fichier = open("hello.txt", "w")
fichier.write("Hello, world!")
fichier.close()

with open("file.txt", "w") as fichier:
    for titre in titres_bs:
        fichier.write(titre.string)
        fichier.write("\r\n")