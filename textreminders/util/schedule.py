DC_STATIONS = {
    'Farragut North': 'A02',
    'Rockville': 'A14',
    'Tenleytown-Au': 'A07',
    'Tenleytown': 'A07',                        # alias
    'American University': 'A07',               # alias
    'Au': 'A07',                                # alias
    'Brookland-Cua': 'B05',
    'Noma-Gallaudet U': 'B35',
    'Woodley Park-Zoo/Adams Morgan': 'A04',
    'Bethesda': 'A09',
    'Metro Center': 'A01',
    'Rhode Island Ave-Brentwood': 'B04',
    'Glenmont': 'B11',
    'Dupont Circle': 'A03',
    'Cleveland Park': 'A05',
    'Forest Glen': 'B09',
    'Van Ness-Udc': 'A06',
    'Fort Totten': 'B06',
    'Takoma': 'B07',
    'Twinbrook': 'A13',
    'Silver Spring': 'B08',
    'Shady Grove': 'A15',
    'Grosvenor-Strathmore': 'A11',
    'Grosvenor': 'A11',                         # alias
    'White Flint': 'A12',
    'Wheaton': 'B10',
    'Gallery Pl-Chinatown': 'B01',
    'Gallery Place': 'B01',                     # alias
    'Union Station': 'B03',
    'Union': 'B03',                             # alias
    'Judiciary Square': 'B02',
    'Friendship Heights': 'A08',
    'Medical Center': 'A10',
    'Mt Vernon Sq 7th St-Convention Center': 'E01',
    'Huntington': 'C15',
    'Georgia Ave-Petworth': 'E05',
    'Shaw-Howard U': 'E02',
    'Pentagon': 'C07',
    'Eisenhower Avenue': 'C14',
    'Ronald Reagan Washington National Airport': 'C10',
    'Ronald Reagan': 'C10',                     # alias
    'Braddock Road': 'C12',
    'Crystal City': 'C09',
    'Archives-Navy Memorial-Penn Quarter': 'F02',
    "L'Enfant Plaza": 'F03',
    'Pentagon City': 'C08',
    'U Street/African-Amer Civil War Memorial/Cardozo': 'E03',
    'King St-Old Town': 'C13',
    "Prince George's Plaza": 'E08',
    'Congress Heights': 'F07',
    'West Hyattsville': 'E07',
    'College Park-U Of Md': 'E09',
    'College Park': 'E09',                      # alias
    'Navy Yard-Ballpark': 'F05',
    'Greenbelt': 'E10',
    'Naylor Road': 'F09',
    'Waterfront': 'F04',
    'Columbia Heights': 'E04',
    'Suitland': 'F10',
    'Anacostia': 'F06',
    'Branch Ave': 'F11',
    'Southern Avenue': 'F08',
    'Van Dorn Street': 'J02',
    'Arlington Cemetery': 'C06',
    'Potomac Ave': 'D07',
    'Addison Road-Seat Pleasant': 'G03',
    'Capitol Heights': 'G02',
    'Federal Triangle': 'D01',
    'Rosslyn': 'C05',
    'Capitol South': 'D05',
    'Largo Town Center': 'G05',
    'Eastern Market': 'D06',
    'Benning Road': 'G01',
    'Smithsonian': 'D02',
    'Federal Center SW': 'D04',
    'Federal Center': 'D04',                    # alias
    'Stadium-Armory': 'D08',
    'McPherson Square': 'C02',
    'Franconia-Springfield': 'J03',
    'Farragut West': 'C03',
    'Foggy Bottom-Gwu': 'C04',
    'Morgan Boulevard': 'G04',
    'Vienna/Fairfax-Gmu': 'K08',
    'Court House': 'K01',
    'Ballston-MU': 'K04',
    'New Carrollton': 'D13',
    'Landover': 'D12',
    'Dunn Loring-Merrifield': 'K07',
    'Virginia Square-Gmu': 'K03',
    'West Falls Church-Vt/Uva': 'K06',
    'Clarendon': 'K02',
    'East Falls Church': 'K05',
    'Minnesota Ave': 'D09',
    'Deanwood': 'D10',
    'Cheverly': 'D11',
    'Spring Hill': 'N04',
    'McLean': 'N01',
    'Wiehle-Reston East': 'N06',
    'Tysons Corner': 'N02',
    'Greensboro': 'N03'
}

DC_TRAINS = {
    'red': 'RD',
    'yellow': 'YL',
    'green': 'GR',
    'blue': 'BL',
    'orange': 'OR',
    'silver': 'SV'
}

