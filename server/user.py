import datetime


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
        ratingBins = {'': 0, '0': 0, '0.25': 0, '0.5': 0, '0.75': 0, '1': 0, '1.25': 0,
                      '1.5': 0, '1.75': 0, '2': 0, '2.25': 0, '2.5': 0, '2.75': 0, '3': 0,
                      '3.25': 0, '3.5': 0, '3.75': 0, '4': 0, '4.25': 0, '4.5': 0, '4.75': 0, '5': 0, 'error': 0}

        for checkin in self.checkinData:
            try:
                ratingBins[checkin['rating_score']] += 1
            except:
                ratingBins['error'] += 1
                print("Could not grab rating!")

        return ratingBins

    def BuildDayBins(self):
        dayBins = {'Mon': 0, 'Tue': 0, 'Wed': 0,
                   'Thu': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}

        for checkin in self.tupleCheckinDates:
            dayBins[datetime.datetime.strftime(checkin, "%a")] += 1

        return dayBins

    def BuildHourBins(self):
        hourBins = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0,
                    '08': 0, '09': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
                    '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}

        for checkin in self.tupleCheckinDates:
            hourBins[datetime.datetime.strftime(checkin, "%H")] += 1

        return hourBins
