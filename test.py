#https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20200122T170248Z.de87d85bf55ff34f.1d5d0127e696c6496ff9250a57595d18c38f5abd&lang=es-en&text=arbol
import requests
import json

def dictionary():
    url = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?"
    key = "dict.1.1.20200122T170248Z.de87d85bf55ff34f.1d5d0127e696c6496ff9250a57595d18c38f5abd"
    text = "ladron" #request.POST['text'].lower().strip()
    lang = "es-es" #request.POST['lang']



    # Request data from the yandex API
    url = url + "key="+key+"&text="+text+"&lang="+lang
    response = requests.get(url, verify=False)
    data = json.loads(response.text)

    info = {}   #dictionary holding all the words under all the definitions
    words = {}  #dictipmary holding words under each definitions
    sub = []    #holds the words under the "syn" key
    
    # Loop through possible definitions of the word
    for definition in range(len(data["def"])):
        words = {}
        # Loop through all of the words used to describe the word
        for entry in range(len((data["def"][definition]["tr"]))):
            sub = []
            # Get the nested words (if any)
            if ('syn' in data["def"][definition]["tr"][entry]):
                for child in range(len(data["def"][definition]["tr"][entry]['syn'])):
                    sub.append(data["def"][definition]["tr"][entry]['syn'][child]['text'])

            words[data["def"][definition]["tr"][entry]['text']] = sub
        
                    
        info[str(definition)] = words  

    return info


print(dictionary())