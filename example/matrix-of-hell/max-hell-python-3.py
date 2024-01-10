import urllib.request

def fetch_url(url):
    response = urllib.request.urlopen(url)
    return response.read()


print(fetch_url("https://google.com"))