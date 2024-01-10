import urllib

def fetch_url(url):
    response = urllib.urlopen(url)
    return response.read()

print fetch_url("https://google.com")


