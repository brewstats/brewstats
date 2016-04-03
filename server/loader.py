import json
import user

with open('checkin-report_03_05_16.json') as data_file:
    parsedUser = user.User(json.load(data_file))

output = {
    'totalCheckins': parsedUser.totalCheckins,
    'ratingBins': parsedUser.ratingBins,
    'dayBins': parsedUser.dayBins,
    'hourBins': parsedUser.hourBins,
    'countryBins': parsedUser.countryBins,
    'usStateBins': parsedUser.usStateBins,
    'beerStyleBins': parsedUser.beerStyleBins,
    'venueNameBins': parsedUser.venueNameBins,
    'venueStateBins': parsedUser.venueStateBins,
    'venueCityBins': parsedUser.venueCityBins,
    'checkinRatings': parsedUser.checkinRatings,
    'epochCheckinDates': parsedUser.epochCheckinDates,
    'abvBins': parsedUser.abvBins
}

with open('checkin-report-summary.json', 'w') as f:
    json.dump(output, f)
