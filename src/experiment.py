import numpy as np
import random


watched_dict = {
	"234":"film1",
	"245":"film2",
	"258":"film3",
	"256":"film4",
	"255":"film5",
}

top_reco_dict = {
	"874":"film6",
	"852":"film7",
	"853":"film8",
	"862":"film9",
	"874":"film10",
}

unwatched_dict = {
	"745":"film11",
	"741":"film12",
	"785":"film13",
	"789":"film14",
	"782":"film15",
}

score = 0
experiment_dataset = np.array([[watched_dict, top_reco_dict, unwatched_dict]])
print(experiment_dataset)
size = len(experiment_dataset) 

for i, values in enumerate(experiment_dataset):
	watched_dict, top_reco_dict, unwatched_dict = values
	print("---------------------- User", i+1, "/", size+1 ,"----------------------")
	print("--> List of film seen by user")
	print(watched_dict.values())
	print("--> Choose 5 films you would recommand for that user in the following list :")
	tmp = dict(top_reco_dict, **unwatched_dict)
	keys = list(dict(top_reco_dict, **unwatched_dict).keys())
	random.shuffle(keys)
	shuffled_dict = dict()
	for key in keys:
		shuffled_dict.update({key: tmp[key]})
	print(shuffled_dict)
	print("--> Your choice must be this format : 145/323/447/565/23")
	while True:
		try:
			help_choice = input().split("/")
			assert len(help_choice) == 5
			assert [help_choice[i] in shuffled_dict.keys() for i in range(len(help_choice))] == [True] * 5
		except:
			print("-> Please use the correct format, you must give 5 answers only, chosen in the previous list.")
			continue
		else:
			break
	for choice in help_choice:
		if choice in top_reco_dict.keys():
			score += 1
print("--> Please return this score :", score/(size*5))
