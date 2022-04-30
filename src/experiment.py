import random
import pprint
import numpy as np


dataset = np.array([[{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'277': 'Shawshank Redemption, The (1994)', '2224': 'Fight Club (1999)', '659': 'Godfather, The (1972)', '507': 'Terminator 2: Judgment Day (1991)', '31': 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)'},
        {'6653': 'Untraceable (2008)', '4179': 'Mystery Date (1991)', '2993': 'Punchline (1988)', '6167': 'Friends with Money (2006)', '4298': 'House of 1000 Corpses (2003)'}],
       [{'277': 'Shawshank Redemption, The (1994)', '1283': 'Good Will Hunting (1997)', '2670': 'Gladiator (2000)', '4607': 'Kill Bill: Vol. 1 (2003)', '291': 'Tommy Boy (1995)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'4002': 'Brown Sugar (2002)', '5089': 'Frankenstein Unbound (1990)', '6845': 'City of Ember (2008)', '3209': 'Animal, The (2001)', '546': 'Mission: Impossible (1996)'}],
       [{'461': "Schindler's List (1993)", '2941': 'Requiem for a Dream (2000)', '1543': 'Lady and the Tramp (1955)', '973': 'Highlander (1986)', '999': 'Field of Dreams (1989)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'8087': 'Safe Haven (2013)', '1167': 'Rough Magic (1995)', '5198': 'Christmas Carol, A (Scrooge) (1951)', '1399': 'Madeline (1998)', '9639': 'Ferdinand (2017)'}],
       [{'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'314': 'Forrest Gump (1994)', '277': 'Shawshank Redemption, The (1994)', '418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)', '97': 'Braveheart (1995)'},
        {'6730': 'Fall, The (2006)', '2171': 'Drive Me Crazy (1999)', '3244': 'Alice (1990)', '8082': 'Identity Thief (2013)', '7014': 'Night at the Museum: Battle of the Smithsonian (2009)'}],
       [{'257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '0': 'Toy Story (1995)', '97': 'Braveheart (1995)', '46': 'Usual Suspects, The (1995)'},
        {'314': 'Forrest Gump (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'1186': 'Contact (1997)', '9013': 'Ready Player One', '6551': 'December Boys (2007)', '4104': 'Elling (2001)', '3749': 'Taps (1981)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '0': 'Toy Story (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)'},
        {'5891': 'Cinderella Man (2005)', '5348': 'Tarnation (2003)', '3116': 'Battle Beyond the Stars (1980)', '7561': '13 Assassins (Jûsan-nin no shikaku) (2010)', '9179': 'Tomorrow (2015)'}],
       [{'314': 'Forrest Gump (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)'},
        {'257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '43': 'Seven (a.k.a. Se7en) (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)'},
        {'1083': 'Last of the Mohicans, The (1992)', '1279': 'Butcher Boy, The (1997)', '1470': 'Poltergeist III (1988)', '359': 'Another Stakeout (1993)', '5181': 'Anthony Adverse (1936)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '43': 'Seven (a.k.a. Se7en) (1995)', '97': 'Braveheart (1995)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)'},
        {'6028': 'Revolver (2005)', '930': 'Right Stuff, The (1983)', '8112': 'Brass Teapot, The (2012)', '9159': 'Parasyte: Part 2 (2015)', '5876': 'Cocoanuts, The (1929)'}],
       [{'899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '968': 'Back to the Future (1985)', '3633': 'Lord of the Rings: The Fellowship of the Ring, The (2001)', '1485': 'Back to the Future Part II (1989)', '1486': 'Back to the Future Part III (1990)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'8179': "Adam and Eve (National Lampoon's Adam & Eve) (2005)", '3467': 'Summer Catch (2001)', '2253': 'Rawhead Rex (1986)', '5987': 'Flightplan (2005)', '3430': 'Uncle Buck (1989)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '1938': 'Matrix, The (1999)', '2224': 'Fight Club (1999)', '2077': 'Sixth Sense, The (1999)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'1098': 'Angel Baby (1995)', '8140': 'Great Gatsby, The (2013)', '2274': 'Drugstore Cowboy (1989)', '9636': 'The Post (2017)', '1645': 'Dirty Work (1998)'}],
       [{'314': 'Forrest Gump (1994)', '277': 'Shawshank Redemption, The (1994)', '418': 'Jurassic Park (1993)', '97': 'Braveheart (1995)', '510': 'Silence of the Lambs, The (1991)'},
        {'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'7139': 'Education, An (2009)', '351': 'Federal Hill (1994)', '358': 'Air Up There, The (1994)', '1574': 'Outsiders, The (1983)', '8306': 'Guest from the Future (Gostya iz buduschego) (1985)'}],
       [{'963': 'Groundhog Day (1993)', '1290': 'Titanic (1997)', '315': 'Four Weddings and a Funeral (1994)', '35': 'Clueless (1995)', '1562': 'Splash (1984)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'8228': 'Justice League: Crisis on Two Earths (2010)', '359': 'Another Stakeout (1993)', '5502': 'Boy Meets Girl (1984)', '2927': 'Creature from the Black Lagoon, The (1954)', '7251': 'District 13: Ultimatum (Banlieue 13 - Ultimatum) (2009)'}],
       [{'1938': 'Matrix, The (1999)', '43': 'Seven (a.k.a. Se7en) (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '1290': 'Titanic (1997)', '2670': 'Gladiator (2000)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'2698': 'Better Living Through Circuitry (1999)', '7153': 'Aelita: The Queen of Mars (Aelita) (1924)', '3423': 'Sweetie (1989)', '2950': 'Ghoulies II (1987)', '5668': 'Helen of Troy (2003)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '0': 'Toy Story (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)'},
        {'9647': 'Porky in Wackyland (1938)', '8522': 'Culture High, The (2014)', '6519': 'Tell No One (Ne le dis à personne) (2006)', '5896': 'Adventures of Sharkboy and Lavagirl 3-D, The (2005)', '6923': 'Wild Child (2008)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'418': 'Jurassic Park (1993)', '97': 'Braveheart (1995)', '510': 'Silence of the Lambs, The (1991)', '46': 'Usual Suspects, The (1995)', '1182': 'Men in Black (a.k.a. MIB) (1997)'},
        {'55': "Mr. Holland's Opus (1995)", '967': 'Arsenic and Old Lace (1944)', '675': 'Halloween: The Curse of Michael Myers (Halloween 6: The Curse of Michael Myers) (1995)', '8107': 'Call, The (2013)', '5636': 'Ali G Indahouse (2002)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)', '97': 'Braveheart (1995)', '910': 'Star Wars: Episode VI - Return of the Jedi (1983)', '1182': 'Men in Black (a.k.a. MIB) (1997)'},
        {'3262': 'Cries and Whispers (Viskningar och rop) (1972)', '4491': '10 (1979)', '7216': "Project A 2 ('A' gai wak juk jap) (1987)", '7455': 'Casino Jack (2010)', '9146': 'The Ridiculous 6 (2015)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'1182': 'Men in Black (a.k.a. MIB) (1997)', '31': 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)', '334': 'Speed (1994)', '862': 'Monty Python and the Holy Grail (1975)', '520': 'Fargo (1996)'},
        {'1483': 'Soylent Green (1973)', '3316': 'D.O.A. (1988)', '2327': 'Babes in Toyland (1934)', '1329': 'Suicide Kings (1997)', '712': 'Spellbound (1945)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'2144': 'American Beauty (1999)', '963': 'Groundhog Day (1993)', '123': 'Apollo 13 (1995)', '1978': 'Star Wars: Episode I - The Phantom Menace (1999)', '835': 'E.T. the Extra-Terrestrial (1982)'},
        {'7329': 'Sex and the City 2 (2010)', '1667': 'Allnighter, The (1987)', '3958': 'Ernest Scared Stupid (1991)', '5791': 'Kung Fu Hustle (Gong fu) (2004)', '896': "Cheech and Chong's Up in Smoke (1978)"}],
       [{'314': 'Forrest Gump (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '97': 'Braveheart (1995)', '510': 'Silence of the Lambs, The (1991)', '46': 'Usual Suspects, The (1995)'},
        {'2759': 'Alien Nation (1988)', '2352': 'End of Days (1999)', '8658': 'Tooth Fairy 2 (2012)', '6870': 'Role Models (2008)', '8432': 'Equalizer, The (2014)'}],
       [{'322': 'Lion King, The (1994)', '835': 'E.T. the Extra-Terrestrial (1982)', '2670': 'Gladiator (2000)', '3189': 'Shrek (2001)', '506': 'Aladdin (1992)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'7065': 'Imaginarium of Doctor Parnassus, The (2009)', '3403': 'Punisher, The (1989)', '90': 'Mr. Wrong (1996)', '4754': 'Amarcord (1973)', '5328': 'Orca: The Killer Whale (1977)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'277': 'Shawshank Redemption, The (1994)', '43': 'Seven (a.k.a. Se7en) (1995)', '97': 'Braveheart (1995)', '510': 'Silence of the Lambs, The (1991)', '46': 'Usual Suspects, The (1995)'},
        {'9243': 'Neighbors 2: Sorority Rising (2016)', '55': "Mr. Holland's Opus (1995)", '3438': "Who'll Stop the Rain (1978)", '4551': 'Triplets of Belleville, The (Les triplettes de Belleville) (2003)', '1968': 'Chopping Mall (a.k.a. Killbots) (1986)'}],
       [{'314': 'Forrest Gump (1994)', '277': 'Shawshank Redemption, The (1994)', '2224': 'Fight Club (1999)', '659': 'Godfather, The (1972)', '474': 'Blade Runner (1982)'},
        {'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'3723': 'Zombie (a.k.a. Zombie 2: The Dead Are Among Us) (Zombi 2) (1979)', '3990': 'Welcome to Collinwood (2002)', '8844': 'Carol (2015)', '4510': 'Dust (2001)', '3053': 'Cop (1988)'}],
       [{'257': 'Pulp Fiction (1994)', '46': 'Usual Suspects, The (1995)', '659': 'Godfather, The (1972)', '31': 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)', '793': 'Die Hard (1988)'},
        {'314': 'Forrest Gump (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'9218': 'Rabbits (2002)', '7131': 'Metropia (2009)', '7394': 'Resident Evil: Afterlife (2010)', '5054': 'Winter Light (Nattvardsgästerna) (1963)', '7423': 'Luck by Chance (2009)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)', '0': 'Toy Story (1995)'},
        {'2121': 'Three Days of the Condor (3 Days of the Condor) (1975)', '5061': 'Monterey Pop (1968)', '5440': 'Carabineers, The (Carabiniers, Les) (1963)', '9270': 'Buck Rogers in the 25th Century (1979)', '4961': 'Fountainhead, The (1949)'}],
       [{'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '1502': 'Saving Private Ryan (1998)', '461': "Schindler's List (1993)"},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'4632': 'Revolution Will Not Be Televised, The (a.k.a. Chavez: Inside the Coup) (2003)', '5662': "Crimson Rivers 2: Angels of the Apocalypse (Rivières pourpres II - Les anges de l'apocalypse, Les) (2004)", '1199': 'Desperate Measures (1998)', '7144': 'Where the Wild Things Are (2009)', '5046': 'Stray Dog (Nora inu) (1949)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '43': 'Seven (a.k.a. Se7en) (1995)', '123': 'Apollo 13 (1995)', '337': 'True Lies (1994)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'4489': 'Atragon (Kaitei Gunkan) (1963)', '849': 'People vs. Larry Flynt, The (1996)', '9447': 'T2: Trainspotting (2017)', '4846': 'Perfect Score, The (2004)', '4665': 'Ordet (Word, The) (1955)'}],
       [{'314': 'Forrest Gump (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)'},
        {'257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '43': 'Seven (a.k.a. Se7en) (1995)', '2224': 'Fight Club (1999)'},
        {'7062': 'Roots (1977)', '4345': 'Matrix Reloaded, The (2003)', '3480': 'Two Can Play That Game (2001)', '8260': 'Escape Plan (2013)', '3449': 'Theremin: An Electronic Odyssey (1993)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'0': 'Toy Story (1995)', '968': 'Back to the Future (1985)', '322': 'Lion King, The (1994)', '963': 'Groundhog Day (1993)', '325': 'Mask, The (1994)'},
        {'7120': 'Thirst (Bakjwi) (2009)', '5547': 'Begotten (1990)', '655': 'Spitfire Grill, The (1996)', '7157': 'Love Exposure (Ai No Mukidashi) (2008)', '4141': 'Duellists, The (1977)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '46': 'Usual Suspects, The (1995)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'8239': 'Insidious: Chapter 2 (2013)', '9233': 'Neon Bull (2015)', '578': 'Oliver & Company (1988)', '8240': 'Rush (2013)', '3776': 'Lucky Break (2001)'}],
       [{'224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)', '0': 'Toy Story (1995)'},
        {'3411': 'Cure (1997)', '3708': 'Dragonfly (2002)', '5925': 'Hardware (1990)', '1900': 'Alligator (1980)', '3382': 'January Man, The (1989)'}],
       [{'897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '0': 'Toy Story (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '968': 'Back to the Future (1985)', '793': 'Die Hard (1988)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'6189': 'Art School Confidential (2006)', '1769': 'King Kong Lives (1986)', '2560': 'Death Wish (1974)', '4537': 'Anything Else (2003)', '8660': 'The Deadly Bees (1967)'}],
       [{'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '0': 'Toy Story (1995)', '510': 'Silence of the Lambs, The (1991)'},
        {'314': 'Forrest Gump (1994)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'6925': 'Zeitgeist: Addendum (2008)', '3885': 'Road to Perdition (2002)', '3712': 'Monsoon Wedding (2001)', '4539': 'Fighting Temptations, The (2003)', '2014': 'Red Violin, The (Violon rouge, Le) (1998)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '0': 'Toy Story (1995)', '97': 'Braveheart (1995)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'4895': 'Broken Wings (Knafayim Shvurot) (2002)', '5005': 'Undercurrent (1946)', '772': 'Pollyanna (1960)', '1496': 'Last Temptation of Christ, The (1988)', '3816': 'Giant Spider Invasion, The (1975)'}],
       [{'314': 'Forrest Gump (1994)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '2224': 'Fight Club (1999)', '97': 'Braveheart (1995)'},
        {'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'5771': 'Marriage of Maria Braun, The (Ehe der Maria Braun, Die) (1979)', '284': 'To Live (Huozhe) (1994)', '6039': 'Derailed (2005)', '256': "Pyromaniac's Love Story, A (1995)", '1304': 'Dark City (1998)'}],
       [{'46': 'Usual Suspects, The (1995)', '123': 'Apollo 13 (1995)', '197': 'Dumb & Dumber (Dumb and Dumber) (1994)', '275': 'Stargate (1994)', '156': 'Net, The (1995)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'6361': 'Black Christmas (2006)', '6488': 'Fantastic Four: Rise of the Silver Surfer (2007)', '4435': 'Little Giants (1994)', '728': 'Giant (1956)', '1262': 'Joy Luck Club, The (1993)'}],
       [{'277': 'Shawshank Redemption, The (1994)', '1283': 'Good Will Hunting (1997)', '701': 'Wizard of Oz, The (1939)', '922': 'Full Metal Jacket (1987)', '1486': 'Back to the Future Part III (1990)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'6999': 'X-Men Origins: Wolverine (2009)', '9369': 'Over the Garden Wall (2013)', '7606': 'Beginners (2010)', '8087': 'Safe Haven (2013)', '2612': "Murphy's Romance (1985)"}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '123': 'Apollo 13 (1995)', '337': 'True Lies (1994)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'1709': 'Strangeland (1998)', '412': 'In the Line of Fire (1993)', '7201': 'Sorority Babes in the Slimeball Bowl-O-Rama (1988)', '2717': 'Endless Summer, The (1966)', '6706': "Nim's Island (2008)"}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '418': 'Jurassic Park (1993)', '97': 'Braveheart (1995)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '43': 'Seven (a.k.a. Se7en) (1995)', '0': 'Toy Story (1995)'},
        {'6674': 'Descent (2007)', '6395': 'Unknown (2006)', '13': 'Nixon (1995)', '506': 'Aladdin (1992)', '1446': 'Nightmare on Elm Street 3: Dream Warriors, A (1987)'}],
       [{'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'314': 'Forrest Gump (1994)', '277': 'Shawshank Redemption, The (1994)', '418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)', '2224': 'Fight Club (1999)'},
        {'462': 'Scout, The (1994)', '6917': 'Bedtime Stories (2008)', '2662': 'Smiling Fish and Goat on Fire (1999)', '6018': 'Shopgirl (2005)', '2965': 'Men of Honor (2000)'}],
       [{'257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '0': 'Toy Story (1995)', '97': 'Braveheart (1995)', '322': 'Lion King, The (1994)'},
        {'314': 'Forrest Gump (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'4389': 'Music Box (1989)', '5106': 'Charly (1968)', '7254': 'Crazies, The (2010)', '5467': 'Topo, El (1970)', '9116': "Le Maître d'école (1981)"}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '1938': 'Matrix, The (1999)', '43': 'Seven (a.k.a. Se7en) (1995)', '2224': 'Fight Club (1999)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)'},
        {'3917': 'Secret Ballot (Raye makhfi) (2001)', '1769': 'King Kong Lives (1986)', '5733': 'Merchant of Venice, The (2004)', '814': 'Crossfire (1947)', '8949': 'Amy (2015)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)'},
        {'418': 'Jurassic Park (1993)', '0': 'Toy Story (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '507': 'Terminator 2: Judgment Day (1991)', '31': 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)'},
        {'2640': 'East is East (1999)', '7630': 'One Day (2011)', '4462': 'Divorce, Le (2003)', '4414': 'Tenant, The (Locataire, Le) (1976)', '3313': 'Couch Trip, The (1988)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '2224': 'Fight Club (1999)'},
        {'777': '20,000 Leagues Under the Sea (1954)', '9386': 'La La Land (2016)', '9199': 'Grease Live (2016)', '1798': 'Santa Claus: The Movie (1985)', '5865': 'Enron: The Smartest Guys in the Room (2005)'}],
       [{'224': 'Star Wars: Episode IV - A New Hope (1977)', '0': 'Toy Story (1995)', '615': 'Independence Day (a.k.a. ID4) (1996)', '546': 'Mission: Impossible (1996)', '92': 'Happy Gilmore (1996)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'2275': 'Falling Down (1993)', '3898': 'Austin Powers in Goldmember (2002)', '6186': 'American Haunting, An (2005)', '9613': 'Male Hunt (1964)', '3710': "How to Kill Your Neighbor's Dog (2000)"}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'277': 'Shawshank Redemption, The (1994)', '43': 'Seven (a.k.a. Se7en) (1995)', '334': 'Speed (1994)', '520': 'Fargo (1996)', '914': 'Alien (1979)'},
        {'4487': 'THX 1138 (1971)', '4638': "My Architect: A Son's Journey (2003)", '5932': 'Sky High (2005)', '5325': 'Come Back, Little Sheba (1952)', '5736': 'White Noise (2005)'}],
       [{'277': 'Shawshank Redemption, The (1994)', '0': 'Toy Story (1995)', '97': 'Braveheart (1995)', '46': 'Usual Suspects, The (1995)', '31': 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'9069': 'Wonder Woman (2017)', '1815': 'Back to School (1986)', '6024': "Don't Move (Non ti muovere) (2004)", '6216': "Jet Li's Fearless (Huo Yuan Jia) (2006)", '7207': 'Book of Eli, The (2010)'}],
       [{'314': 'Forrest Gump (1994)', '277': 'Shawshank Redemption, The (1994)', '43': 'Seven (a.k.a. Se7en) (1995)', '2224': 'Fight Club (1999)', '510': 'Silence of the Lambs, The (1991)'},
        {'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)'},
        {'4512': 'Jeepers Creepers 2 (2003)', '234': 'Madness of King George, The (1994)', '4772': 'Wings of Honneamise (Ôritsu uchûgun Oneamisu no tsubasa) (1987)', '2009': 'Instinct (1999)', '1120': "Vegas Vacation (National Lampoon's Las Vegas Vacation) (1997)"}],
       [{'1938': 'Matrix, The (1999)', '1182': 'Men in Black (a.k.a. MIB) (1997)', '615': 'Independence Day (a.k.a. ID4) (1996)', '1575': 'Indiana Jones and the Temple of Doom (1984)', '1157': 'Fifth Element, The (1997)'},
        {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '277': 'Shawshank Redemption, The (1994)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)'},
        {'9089': 'Goosebumps (2015)', '5292': 'Musa the Warrior (Musa) (2001)', '5392': 'Freshman, The (1925)', '765': 'Apple Dumpling Gang, The (1975)', '3581': 'Midway (1976)'}],
       [{'314': 'Forrest Gump (1994)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '97': 'Braveheart (1995)', '1502': 'Saving Private Ryan (1998)'},
        {'257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)'},
        {'9427': "Assassin's Creed (2016)", '9260': 'I Am Wrath (2016)', '7128': 'Serious Man, A (2009)', '4632': 'Revolution Will Not Be Televised, The (a.k.a. Chavez: Inside the Coup) (2003)', '4911': 'Walking Tall (2004)'}],
       [{'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '277': 'Shawshank Redemption, The (1994)', '1938': 'Matrix, The (1999)', '0': 'Toy Story (1995)'},
        {'224': 'Star Wars: Episode IV - A New Hope (1977)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)', '97': 'Braveheart (1995)'},
        {'28': 'City of Lost Children, The (Cité des enfants perdus, La) (1995)', '7194': 'Alice (2009)', '5281': 'Prime of Miss Jean Brodie, The (1969)', '4944': 'Enemy Mine (1985)', '5474': 'Emmanuelle (1974)'}]], dtype=object)

score = 0
r = (np.random.rand(10)*len(dataset)).astype(int)
experiment_dataset = np.array(dataset)[r]
experiment_dataset = experiment_dataset[:2]
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
			assert len(help_choice) == 5
			assert [help_choice[i] in shuffled_dict.keys() for i in range(len(help_choice))] == [True] * 5
		except:
			print("\n--> Please use the correct format, you must give 5 answers only, chosen in the previous list.")
			continue
		else:
			break
	for choice in help_choice:
		if choice in top_reco_dict.keys():
			score += 1
print("\n--> Please return this score :", score/(size*5))
