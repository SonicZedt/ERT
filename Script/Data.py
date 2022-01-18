import pickle
import requests

var = 'asdjhauisjh'
url = ''

def GetOnline():
    requests.get(url, allow_redirects=True)
    return url.rsplit('/', 1)[1]

def Create(fileName):
    with open(fileName, 'wb') as file:
        pickle.dump(var, file)

def Read(fileName):
    with open(fileName, 'rb') as file:
        print(pickle.load(file))

Create('License.ZEDT')