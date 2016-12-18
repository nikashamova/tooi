import http.client
import json
import urllib


def search_in_bing(this_is_what_i_search):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'HERE IS KEY',
    }

    params = urllib.parse.urlencode({
        'q': this_is_what_i_search,
        'mkt': 'en-us',
        'safesearch': 'Moderate',
    })

    try:
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        data_json = json.loads(data)
        total_number_of_results = data_json["webPages"]["totalEstimatedMatches"]
        conn.close()
        return total_number_of_results
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def main():
    this_is_what_i_search = "wait for"
    number = search_in_bing(this_is_what_i_search)
    print(number)


main()
####################################
