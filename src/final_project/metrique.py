from global_ import *


# Running some test for the DOA metrics before computing it on whole user list

# Computes DOA score for a specific user
def compute_doa_score(TR_ki, test_rating_user, unwatched_user):
	score = 0
	for m_i in test_rating_user:
		for m_j in unwatched_user:
			if TR_ki[int(m_i)] > TR_ki[int(m_j)]:
				score += 1
	return score / (len(test_rating_user) * len(unwatched_user))

# Computes DOA for the whole user list
def compute_all_doa(TR_ki_all_user, test_rating_user_list, ratings):
	score = 0
	n_user = TR_ki_all_user.shape[0]
	for user_id in range(n_user):
		tmp = test_rating_user_list[user_id]
		test_films = tmp[:,1]
		TR_ki = TR_ki_all_user[user_id]
		_, _, unwatched_films = get_infos_user(user_id, ratings)
		score += compute_doa_score(TR_ki, test_films, unwatched_films)
	return score / n_user

def test_doa_user(n_user, n_film_test, TR_ki_all_user, test_rating_user_list, ratings):
	for test_user_id in range(n_user):
		print("---------- Testing user number", test_user_id, "----------")
		test = test_rating_user_list[test_user_id]
		test_films = test[:,1]
		TR_ki = TR_ki_all_user[test_user_id]
		_, _, unwatched_films = get_infos_user(test_user_id, ratings)
		print("Some movies from test set:")
		print(test_films[:n_film_test])
		print("Some movies from unwatched set:")
		print(unwatched_films[:n_film_test])
		print("Some score for test set (movies watched by user):")
		for i in test_films[:n_film_test]:
			print(TR_ki[int(i)])
		print("Some score for unwatched movies:")
		for i in unwatched_films[:n_film_test]:
			print(TR_ki[int(i)])
		print("Total DOA score for this user :", compute_doa_score(TR_ki, test_films, unwatched_films))