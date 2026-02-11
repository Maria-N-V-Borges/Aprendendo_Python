import urllib.request
import urllib.error

try:  
    url = 'https://www.pudim.com.br'
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )


    with urllib.request.urlopen(req) as site:
        print('✅ O site Pudim está acessível!') 

except urllib.error.URLError:
    print('❌ O site Pudim não está acessível.')
