Coloradosport=['Nuggets','Broncos','avalanche','rapids']
Californiasport=['Los Angeles Lakers (NBA)', 'Los Angeles Dodgers (MLB)', 'San Francisco 49ers (NFL)', 'San Francisco Giants (MLB)', 'Golden State Warriors (NBA)', 'Los Angeles Rams (NFL)', 'Los Angeles Clippers (NBA)', 'Anaheim Ducks (NHL)', 'San Jose Sharks (NHL)', 'Los Angeles Kings (NHL)', 'Los Angeles Chargers (NFL)']
Connecticutsport=['UConn Huskies (NCAA)', 'Hartford Yard Goats (MiLB)', 'Bridgeport Islanders (AHL)']
Delawaresport=['Wilmington Blue Rocks (MiLB)']
Georgiasport=['Atlanta Falcons (NFL)', 'Atlanta Braves (MLB)', 'Atlanta Hawks (NBA)', 'Georgia Bulldogs (NCAA)', 'Georgia Tech Yellow Jackets (NCAA)', 'Atlanta United FC (MLS)']
Illinoisport=['Chicago Bears (NFL)', 'Chicago Cubs (MLB)', 'Chicago Bulls (NBA)', 'Chicago White Sox (MLB)', 'Chicago Blackhawks (NHL)', 'Chicago Fire FC (MLS)']
Indianasport=['Indianapolis Colts (NFL)', 'Indiana Pacers (NBA)', 'Indianapolis Indians (MiLB)', 'Indiana Hoosiers (NCAA)', 'Purdue Boilermakers (NCAA)']
Iowapsort=['Iowa Hawkeyes (NCAA)']
Kansasport=['Kansas City Chiefs (NFL)', 'Kansas City Royals (MLB)']
Kentuckysport=['Kentucky Wildcats (NCAA)', 'Louisville Cardinals (NCAA)']
Louisianasport=['New Orleans Saints (NFL)', 'New Orleans Pelicans (NBA)', 'LSU Tigers (NCAA)']
Marylandsport=['Baltimore Ravens (NFL)', 'Baltimore Orioles (MLB)', 'Washington Wizards (NBA)', 'Washington Capitals (NHL)', 'Washington Football Team (NFL)', 'Maryland Terrapins (NCAA)', 'Navy Midshipmen (NCAA)']
Massachusettssport=['New England Patriots (NFL)', 'Boston Red Sox (MLB)', 'Boston Celtics (NBA)', 'Boston Bruins (NHL)', 'New England Revolution (MLS)']
Michigansport=['Detroit Lions (NFL)', 'Detroit Tigers (MLB)', 'Detroit Pistons (NBA)', 'Detroit Red Wings (NHL)', 'Michigan Wolverines (NCAA)', 'Michigan State Spartans (NCAA)']
Minnesotasport=['Minnesota Vikings (NFL)', 'Minnesota Twins (MLB)', 'Minnesota Timberwolves (NBA)', 'Minnesota Wild (NHL)', 'Minnesota Golden Gophers (NCAA)']
Mississippiasport=['Ole Miss Rebels (NCAA)', 'Mississippi State Bulldogs (NCAA)']
Missourisport=['Kansas City Chiefs (NFL)', 'St. Louis Cardinals (MLB)', 'St. Louis Blues (NHL)', 'St. Louis Cardinals (MLB)', 'Missouri Tigers (NCAA)', 'Saint Louis Billikens (NCAA)']
Nebraskasport=['Omaha Storm Chasers (MiLB)', 'Nebraska Cornhuskers (NCAA)']
Nevadasport=['Las Vegas Raiders (NFL)', 'Vegas Golden Knights (NHL)']
NewJerseysport=['New York Giants (NFL)', 'New York Jets (NFL)', 'New Jersey Devils (NHL)']
NewYorksport=['New York Yankees (MLB)', 'New York Mets (MLB)', 'New York Knicks (NBA)', 'Buffalo Bills (NFL)', 'New York Rangers (NHL)', 'Brooklyn Nets (NBA)', 'New York Islanders (NHL)', 'Buffalo Sabres (NHL)', 'New York Red Bulls (MLS)', 'New York City FC (MLS)']
NorthCarolinasport=['Carolina Panthers (NFL)', 'Carolina Hurricanes (NHL)', 'Charlotte Hornets (NBA)', 'North Carolina Tar Heels (NCAA)', 'Duke Blue Devils (NCAA)', 'North Carolina State Wolfpack (NCAA)']
Ohiosport=['Cleveland Browns (NFL)', 'Cincinnati Reds (MLB)', 'Cleveland Cavaliers (NBA)', 'Columbus Blue Jackets (NHL)', 'Ohio State Buckeyes (NCAA)', 'Cincinnati Bengals (NFL)', 'Cleveland Guardians (MLB)']
Oklahomasport=['Oklahoma City Thunder (NBA)', 'Oklahoma Sooners (NCAA)', 'Oklahoma State Cowboys (NCAA)']
Oregonsport=['Portland Trail Blazers (NBA)', 'Portland Timbers (MLS)', 'Oregon Ducks (NCAA)', 'Oregon State Beavers (NCAA)']
Pennsylvaniasport=['Philadelphia Eagles (NFL)', 'Pittsburgh Steelers (NFL)', 'Philadelphia Phillies (MLB)', 'Pittsburgh Pirates (MLB)', 'Philadelphia 76ers (NBA)', 'Pittsburgh Penguins (NHL)', 'Philadelphia Union (MLS)', 'Penn State Nittany Lions (NCAA)', 'Pittsburgh Panthers (NCAA)']
SouthCarolinasport=['Carolina Panthers (NFL)', 'South Carolina Gamecocks (NCAA)', 'Clemson Tigers (NCAA)', 'Charleston RiverDogs (MiLB)']
Tennesseesport=['Tennessee Titans (NFL)', 'Nashville Predators (NHL)', 'Memphis Grizzlies (NBA)', 'Tennessee Volunteers (NCAA)', 'Vanderbilt Commodores (NCAA)', 'Nashville SC (MLS)', 'Memphis Tigers (NCAA)']
Texassport=['Dallas Cowboys (NFL)', 'Houston Astros (MLB)', 'Houston Rockets (NBA)', 'Dallas Mavericks (NBA)', 'Texas Longhorns (NCAA)', 'Texas A&M Aggies (NCAA)', 'San Antonio Spurs (NBA)', 'Texas Rangers (MLB)', 'Dallas Stars (NHL)', 'Houston Texans (NFL)', 'Houston Dynamo (MLS)', 'Texas Tech Red Raiders (NCAA)', 'Baylor Bears (NCAA)', 'Texas Rangers (MLB)', 'Houston Dynamo (MLS)']
Utahsport=['Utah Jazz (NBA)', 'Real Salt Lake (MLS)', 'BYU Cougars (NCAA)', 'Utah Utes (NCAA)']
Washingtonsport=['Redskins football team (NFL)', 'Washington Nationals (MLB)', 'Washington Capitals (NHL)', 'Washington Wizards (NBA)', 'Virginia Tech Hokies (NCAA)', 'Virginia Cavaliers (NCAA)', 'George Mason Patriots (NCAA)', 'Richmond Spiders (NCAA)']
WashingtonnotDC=['Seattle Seahawks (NFL)', 'Seattle Mariners (MLB)', 'Seattle Sounders FC (MLS)', 'Seattle Storm (WNBA)', 'Washington Huskies (NCAA)', 'Washington State Cougars (NCAA)', 'Spokane Indians (MiLB)', 'Tacoma Rainiers (MiLB)']
Westvirginiasport=['West Virginia Mountaineers (NCAA)']
Wisconsinsport=['Green Bay Packers (NFL)', 'Milwaukee Brewers (MLB)', 'Milwaukee Bucks (NBA)', 'Wisconsin Badgers (NCAA)', 'Marquette Golden Eagles (NCAA)']

