import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f"\033[31mO site não está disponível.\033[m")
else:
    print("\033[33mO site está disponível.\033[m")