DC_TRAIN_STOPS = {
    'red': ['Shady Grove', 'Rockville', 'Twinbrook', 'White Flint', 'Grosvenor-Strathmore', 'Medical Center',
            'Bethesda', 'Friendship-Heights', 'Tenleytown-Au', 'Van Ness-Udc', 'Cleveland Park', 'Woodley Park',
            'Dupont Circle', 'Farragut North', 'Metro Center', 'Gallery Place', 'Judiciary Square',
            'Union Station', 'Noma-Gallaudet U', 'Rhode Island Avenue-Brentwood', 'Brookland-Cua', 'Fort Totten',
            'Takoma', 'Silver Spring', 'Forest Glen', 'Wheaton', 'Glenmont'],
    'yellow': [],
    'green': ['College Park-U Of Md'],
    'blue': [],
    'orange': [],
    'silver': []
}

DC_LIVE_TRAIN_URL = 'https://www.wmata.com/js/nexttrain/nexttrain.html#'

DENVER_TRAIN_DIRECTIONS = {
    'A': ['EB', 'WB'],
    'B': ['EB', 'WB'],
    'C': ['NB', 'SB'],
    'D': ['NB', 'SB'],
    'E': ['NB', 'SB'],
    'F': ['NB', 'SB'],
    'H': ['NB', 'SB'],
    'R': ['NB', 'SB'],
    'W': ['EB', 'WB']
}

DENVER_TRAIN_STOPS = {
    'A': ['Denver Airport', '61st & Pena', '40th Ave & Airport Blvd-Gateway Park',
          'Peoria', 'Central Park', '40th & Colorado', '38th & Blake', 'Union'],
    'B': ['Westminster', 'Union'],
    'C': ['Union', 'Pepsi Center - Elitch Gardens', 'Sports Authority Field at Mile High',
          'Auraria West', '10th & Osage', 'Alameda', 'I-25 & Broadway', 'Evans',
          'Englewood', 'Oxford', 'Littleton Downtown', 'Littleton Mineral'],
    'D': ['Littleton Mineral', 'Littleton Downtown', 'Oxford', 'Englewood', 'Evans', 'I-25 & Broadway', 'Alameda',
          '10th & Osage', 'Colfax at Auraria', 'Theatre District - Convention Center', '16th & California',
          '18th & California', '20th & Welton', '25th & Welton', '27th & Welton', '30th & Downing'],
    'E': ['Lincoln', 'County Line', 'Dry Creek', 'Arapahoe at Village Center', 'Orchard', 'Belleview', 'Southmoor',
          'Yale', 'Colorado', 'University of Denver', 'Louisiana - Pearl', 'I-25 & Broadway', 'Alameda', '10th & Osage',
          'Auraria West', 'Sports Authority Field at Mile High', 'Pepsi Center - Elitch Gardens', 'Union'],
    'F': ['Lincoln', 'County Line', 'Dry Creek', 'Arapahoe at Village Center', 'Orchard', 'Belleview', 'Southmoor',
          'Yale', 'Colorado', 'University of Denver', 'Louisiana - Pearl', 'I-25 & Broadway', 'Alameda', '10th & Osage',
          'Colfax at Auraria', 'Theatre District - Convention Center', '16th & California', '18th & California'],
    'H': ['Florida', 'Iliff', 'Nine Mile', 'Dayton', 'Southmoor', 'Yale', 'Colorado', 'University of Denver',
          'Louisiana - Pearl', 'I-25 & Broadway', 'Alameda', '10th & Osage', 'Colfax at Auraria',
          'Theatre District - Convention Center', '16th & California', '18th & California'],
    'R': ['Lincoln', 'County Line', 'Dry Creek', 'Arapahoe at Village Center', 'Orchard', 'Belleview', 'Dayton',
          'Nine Mile', 'Iliff', 'Florida', 'Aurora Metro Center Stn', '2nd & Abilene',
          '13th Avenue', 'Colfax', 'Fitzsimons', 'Peoria'],
    'W': ['Jefferson County Government Center - Golden', 'Red Rocks College', 'Federal Center', 'Oak', 'Garrison',
          'Lakewood-Wadsworth', 'Lamar', 'Sheridan', 'Perry', 'Knox', 'Decatur - Federal', 'Auraria West',
          'Sports Authority Field at Mile High', 'Pepsi Center - Elitch Gardens', 'Union']
}

STOPS = {
    'Denver': DENVER_TRAIN_STOPS,
    'DC': DC_TRAIN_STOPS
}