while True:
    print ('welcome to sports team look up')
    userinput = input('Please enter state abbreviation')
    if userinput ==("CO"):
        for team in Coloradosport:
            print(team)
    
    if userinput ==("CA"):
        for team in Californiasport:
            print(team)
    if userinput ==("USA"):
        break
    if userinput ==("CT"):
        for team in Connecticutsport:
            print(team)
    if userinput ==("CT"):
        for team in Connecticutsport:
            print(team)
    if userinput ==("DE"):
        for team in Delawaresport:
            print(team)    
    if userinput ==("GA"):
        for team in Georgiasport:
            print(team) 
    if userinput ==("IL"):
        for team in Illinoisport:
            print(team)
    if userinput ==("IN"):
        for team in Indianasport:
            print(team)
    if userinput ==("IA"):
        for team in Iowapsort:
            print(team)
    if userinput ==("KS"):
        for team in Kansasport:
            print(team)
    if userinput ==("KY"):
        for team in Kentuckysport:
            print(team)
    if userinput ==("KY"):
        for team in Kentuckysport:
            print(team)
    if userinput ==("LA"):
        for team in Louisianasport:
            print(team)
    if userinput ==("LA"):
        for team in Louisianasport:
            print(team)
    if userinput ==("MD"):
        for team in Marylandsport:
            print(team)        
    if userinput ==("MA"):
        for team in Massachusettssport:
            print(team)
    if userinput ==("MI"):
        for team in Michigansport:
            print(team)
    if userinput ==("MN"):
        for team in Minnesotasport:
            print(team)
    if userinput ==("MS"):
        for team in Mississippiasport:
            print(team)
    if userinput ==("MO"):
        for team in Missourisport:
            print(team)
    if userinput ==("NE"):
        for team in Nebraskasport:
            print(team)
    if userinput ==("NV"):
        for team in Nevadasport:
            print(team)
    if userinput ==("NJ"):
        for team in NewJerseysport:
            print(team)
    if userinput ==("NY"):
        for team in NewYorksport:
            print(team)
    if userinput ==("NC"):
        for team in NorthCarolinasport:
            print(team)
    if userinput ==("OH"):
        for team in Ohiosport:
            print(team)
    if userinput ==("OK"):
        for team in Oklahomasport:
            print(team)
    if userinput ==("OR"):
        for team in Oregonsport:
            print(team)
    if userinput ==("PA"):
        for team in Pennsylvaniasport:
            print(team)
    if userinput ==("SC"):
        for team in SouthCarolinasport:
            print(team)
    if userinput ==("TN"):
        for team in Tennesseesport:
            print(team)
    if userinput ==("TX"):
        for team in Texassport:
            print(team)
    if userinput ==("UT"):
        for team in Utahsport:
            print(team)
    if userinput ==("DC"):
        for team in Washingtonsport:
            print(team)
    if userinput ==("WA"):
        for team in WashingtonnotDC:
            print(team)
    if userinput ==("WV"):
        for team in Westvirginiasport:
            print(team)
    if userinput ==("WI"):
        for team in Wisconsinsport:
            print(team)