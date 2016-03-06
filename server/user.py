import datetime
from collections import Counter

class User(object):

    def __init__(self, checkins):
        # Raw Data
        self.checkinData = checkins

        # Summary Counts
        self.totalCheckins = self.ReturnTotalCheckins()
        self.checkinRatings = self.ReturnCheckinRatings()
        self.tupleCheckinDates = self.ReturnTupleCheckinDates()
        self.readableCheckinDates = self.ReturnReadableCheckinDates()
        self.epochCheckinDates = self.ReturnEpochCheckinDates()

        # Binned data
        self.rankingHistogram = self.BuildRankingHistogram()
        self.dayBins = self.BuildDayBins()
        self.hourBins = self.BuildHourBins()
        self.countryBins = self.BuildBreweryCountryBins()
        self.usStateBins = self.BuildUSStateBins()
        self.beerStyleBins = self.BuildBeerStyleBins()
        self.venueNameBins = self.BuildVenueNameBins()
        self.venueStateBins = self.BuildVenueStateBins()
        self.venueCityBins = self.BuildVenueCityBins()

    def ReturnTotalCheckins(self):
        return len(self.checkinData)

    def ReturnCheckinRatings(self):
        return [float(checkin['rating_score']) for checkin in self.checkinData if checkin['rating_score'] is not '']

    def ReturnReadableCheckinDates(self):
        return [checkin['created_at'] for checkin in self.checkinData]

    def ReturnTupleCheckinDates(self):
        return [datetime.datetime.strptime(checkin['created_at'], "%Y-%m-%d %H:%M:%S") for checkin in self.checkinData]

    def ReturnEpochCheckinDates(self):
        return [int(checkin.timestamp()) for checkin in self.tupleCheckinDates]

    def BuildRankingHistogram(self):
        return Counter([checkin['rating_score'] for checkin in self.checkinData])

    def BuildABVBins(self):
        return Counter([round(float(checkin['beer_abv']) / .5) * .5 for checkin in self.checkinData])

    def BuildDayBins(self):
        return Counter([datetime.datetime.strftime(checkin, "%a") for checkin in self.tupleCheckinDates])

    def BuildHourBins(self):
        return Counter([datetime.datetime.strftime(checkin, "%H") for checkin in self.tupleCheckinDates])

    def BuildBreweryCountryBins(self):
        return Counter([checkin['brewery_country'] for checkin in self.checkinData])

    def BuildUSStateBins(self):
        return Counter([checkin['brewery_state'] for checkin in self.checkinData if 'United States' in checkin['brewery_country']])

    def BuildBeerStyleBins(self):
        return Counter([checkin['beer_type'] for checkin in self.checkinData])

    def BuildVenueNameBins(self):
        return Counter([checkin['venue_name'] for checkin in self.checkinData])

    def BuildVenueStateBins(self):
        return Counter([checkin['venue_state'] for checkin in self.checkinData])

    def BuildVenueCityBins(self):
        return Counter([checkin['venue_city'] for checkin in self.checkinData])
