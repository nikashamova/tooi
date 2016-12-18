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
    # pprint.pprint(res)
    return res['searchInformation']['totalResults']


def main():
    result = search_total_count('wait for')
    print(result)


main()


# 135000000
# 135000000
# 116000000
