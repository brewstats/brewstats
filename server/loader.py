import json
import user
import pprint

with open('checkin-report_03_05_16.json') as data_file:
    parsedUser = user.User(json.load(data_file))

pp = pprint.PrettyPrinter()
pp.pprint(parsedUser.BuildBeerStyleBins())
