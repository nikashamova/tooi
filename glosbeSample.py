import json
import urllib
from pprint import pprint
from urllib.parse import urlencode
from urllib.request import urlopen


def glosbe_request(what_to_search):
    glosbe_url = 'https://glosbe.com/gapi/translate'
    query_params = {
        'from': 'eng',
        'dest': 'rus',
        'format': 'json',
        'phrase': what_to_search
    }
    query_url = urllib.parse.urlencode(query_params)
    response = urllib.request.urlopen(glosbe_url + '?' + query_url)
    return response.read()


def glosbe_search(what_to_search):
    result = []
    theJSON = json.loads(glosbe_request(what_to_search).decode('utf-8'))
    pprint(theJSON["tuc"])
    for i in theJSON["tuc"]:
        if 'phrase' in i:
            result.append(i['phrase']['text'])
            if 'meanings' in i:
                for j in i['meanings']:
                    if ('language' in j) and (j['language'] == 'ru') and ('text' in j):
                        result.append(j['text'])
    print(result)
    return result


def main():
    file = open("trans.txt", 'w+')
    result = glosbe_search("come by")
    for i in result:
        try:
            file.write(i + ', ')
        except UnicodeEncodeError:
            print("skip")


main()
