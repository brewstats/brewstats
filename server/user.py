import datetime
from collections import Counter


class User(object):

    def __init__(self, checkins):
        # Raw Data
        self.checkinData = checkins

        # Summary Counts
        self.totalCheckins = self.ReturnTotalCheckins()

        # Processed raw data
        self.checkinRatings = self.ReturnCheckinRatings()
        self.tupleCheckinDates = self.ReturnTupleCheckinDates()
        self.readableCheckinDates = self.ReturnReadableCheckinDates()
        self.epochCheckinDates = self.ReturnEpochCheckinDates()
        self.abvValues = self.ReturnABVValues()

        # Binned data
        self.ratingBins = self.BuildRatingBins()
        self.dayBins = self.BuildDayBins()
        self.hourBins = self.BuildHourBins()
        self.countryBins = self.BuildBreweryCountryBins()
        self.usStateBins = self.BuildUSStateBins()
        self.beerStyleBins = self.BuildBeerStyleBins()
        self.venueNameBins = self.BuildVenueNameBins()
        self.venueStateBins = self.BuildVenueStateBins()
        self.venueCityBins = self.BuildVenueCityBins()
        self.

    # Processed Raw Data
    def ReturnCheckinRatings(self):
        """Returns all checkin ratings as list of floats."""
        return [float(checkin['rating_score']) for checkin in self.checkinData if checkin['rating_score'] is not '']

    def ReturnABVValues(self):
        """Returns all checkin ABV values as list of floats."""
        return [float(checkin['beer_abv']) for checkin in self.checkinData if checkin['beer_abv'] is not '']

    def ReturnReadableCheckinDates(self):
        """Returns all checkin dates as list of human-readable strings."""
        return [checkin['created_at'] for checkin in self.checkinData]

    def ReturnTupleCheckinDates(self):
        """Returns all checkin dates as list of datetime parsable tuples."""
        return [datetime.datetime.strptime(checkin['created_at'], "%Y-%m-%d %H:%M:%S") for checkin in self.checkinData]

    def ReturnEpochCheckinDates(self):
        """Returns all checkin dates as list of UNIX epoch ints."""
        return [int(checkin.timestamp()) for checkin in self.tupleCheckinDates]

    # Summary Data
    def ReturnTotalCheckins(self):
        """Returns total number of checkins as int."""
        return len(self.checkinData)

    def ReturnFirstBeer(self):
        """Returns entire first checkin dict object."""
        return self.checkinData[0]

    # Binned Data
    def BuildRatingBins(self):
        """Returns count of all rating instances as dict."""
        return Counter([checkin['rating_score'] for checkin in self.checkinData])

    def BuildABVBins(self):
        """Returns count of all ABV instances as dict, rounded to nearest 0.5."""
        return Counter([round(checkin / .5) * .5 for checkin in self.abvValues])

    def BuildDayBins(self):
        """Returns count of weekdays each checkin was logged as dict."""
        return Counter([datetime.datetime.strftime(checkin, "%a") for checkin in self.tupleCheckinDates])

    def BuildHourBins(self):
        """Returns count of hour each checkin was logged as dict."""
        return Counter([datetime.datetime.strftime(checkin, "%H") for checkin in self.tupleCheckinDates])

    def BuildBreweryCountryBins(self):
        """Returns count of brewery countries as dict."""
        return Counter([checkin['brewery_country'] for checkin in self.checkinData])

    def BuildUSStateBins(self):
        """Returns count of brewery US States as dict."""
        return Counter([checkin['brewery_state'] for checkin in self.checkinData if 'United States' in checkin['brewery_country']])

    def BuildBeerStyleBins(self):
        """Returns count of unique beer styles as dict."""
        return Counter([checkin['beer_type'] for checkin in self.checkinData])

    def BuildVenueNameBins(self):
        """Returns count of names of venues checked in at as dict."""
        return Counter([checkin['venue_name'] for checkin in self.checkinData])

    def BuildVenueStateBins(self):
        """Returns count of states of venues checked in at as dict."""
        return Counter([checkin['venue_state'] for checkin in self.checkinData])

    def BuildVenueCityBins(self):
        """Returns count of cities of venues checked in at as dict."""
        return Counter([checkin['venue_city'] for checkin in self.checkinData])
