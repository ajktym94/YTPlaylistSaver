import requests, time, json
import webbrowser
from selenium import webdriver

URL = {
        'M_URL' : "https://www.youtube.com/playlist?list=PLqLu_Fx0uieHjlT21DeCjlL_YMnFVKOsC",
        'T_URL' : "https://www.youtube.com/playlist?list=PLqLu_Fx0uieGh66chFLg-_exltlbjC-c7",
        'E_URL' : "https://www.youtube.com/playlist?list=PLqLu_Fx0uieEGpsqV5B5Bcinm_Bhvh3aI",
        'H_URL' : "https://www.youtube.com/playlist?list=PLqLu_Fx0uieG3ZflewYgXb2x2VoE28aVm"
    }



'''tracks = {
    'M' : {
        'tracks' :[],
        'deleted' :[]
    },
    'T' : {
        'tracks' :[],
        'deleted' :[]
    },
    'E' : {
        'tracks' :[],
        'deleted' :[]
    },
    'H' : {
        'tracks' :[],
        'deleted' :[]
    }
}
'''

browser = webdriver.Firefox()

in_file = open('data.json', 'r', encoding='UTF-8')
tracks = json.load(in_file)

for lang,url in URL.items():
    browser.get(url)

    vids = browser.find_elements_by_id('video-title')

    del_list = tracks[lang[0]]['deleted']

    for vid in vids:
        d={}
        d['name'] = vid.text
        d['link'] = vid.get_attribute('href').split('&')[0]

        if d['name'] == '[Deleted video]':
            for item in tracks[lang[0]]['tracks']:
                if item['link'] == d['link']:
                    del_name = item['name']
                    break
            if del_name not in tracks[lang[0]]['deleted']:
                tracks[lang[0]]['deleted'].append(del_name)

            continue

        if d not in tracks[lang[0]]['tracks']:
            tracks[lang[:1]]['tracks'].append(d)
        
browser.close()
out_file = open('data.json', 'w')
json.dump(tracks, out_file, indent=5)
out_file.close()

HTML = """<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>List of Deleted Videos</title>
</head>

<body>"""

for lang in URL.keys():
    HTML+="<h1>"+lang[0]+"</h1>"
    for title in tracks[lang[0]]['deleted']:
        HTML+= title+"<br>"

HTML+="""</body>

</html>"""

ht = open("deleted list.html", "w")
ht.write(HTML)
ht.close()
webbrowser.open("deleted list.html")

