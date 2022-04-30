import random
import pprint



dataset = [({'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)', '0': 'Toy Story (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '97': 'Braveheart (1995)'}, {'277': 'Shawshank Redemption, The (1994)', '2224': 'Fight Club (1999)', '659': 'Godfather, The (1972)', '507': 'Terminator 2: Judgment Day (1991)', '31': 'Twelve Monkeys (a.k.a. 12 Monkeys) (1995)', '2077': 'Sixth Sense, The (1999)', '793': 'Die Hard (1988)', '334': 'Speed (1994)', '322': 'Lion King, The (1994)', '1266': 'Truman Show, The (1998)'}, {'7272': 'Generation X (1996)', '7278': 'Mondo Cane (1962)', '7305': 'Human Centipede, The (First Sequence) (2009)', '7280': 'Case 39 (2009)', '7294': 'American Drug War: The Last White Hope (2007)', '7295': 'Runaways, The (2010)', '7298': 'Valhalla Rising (2009)', '7299': 'Diary of a Wimpy Kid (2010)', '7301': 'Disgrace (2008)', '9723': 'Andrew Dice Clay: Dice Rules (1991)'}), ({'277': 'Shawshank Redemption, The (1994)', '1283': 'Good Will Hunting (1997)', '2670': 'Gladiator (2000)', '4607': 'Kill Bill: Vol. 1 (2003)', '291': 'Tommy Boy (1995)', '6693': 'Dark Knight, The (2008)', '6298': 'Departed, The (2006)', '5294': 'Collateral (2004)', '6993': 'Inglourious Basterds (2009)', '7355': 'Inception (2010)'}, {'314': 'Forrest Gump (1994)', '257': 'Pulp Fiction (1994)', '224': 'Star Wars: Episode IV - A New Hope (1977)', '1938': 'Matrix, The (1999)', '897': 'Star Wars: Episode V - The Empire Strikes Back (1980)', '418': 'Jurassic Park (1993)', '43': 'Seven (a.k.a. Se7en) (1995)', '0': 'Toy Story (1995)', '899': 'Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)', '2224': 'Fight Club (1999)'}, {'7272': 'Generation X (1996)', '7278': 'Mondo Cane (1962)', '7305': 'Human Centipede, The (First Sequence) (2009)', '7280': 'Case 39 (2009)', '7294': 'American Drug War: The Last White Hope (2007)', '7295': 'Runaways, The (2010)', '7298': 'Valhalla Rising (2009)', '7299': 'Diary of a Wimpy Kid (2010)', '7301': 'Disgrace (2008)', '9723': 'Andrew Dice Clay: Dice Rules (1991)'})]


# watched_dict = {
# 	"234":"film1",
# 	"245":"film2",
# 	"258":"film3",
# 	"256":"film4",
# 	"255":"film5",
# }

# top_reco_dict = {
# 	"874":"film6",
# 	"852":"film7",
# 	"853":"film8",
# 	"862":"film9",
# 	"874":"film10",
# }

# unwatched_dict = {
# 	"745":"film11",
# 	"741":"film12",
# 	"785":"film13",
# 	"789":"film14",
# 	"782":"film15",
# }

score = 0
experiment_dataset = dataset
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
