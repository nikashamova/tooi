import json
import time
import urllib
from urllib.parse import urlencode
from urllib.request import urlopen

from googleapiclient.discovery import build

myDeveloperKey = "dev key"
myCx = 'cx'


def search_total_count(this_is_what_i_search):
    service = build("customsearch", "v1",
                    developerKey=myDeveloperKey)

    res = service.cse().list(
        q=this_is_what_i_search,
        cx=myCx,
    ).execute()
    return res['searchInformation']['totalResults']


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
    file = open("popular_pairs.txt", 'r')
    file_result = open("trans_result.txt", 'a+')
    i = 0
    while i < 100:
        i += 1
        line = file.readline()
        line.strip()
        print(line)
        count_of_results = search_total_count(line)
        print(count_of_results)
        file_result.write(line + ' ' + count_of_results + ' ')
        line = line.replace('\n', '')
        trans_result = glosbe_search(line)
        for translation in trans_result:
            try:
                file_result.write(translation + ', ')
            except UnicodeEncodeError:
                print('skip')
        file_result.write('\n')
        time.sleep(1)
        # i = 0
        # while i < 882:
        #     i += 1
        #     line = file.readline().strip()
        #     print(line)
        #     file_result.write(line + ' ')
        #     t_result = glosbe_search(line)
        #     for j in t_result:
        #         try:
        #             file_result.write(j + ', ')
        #         except UnicodeEncodeError:
        #             print("ok")
        #     print(t_result)
        #     file_result.write('\n')
        #     time.sleep(1)
        file.close()
        file_result.close()


main()
