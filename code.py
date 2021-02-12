import requests, time, json
from selenium import webdriver

URL = {'M_URL' : "https://www.youtube.com/playlist?list=PLqLu_Fx0uieHjlT21DeCjlL_YMnFVKOsC",
    'T_URL' : "https://www.youtube.com/playlist?list=PLqLu_Fx0uieGh66chFLg-_exltlbjC-c7",
    'E_URL' : "https://www.youtube.com/playlist?list=PLqLu_Fx0uieEGpsqV5B5Bcinm_Bhvh3aI",
    'H_URL' : "https://www.youtube.com/playlist?list=PLqLu_Fx0uieG3ZflewYgXb2x2VoE28aVm"}



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

'''
<ytd-menu-service-item-renderer class="style-scope ytd-menu-popup-renderer" use-icons="" role="menuitem" tabindex="-1" aria-selected="false"><!--css-build:shady--><paper-item class="style-scope ytd-menu-service-item-renderer" role="option" tabindex="0" aria-disabled="false"><!--css-build:shady-->
    
    
  <yt-icon class="style-scope ytd-menu-service-item-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon"><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z" class="style-scope yt-icon"></path></g></svg><!--css-build:shady--></yt-icon>
  <yt-formatted-string class="style-scope ytd-menu-service-item-renderer"><span dir="auto" class="style-scope yt-formatted-string">Remove from </span><span dir="auto" class="style-scope yt-formatted-string">Hindi Pwoli</span></yt-formatted-string>

</paper-item>
</ytd-menu-service-item-renderer>


<button id="button" class="style-scope yt-icon-button">
  <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path></g></svg><!--css-build:shady--></yt-icon>
</button>'''