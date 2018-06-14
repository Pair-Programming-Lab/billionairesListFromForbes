import urllib.request, json
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

    filename = "blist.csv"

    with open(filename, "w") as f:
        headers = "Rank, Name, Company, Worth\n"
        f.write(headers)

        for d in new_list:
            rank = d['rank']
            name = d['name']
            company = d['company'] if 'company' in d else 'None'
            worth = d['worth']
            f.write("{}, {}, {}, {}\n".format(
                rank, name, company, worth
            ))
