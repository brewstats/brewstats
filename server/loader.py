import json
import user

with open('checkin-report_03_05_16.json') as data_file:
    parsedUser = user.User(json.load(data_file))
