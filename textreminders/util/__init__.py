import re, json
import http
from collections import defaultdict


class ResponseHandler(object):
    """
    Handles incoming sms and returns a xml object
    """

    def __init__(self, body):
        """

        :param body: unicode body of incoming text message
        """
        self.body = body  # original body of incoming text message
        self.city = None  # name of city
        self.train = None  # utility name of train
        self.station = None  # utility name of station
        self.directions = set()  # e.g. {'NB', 'SB'}
        self.time_left = defaultdict(list)   # according to self.directions: {'NB': [5, 8], 'SB': [2, 10]}

        self.error = None  # error codes

        self.parse_body()

    def parse_body(self):
        """
        Parses the body and populates the instance variables
        :return: None
        """
        import textreminders.util.schedule as schedule
        from textreminders.util.settings import WMATA_KEY
        if 'denver' in self.body.lower():
            self.city = 'Denver'
            try:
                self.train = re.findall('[EF]', self.body)[0]
                self.station = re.findall(self.train + ' (.*)$', self.body)[0]
            except IndexError:
                self.error = 'FORMAT_ERROR'

            self.directions = list(schedule.TRAINS[self.city][self.train][self.station].keys())
            # TODO: get time left

        elif 'dc' in self.body.lower():
            self.city = 'DC'
            regex = '(red|silver|orange|yellow|blue|green) (.*)$'
            parsed = re.findall(regex, self.body.lower())
            try:
                friendly_train, friendly_station = parsed[0][0], parsed[0][1]
                self.train = schedule.DC_TRAINS[friendly_train]
                self.station = schedule.DC_STATIONS[friendly_station.title()]
            except IndexError:
                self.error = 'FORMAT_ERROR'
                return

            headers = {
                # Request headers
                'api_key': WMATA_KEY,
            }

            params = ''

            try:
                conn = http.client.HTTPSConnection('api.wmata.com')
                conn.request('GET',
                             '/StationPrediction.svc/json/GetPrediction/{}?{}'.format(self.station, params),
                             '{body}',
                             headers)
                response = conn.getresponse()
                data = response.read().decode('utf-8')
                json_data = json.loads(data)
                for train in json_data['Trains']:
                    if train['Line'] == self.train:
                        self.directions.append(train['Destination'])
                        self.time_left[train['Destination']].append(train['Min'])
                if not self.directions:
                    self.error = 'NO_TRAINS_ERROR'
                conn.close()
            except Exception as e:
                self.error = 'API_ERROR'
                return

    def create_response(self):
        """
        Uses the instance variables to create the xml response
        :return: XML object
        """
        twiml = '<Response><Message>'
        if self.error:

            if self.error == 'FORMAT_ERROR':
                twiml += 'Invalid Format: Send a text with the following format:\n'
                twiml += '\'DC red rockville\' or \'Denver E Dry Creek\''
            elif self.error == 'NO_TRAINS_ERROR':
                twiml += 'Unfortunately, no trains are listed as coming :('
            elif self.error == 'API_ERROR':
                twiml += 'There was an API failure :( Check back in 10 minutes!'

            twiml += '</Message></Response>'

            return twiml

        for direction in self.directions:
            twiml += 'Direction {}:'.format(direction)
            twiml += ', '.join([str(x) for x in self.time_left[direction]])
            twiml += '\n'
        twiml += '</Message></Response>'

        return twiml
