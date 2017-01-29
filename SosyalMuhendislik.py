import requests
import webbrowser


url="https://www.donanimhaber.com"
sayfa=requests.get(url,verify=False)
Dosya=open("/Users/anilbaranyelken/PycharmProjects/blackbox/dosya.html","w")
Dosya.write(sayfa.content)
Dosya.close()
webbrowser.open_new("/Users/anilbaranyelken/PycharmProjects/blackbox/dosya.html")
