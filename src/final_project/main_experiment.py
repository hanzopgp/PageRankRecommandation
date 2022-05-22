from global_ import *

dataset = np.array([[{'201': 'Ed Wood (1994)', '551': 'James and the Giant Peach (1996)', '124': 'Rob Roy (1995)', '828': 'Platoon (1986)', '384': 'Dazed and Confused (1993)'},
        {'277': 'Shawshank Redemption, The (1994)', '2224': 'Fight Club (1999)', '659': 'Godfather, The (1972)', '507': 'Terminator 2: Judgment Day (1991)', '31': 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)'},
        {'9608': 'Gaga: Five Foot Two (2017)', '9208': 'The Brothers Grimsby (2016)', '4623': 'Interstate 60 (2002)', '6716': 'Happy-Go-Lucky (2008)', '7056': 'Hood of Horror (2006)'}],
       [{'6236': 'Talladega Nights: The Ballad of Ricky Bobby (2006)', '7137': 'Zombieland (2009)', '5294': 'Collateral (2004)', '7241': 'Shutter Island (2010)', '8045': 'Django Unchained (2012)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'9329': 'Sully (2016)', '569': 'True Crime (1996)', '5785': 'Because of Winn-Dixie (2005)', '4875': 'EuroTrip (2004)', '5139': 'Mitchell (1975)'}],
       [{'545': 'Courage Under Fire (1996)', '2278': 'Piranha (1978)', '1552': 'Rescuers, The (1977)', '4039': 'Galaxy of Terror (Quest) (1981)', '2140': 'Saturn 3 (1980)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'1015': 'Amityville Horror, The (1979)', '6857': 'Pride and Glory (2008)', '7497': 'Trip, The (2010)', '5130': 'Masterminds (1997)', '4326': 'Spellbound (2002)'}],
       [{'109': 'NeverEnding Story III, The (1994)', '818': 'Fish Called Wanda, A (1988)', '2013': 'Austin Powers: The Spy Who Shagged Me (1999)', '680': 'Philadelphia Story, The (1940)', '20': 'Get Shorty (1995)'},
        {'314': 'Forrest Gump (1994)', '277': 'Shawshank Redemption, The (1994)', '418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)', '97': 'Braveheart (1995)'},
        {'2945': 'Dr. T and the Women (2000)', '9643': 'Too Funny to Fail: The Life and Death of The Dana Carvey Show (2017)', '8966': 'Joe Dirt 2: Beautiful Loser (2015)', '6332': 'Déjà Vu (Deja Vu) (2006)', '1679': 'One Crazy Summer (1986)'}],
       [{'225': 'Little Women (1994)', '32': 'Babe (1995)', '315': 'Four Weddings and a Funeral (1994)', '35': 'Clueless (1995)', '52': 'Postman, The (Postino, Il) (1994)'},
        {'314': 'Forrest Gump (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'3016': 'Annie (1982)', '8138': 'Shaolin Temple (Shao Lin si) (1976)', '4078': 'Houseboat (1958)', '3638': 'Topkapi (1964)', '6564': 'Game Plan, The (2007)'}],
       [{'320': 'Jungle Book, The (1994)', '225': 'Little Women (1994)', '494': 'Little Big League (1994)', '152': 'Mallrats (1995)', '473': 'Sliver (1993)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '0': 'Toy Story (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)'},
        {'6124': 'Date Movie (2006)', '7710': 'Shame (2011)', '2575': 'Good Earth, The (1937)', '1931': 'True Crime (1999)', '7332': 'Back-up Plan, The (2010)'}],
       [{'2832': 'X-Men (2000)', '314': 'Forrest Gump (1994)', '3633': 'Lord of the Rings: The Fellowship of the Ring, The (2001)', '1904': 'Planet of the Apes (1968)', '3885': 'Road to Perdition (2002)'},
        {'257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '43': 'Seven (a.k.a. Se7en) (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)'},
        {'1120': "Vegas Vacation (National Lampoon's Las Vegas Vacation) (1997)", '642': 'Adventures of Pinocchio, The (1996)', '6614': 'Alvin and the Chipmunks (2007)', '1348': 'City of Angels (1998)', '4669': "Passion of Joan of Arc, The (Passion de Jeanne d'Arc, La) (1928)"}],
       [{'156': 'Net, The (1995)', '322': 'Lion King, The (1994)', '276': 'Santa Clause, The (1994)', '325': 'Mask, The (1994)', '202': 'French Kiss (1995)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)'},
        {'5365': 'Polar Express, The (2004)', '891': 'Thin Blue Line, The (1988)', '6925': 'Zeitgeist: Addendum (2008)', '8899': 'Star Trek Beyond (2016)', '104': 'Steal Big, Steal Little (1995)'}],
       [{'3352': 'Twins (1988)', '4082': 'Return to the Blue Lagoon (1991)', '190': 'Clerks (1994)', '3074': 'Making Mr. Right (1987)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'2840': "Mackenna's Gold (1969)", '3833': 'Enough (2002)', '687': 'It Happened One Night (1934)', '246': 'New York Cop (Nyû Yôku no koppu) (1993)', '3032': 'Coffy (1973)'}],
       [{'4858': '50 First Dates (2004)', '3826': 'About a Boy (2002)', '4791': 'Lord of the Rings: The Return of the King, The (2003)', '4136': 'Two Weeks Notice (2002)', '6056': 'Match Point (2005)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'6295': 'Guardian, The (2006)', '2551': '...And Justice for All (1979)', '3382': 'January Man, The (1989)', '1910': 'Earthquake (1974)', '7911': 'Ice Age 4: Continental Drift (2012)'}],
       [{'1198': 'Conspiracy Theory (1997)', '333': 'River Wild, The (1994)', '138': 'Die Hard: With a Vengeance (1995)', '253': 'Outbreak (1995)', '1205': 'Money Talks (1997)'},
        {'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'2406': 'Presidio, The (1988)', '8235': 'What If (2013)', '7661': 'Conan the Barbarian (2011)', '2266': 'Rosetta (1999)', '3474': '3 Ninjas (1992)'}],
       [{'1820': 'Karate Kid, Part II, The (1986)', '2727': 'Romeo and Juliet (1968)', '220': 'Junior (1994)', '1290': 'Titanic (1997)', '476': 'So I Married an Axe Murderer (1993)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'2637': 'American Psycho (2000)', '1965': 'Winslow Boy, The (1999)', '1755': 'Rugrats Movie, The (1998)', '4681': 'Hudson Hawk (1991)', '2693': 'Small Time Crooks (2000)'}],
       [{'899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '514': 'Pretty Woman (1990)', '1218': 'Seven Years in Tibet (1997)', '2836': 'What Lies Beneath (2000)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'8987': 'Madly in Love (1981)', '6674': 'Descent (2007)', '6571': 'Elizabeth: The Golden Age (2007)', '134': 'Crimson Tide (1995)', '5031': 'Tremors 3: Back to Perfection (2001)'}],
       [{'333': 'River Wild, The (1994)', '418': 'Jurassic Park (1993)', '297': 'While You Were Sleeping (1995)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '0': 'Toy Story (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)'},
        {'6432': 'Black Book (Zwartboek) (2006)', '5981': 'Frankenstein 90 (1984)', '4669': "Passion of Joan of Arc, The (Passion de Jeanne d'Arc, La) (1928)", '1146': 'Kissed (1996)', '2781': 'Assault on Precinct 13 (1976)'}],
       [{'6905': 'Gran Torino (2008)', '3456': 'Others, The (2001)', '7524': 'Adjustment Bureau, The (2011)', '7116': 'Cloudy with a Chance of Meatballs (2009)', '910': 'Star Wars: Episode VI - Return of the Jedi (1983)'},
        {'418': 'Jurassic Park (1993)', '97': 'Braveheart (1995)', '510': 'Silence of the Lambs, The (1991)', '46': 'Usual Suspects, The (1995)', '1182': 'Men in Black (a.k.a. MIB) (1997)'},
        {'5032': 'Notorious C.H.O. (2002)', '6370': 'Hitcher, The (2007)', '7014': 'Night at the Museum: Battle of the Smithsonian (2009)', '3977': 'Invincible (2001)', '7690': 'Three Outlaw Samurai (Sanbiki no samurai) (1964)'}],
       [{'1264': 'Sliding Doors (1998)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '278': 'Shallow Grave (1994)', '922': 'Full Metal Jacket (1987)', '1570': 'Jerk, The (1979)'},
        {'418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)', '97': 'Braveheart (1995)', '910': 'Star Wars: Episode VI - Return of the Jedi (1983)', '1182': 'Men in Black (a.k.a. MIB) (1997)'},
        {'1149': "Romy and Michele's High School Reunion (1997)", '7324': 'Shake Hands with the Devil (2007)', '1207': 'Kull the Conqueror (1997)', '3443': 'Chocolat (1988)', '7127': 'Cove, The (2009)'}],
       [{'2565': 'Double Indemnity (1944)', '928': 'Raging Bull (1980)', '4131': 'Lord of the Rings: The Two Towers, The (2002)', '474': 'Blade Runner (1982)', '1080': 'Beavis and Butt-Head Do America (1996)'},
        {'1182': 'Men in Black (a.k.a. MIB) (1997)', '31': 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)', '334': 'Speed (1994)', '862': 'Monty Python and the Holy Grail (1975)', '520': 'Fargo (1996)'},
        {'373': 'Cabin Boy (1994)', '3168': 'Under the Sand (2000)', '5314': 'Camera Buff (Amator) (1979)', '6379': "Smokin' Aces (2006)", '7991': '[REC]³ 3 Génesis (2012)'}],
       [{'5495': 'Hitch Hikers Guide to the Galaxy, The (1981)', '31': 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)', '1871': 'Payback (1999)', '968': 'Back to the Future (1985)', '4350': 'Bruce Almighty (2003)'},
        {'2144': 'American Beauty (1999)', '963': 'Groundhog Day (1993)', '123': 'Apollo 13 (1995)', '1978': 'Star Wars: Episode I - The Phantom Menace (1999)', '835': 'E.T. the Extra-Terrestrial (1982)'},
        {'8184': "World's End, The (2013)", '8335': 'Nymphomaniac: Volume I (2013)', '4016': 'Naqoyqatsi (2002)', '3819': 'White Fang (1991)', '483': 'Nightmare Before Christmas, The (1993)'}],
       [{'1303': 'Wag the Dog (1997)', '967': 'Arsenic and Old Lace (1944)', '507': 'Terminator 2: Judgment Day (1991)', '1251': 'Stripes (1981)', '2144': 'American Beauty (1999)'},
        {'257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '97': 'Braveheart (1995)', '510': 'Silence of the Lambs, The (1991)', '46': 'Usual Suspects, The (1995)'},
        {'8146': 'Only God Forgives (2013)', '6927': 'Ponyo (Gake no ue no Ponyo) (2008)', '677': 'Mother Night (1996)', '4736': 'Macbeth (a.k.a. Tragedy of Macbeth, The) (1971)', '6940': 'Inkheart (2008)'}],
       [{'785': 'Mary Poppins (1964)', '3152': "Bridget Jones's Diary (2001)", '3225': 'Atlantis: The Lost Empire (2001)', '1562': 'Splash (1984)', '2972': 'How the Grinch Stole Christmas (a.k.a. The Grinch) (2000)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'2771': 'Long Walk Home, The (1990)', '4040': 'Gallipoli (1981)', '6108': 'Annapolis (2006)', '5410': 'Wuthering Heights (1939)', '3525': 'Swamp, The (Ciénaga, La) (2001)'}],
       [{'599': 'Wallace & Gromit: A Close Shave (1995)', '2325': 'World Is Not Enough, The (1999)', '8278': 'Hobbit: The Desolation of Smaug, The (2013)', '793': 'Die Hard (1988)', '989': 'Indiana Jones and the Last Crusade (1989)'},
        {'277': 'Shawshank Redemption, The (1994)', '43': 'Seven (a.k.a. Se7en) (1995)', '97': 'Braveheart (1995)', '510': 'Silence of the Lambs, The (1991)', '46': 'Usual Suspects, The (1995)'},
        {'6576': 'Gone Baby Gone (2007)', '3624': "Bill & Ted's Bogus Journey (1991)", '4056': 'Truth About Charlie, The (2002)', '6357': 'DOA: Dead or Alive (2006)', '2552': 'Animal House (1978)'}],
       [{'4522': 'Lost in Translation (2003)', '6491': 'Death Proof (2007)', '2604': 'Hook (1991)', '895': "One Flew Over the Cuckoo's Nest (1975)", '3635': 'Beautiful Mind, A (2001)'},
        {'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'135': 'Crumb (1994)', '7463': 'Rare Exports: A Christmas Tale (Rare Exports) (2010)', '8357': 'That Awkward Moment (2014)', '5956': 'Red Eye (2005)', '4497': 'Dracula (1979)'}],
       [{'946': 'Touch of Evil (1958)', '661': 'Bound (1996)', '1335': 'Fireworks (Hana-bi) (1997)', '918': 'Killer, The (Die xue shuang xiong) (1989)', '895': "One Flew Over the Cuckoo's Nest (1975)"},
        {'314': 'Forrest Gump (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'5478': 'French Connection II (1975)', '1892': 'Children of the Corn III (1994)', '6059': 'King Kong (2005)', '5515': "'Round Midnight (1986)", '2436': 'Agnes of God (1985)'}],
       [{'3868': 'Minority Report (2002)', '4342': 'Laputa: Castle in the Sky (Tenkû no shiro Rapyuta) (1986)', '277': 'Shawshank Redemption, The (1994)', '1283': 'Good Will Hunting (1997)', '3162': 'Scarface (1983)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)', '0': 'Toy Story (1995)'},
        {'6609': 'Enchanted (2007)', '4506': 'Medallion, The (2003)', '5476': 'Holy Mountain, The (Montaña sagrada, La) (1973)', '5060': 'Ken Park (2002)', '4504': 'Revolution OS (2001)'}],
       [{'6693': 'Dark Knight, The (2008)', '1938': 'Matrix, The (1999)', '6755': 'WALL·E (2008)', '461': "Schindler's List (1993)", '2670': 'Gladiator (2000)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'5290': 'Village, The (2004)', '1799': 'Prancer (1989)', '1597': 'Dark Crystal, The (1982)', '1145': 'Grosse Pointe Blank (1997)', '926': 'Quiet Man, The (1952)'}],
       [{'43': 'Seven (a.k.a. Se7en) (1995)', '9': 'GoldenEye (1995)', '138': 'Die Hard: With a Vengeance (1995)', '314': 'Forrest Gump (1994)', '307': 'Clear and Present Danger (1994)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'2007': 'Thirteenth Floor, The (1999)', '5351': 'Surviving Christmas (2004)', '2508': 'Breaking Away (1979)', '1194': 'Air Bud (1997)', '1943': 'Metroland (1997)'}],
       [{'1718': '2010: The Year We Make Contact (1984)', '508': 'Dances with Wolves (1990)', '1805': 'Romancing the Stone (1984)', '751': 'Fly Away Home (1996)', '948': 'Bridge on the River Kwai, The (1957)'},
        {'257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '43': 'Seven (a.k.a. Se7en) (1995)', '2224': 'Fight Club (1999)'},
        {'9049': 'Into the Forest (2015)', '4728': 'National Velvet (1944)', '4774': 'King of Hearts (1966)', '3058': 'Flowers in the Attic (1987)', '6783': 'Felon (2008)'}],
       [{'4153': 'Catch Me If You Can (2002)', '2246': 'RoboCop (1987)', '6315': 'Flags of Our Fathers (2006)', '2741': 'Blood Simple (1984)', '510': 'Silence of the Lambs, The (1991)'},
        {'0': 'Toy Story (1995)', '968': 'Back to the Future (1985)', '322': 'Lion King, The (1994)', '963': 'Groundhog Day (1993)', '325': 'Mask, The (1994)'},
        {'890': 'Strictly Ballroom (1992)', '5466': 'They Call Me Trinity (1971)', '1612': 'Slums of Beverly Hills, The (1998)', '8014': 'Batman: The Dark Knight Returns, Part 1 (2012)', '6307': 'Feast (2005)'}],
       [{'2214': 'Dirty Dozen, The (1967)', '1324': 'U.S. Marshals (1998)', '5651': 'Battlestar Galactica (2003)', '1711': 'History of the World: Part I (1981)', '277': 'Shawshank Redemption, The (1994)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'7505': 'No Strings Attached (2011)', '2956': 'Bedazzled (2000)', '3250': "Diary of a Chambermaid (Journal d'une femme de chambre, Le) (1964)", '622': 'Nutty Professor, The (1996)', '2586': 'Modern Times (1936)'}],
       [{'793': 'Die Hard (1988)', '8004': 'Wreck-It Ralph (2012)', '4791': 'Lord of the Rings: The Return of the King, The (2003)', '7355': 'Inception (2010)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)', '0': 'Toy Story (1995)'},
        {'4118': 'Beast Within, The (1982)', '2355': 'Ride with the Devil (1999)', '4876': 'Passion of the Christ, The (2004)', '4909': 'Hellboy (2004)', '628': 'Lone Star (1996)'}],
       [{'963': 'Groundhog Day (1993)', '16': 'Sense and Sensibility (1995)', '938': 'Terminator, The (1984)', '898': 'Princess Bride, The (1987)', '619': 'Cable Guy, The (1996)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'6840': 'Duchess, The (2008)', '6530': 'Nanny Diaries, The (2007)', '8690': 'Kenny & Company (1976)', '7339': 'Ricky Gervais Live 3: Fame (2007)', '8009': 'Man with the Iron Fists, The (2012)'}],
       [{'88': 'City Hall (1996)', '549': 'Dragonheart (1996)', '20': 'Get Shorty (1995)', '24': 'Leaving Las Vegas (1995)', '5': 'Heat (1995)'},
        {'314': 'Forrest Gump (1994)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'9026': 'Cooties (2015)', '5547': 'Begotten (1990)', '7445': 'Somewhere (2010)', '3552': 'Focus (2001)', '3172': 'World According to Garp, The (1982)'}],
       [{'1045': 'Sling Blade (1996)', '254': 'Léon: The Professional (a.k.a. The Professional) (Léon) (1994)', '1220': 'Soul Food (1997)', '809': "William Shakespeare's Romeo + Juliet (1996)", '1353': 'Gingerbread Man, The (1998)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'8854': "Carry On Don't Lose Your Head (1966)", '1622': 'Blade (1998)', '4260': 'Spun (2001)', '3833': 'Enough (2002)', '2178': 'Alvarez Kelly (1966)'}],
       [{'2832': 'X-Men (2000)', '2300': 'Dogma (1999)', '1938': 'Matrix, The (1999)', '3192': 'Pearl Harbor (2001)', '3282': 'Legally Blonde (2001)'},
        {'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'8292': "Tim's Vermeer (2013)", '7806': 'Ghost Rider: Spirit of Vengeance (2012)', '3348': 'Vanishing, The (Spoorloos) (1988)', '3132': 'Necessary Roughness (1991)', '3933': 'Care Bears Movie II: A New Generation (1986)'}],
       [{'123': 'Apollo 13 (1995)', '35': 'Clueless (1995)', '46': 'Usual Suspects, The (1995)', '10': 'American President, The (1995)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'4409': 'Anastasia (1956)', '9416': 'Split (2017)', '3836': 'CQ (2001)', '8370': 'Barefoot (2014)', '714': 'To Catch a Thief (1955)'}],
       [{'477': 'Striking Distance (1993)', '950': 'Chinatown (1974)', '277': 'Shawshank Redemption, The (1994)', '1644': 'Untouchables, The (1987)', '922': 'Full Metal Jacket (1987)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'2227': 'Julien Donkey-Boy (1999)', '2918': 'Hellbound: Hellraiser II (1988)', '4550': 'To Be and to Have (Être et avoir) (2002)', '9421': 'Fences (2016)', '1265': 'Mortal Kombat: Annihilation (1997)'}],
       [{'123': 'Apollo 13 (1995)', '253': 'Outbreak (1995)', '307': 'Clear and Present Danger (1994)', '398': 'Fugitive, The (1993)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'2948': 'Billy Jack Goes to Washington (1977)', '1922': 'Dead Ringers (1988)', '7118': 'Food, Inc. (2008)', '4356': 'Wrong Turn (2003)', '27': 'Persuasion (1995)'}],
       [{'235': "Mary Shelley's Frankenstein (Frankenstein) (1994)", '308': 'Client, The (1994)', '93': 'Bridges of Madison County, The (1995)', '314': 'Forrest Gump (1994)', '379': 'Coneheads (1993)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '43': 'Seven (a.k.a. Se7en) (1995)', '0': 'Toy Story (1995)'},
        {'8089': 'Act of Killing, The (2012)', '9289': 'Ali Wong: Baby Cobra (2016)', '6066': 'Wal-Mart: The High Cost of Low Price (2005)', '5280': 'Unprecedented: The 2000 Presidential Election (2002)', '7772': 'Underworld: Awakening (2012)'}],
       [{'855': 'Abyss, The (1989)', '511': 'Snow White and the Seven Dwarfs (1937)', '1594': "Charlotte's Web (1973)", '783': 'Sword in the Stone, The (1963)', '1548': '101 Dalmatians (One Hundred and One Dalmatians) (1961)'},
        {'314': 'Forrest Gump (1994)', '277': 'Shawshank Redemption, The (1994)', '418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)', '2224': 'Fight Club (1999)'},
        {'9157': 'He Never Died (2015)', '3707': 'Stroszek (1977)', '6337': 'Fast Food Nation (2006)', '6368': 'Primeval (2007)', '5726': 'Phantom of the Opera, The (2004)'}],
       [{'228': 'Like Water for Chocolate (Como agua para chocolate) (1992)', '375': "Carlito's Way (1993)", '201': 'Ed Wood (1994)', '196': 'Dolores Claiborne (1995)', '74': "Antonia's Line (Antonia) (1995)"},
        {'314': 'Forrest Gump (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'9443': 'John Wick: Chapter Two (2017)', '1369': 'Clockwatchers (1997)', '4838': 'Tormented (1960)', '8061': "It's Such a Beautiful Day (2012)", '7099': 'If These Walls Could Talk (1996)'}],
       [{'6910': 'Wrestler, The (2008)', '5253': 'Anchorman: The Legend of Ron Burgundy (2004)', '1290': 'Titanic (1997)', '6563': 'Into the Wild (2007)', '5869': 'Crash (2004)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)'},
        {'9424': 'Sing (2016)', '7247': 'Secret of Kells, The (2009)', '9665': 'Isle of Dogs (2018)', '5727': 'Beyond the Sea (2004)', '7870': 'Prometheus (2012)'}],
       [{'2016': "General's Daughter, The (1999)", '480': 'Terminal Velocity (1994)', '15': 'Casino (1995)', '217': 'Interview with the Vampire: The Vampire Chronicles (1994)', '619': 'Cable Guy, The (1996)'},
        {'418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '507': 'Terminator 2: Judgment Day (1991)', '31': 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)'},
        {'9442': 'Kizumonogatari III: Cold Blood (2017)', '3874': 'Pumpkin (2002)', '4043': 'Happy Birthday to Me (1981)', '4125': 'Maid in Manhattan (2002)', '6007': 'Wraith, The (1986)'}],
       [{'220': 'Junior (1994)', '301': 'Baby-Sitters Club, The (1995)', '226': 'Little Princess, A (1995)', '28': 'City of Lost Children, The (Cité des enfants perdus, La) (1995)', '421': 'Lassie (1994)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '2224': 'Fight Club (1999)'},
        {'6082': 'New World, The (2005)', '9393': 'Jack Reacher: Never Go Back (2016)', '6808': 'Mutant Chronicles (2008)', '4078': 'Houseboat (1958)', '7899': 'Presto (2008)'}],
       [{'113': 'Down Periscope (1996)', '116': 'Birdcage, The (1996)', '33': 'Dead Man Walking (1995)', '58': 'Bio-Dome (1996)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'8083': 'ABCs of Death, The (2012)', '4326': 'Spellbound (2002)', '8361': 'Non-Stop (2014)', '4030': 'Blow Out (1981)', '893': 'Madonna: Truth or Dare (1991)'}],
       [{'618': 'Hunchback of Notre Dame, The (1996)', '99': 'Rumble in the Bronx (Hont faan kui) (1995)', '5': 'Heat (1995)', '1480': 'Mask of Zorro, The (1998)', '508': 'Dances with Wolves (1990)'},
        {'277': 'Shawshank Redemption, The (1994)', '43': 'Seven (a.k.a. Se7en) (1995)', '334': 'Speed (1994)', '520': 'Fargo (1996)', '914': 'Alien (1979)'},
        {'6121': 'Freedomland (2006)', '4793': 'Calendar Girls (2003)', '7213': 'MacGyver: Lost Treasure of Atlantis (1994)', '871': 'Tin Drum, The (Blechtrommel, Die) (1979)', '6753': 'Incredible Hulk, The (2008)'}],
       [{'297': 'While You Were Sleeping (1995)', '322': 'Lion King, The (1994)', '176': 'Waterworld (1995)', '274': 'Specialist, The (1994)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'6611': 'Awake (2007)', '6693': 'Dark Knight, The (2008)', '3849': 'Bourne Identity, The (2002)', '9151': 'Wizards of Waverly Place: The Movie (2009)', '1621': 'Return to Paradise (1998)'}],
       [{'116': 'Birdcage, The (1996)', '5725': 'Aviator, The (2004)', '5361': 'Ray (2004)', '3310': 'Cocktail (1988)', '6241': 'Pursuit of Happyness, The (2006)'},
        {'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'984': 'Somewhere in Time (1980)', '7663': 'Birdemic: Shock and Terror (2010)', '167': 'Strange Days (1995)', '7897': 'Rock of Ages (2012)', '6538': 'Nines, The (2007)'}],
       [{'1223': 'Game, The (1997)', '140': 'First Knight (1995)', '1182': 'Men in Black (a.k.a. MIB) (1997)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'3140': 'Spy Kids (2001)', '2023': 'Dinner Game, The (Dîner de cons, Le) (1998)', '8252': 'Bad Milo (Bad Milo!) (2013)', '8750': 'The Last Five Years (2014)', '9678': 'Death Wish (2018)'}],
       [{'6241': 'Pursuit of Happyness, The (2006)', '314': 'Forrest Gump (1994)', '4354': 'Finding Nemo (2003)', '3002': 'Cast Away (2000)', '97': 'Braveheart (1995)'},
        {'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'7091': 'G-Force (2009)', '9083': 'Bros Before Hos (2013)', '5134': 'Grey Gardens (1975)', '9700': 'Boundaries (2018)', '9295': 'Teenage Mutant Ninja Turtles: Out of the Shadows (2016)'}],
       [{'8551': 'The Imitation Game (2014)', '5852': 'Trip to the Moon, A (Voyage dans la lune, Le) (1902)', '2258': 'Princess Mononoke (Mononoke-hime) (1997)', '4607': 'Kill Bill: Vol. 1 (2003)', '929': 'Annie Hall (1977)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)', '97': 'Braveheart (1995)'},
        {'5625': 'Late Night Shopping (2001)', '2499': 'Blood Feast (1963)', '7581': 'Fast Five (Fast and the Furious 5, The) (2011)', '6013': 'North Country (2005)', '4310': 'Fahrenheit 451 (1966)'}]],
      dtype=object)

score = 0
n_film_test = 5
r = (np.random.rand(10)*len(dataset)).astype(int)
experiment_dataset = np.array(dataset)[r]
size = len(experiment_dataset)
pp = pprint.PrettyPrinter(depth=4, sort_dicts=False) 

for i, values in enumerate(experiment_dataset):
	watched_dict, top_reco_dict, unwatched_dict = values
	print("-------------------------------------------- User", i+1, "/", size ,"--------------------------------------------")
	print("\n--> List of film seen by user")
	pp.pprint(list(watched_dict.values()))
	print("\n--> Choose 5 films you would recommand for that user in the following list :")
	tmp = dict(top_reco_dict, **unwatched_dict)
	keys = list(dict(top_reco_dict, **unwatched_dict).keys())
	random.shuffle(keys)
	shuffled_dict = dict()
	for key in keys:
		shuffled_dict.update({key: tmp[key]})
	pp.pprint(shuffled_dict)
	print("\n--> Your choice must be this format : 145/323/447/565/23")
	while True:
		try:
			help_choice = input().split("/")
			assert len(help_choice) == n_film_test
			assert [help_choice[i] in shuffled_dict.keys() for i in range(len(help_choice))] == [True] * n_film_test
		except:
			print("\n--> Please use the correct format, you must give 5 answers only, chosen in the previous list.")
			continue
		else:
			break
	for choice in help_choice:
		if choice in top_reco_dict.keys():
			score += 1
print("\n--> Please return this score :", score/(size*n_film_test))
