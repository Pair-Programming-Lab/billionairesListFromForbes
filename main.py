import urllib.request
import json
from operator import itemgetter
import sys


def mysortfunc(key):
    if 'rank' in key:
        return key['rank']
    return 0


with urllib.request.urlopen("https://www.forbes.com/ajax/list/data?year=2018&uri=billionaires&type=person") as url:
    data = json.loads(url.read().decode())
    new_list = []
    for d in data:
        if 'rank' in d:
            new_list.append(d)
            new_list.sort(key=itemgetter('rank'))

    ########################## get specific field data ###############################

    filename = "blist1.csv"

    with open(filename, "w") as f:
        headers = "Rank, Name, Worth, Source\n"
        f.write(headers)

        for d in new_list:
            rank = d['rank']
            name = d['name']
            worth = d['worth']
            source = d['source']
            f.write("{}, {}, {}, {}\n".format(
                rank, name, worth, source
            ))

    ########################## get all field data ###############################

    # get list of keys in a single object of the whole list
    keys = list(new_list[0].keys())
    # creating the table header for the csv file in comma separated fashion
    headers = ",".join(keys)
    headers += "\n"

    filename = "blist2.csv"
    with open(filename, "w") as f:
        f.write(headers)
        for d in new_list:
            # get list of values in a single object of the whole list
            values = list(d.values())
            # creating the table row data for the csv file in comma separated fashion
            rowData = ",".join(str(e) for e in values)
            rowData += "\n"
            f.write(rowData)

    print("done")

    # But problem is this url gives different type of data for different persons
