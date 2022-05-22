from global_ import *


def build_experimental_dataset(movies, ratings, TR_ki_all_user, train_rating_user_list, test_rating_user_list, n_user, n_film_test):
	dataset = []
	dict_id_title = dict(zip(list(movies['movieId']),list(movies['title'])))
	for userId in tqdm(range(n_user)):
		watched_user = train_rating_user_list[userId][:,1].astype(int)
		test_rating_user = test_rating_user_list[userId][:,1].astype(int)
		_, _, unwatched_user = get_infos_user(userId, ratings)
		unwatched_user = np.append(test_rating_user, unwatched_user)

		ind_sort = np.argsort(TR_ki_all_user[userId,:])[::-1]
		unwatched_user_final = []
		for ind in ind_sort :
			if ind not in watched_user:
				unwatched_user_final.append(ind)

		watched_user = np.random.choice(np.array(watched_user), size=n_film_test)
		unwatched_user_reco = unwatched_user_final[:n_film_test]
		unwatched_user_rand = np.random.choice(np.array(unwatched_user_final[n_film_test+1:]), size=n_film_test)

		watched_user_dict = { str(movieId) : dict_id_title[movieId] for movieId in watched_user } 
		reco_user_dict = { str(movieId) : dict_id_title[movieId] for movieId in unwatched_user_reco } 
		unwatched_user_dict = { str(movieId) : dict_id_title[movieId] for movieId in unwatched_user_rand }

		dataset.append((watched_user_dict, reco_user_dict, unwatched_user_dict))

	return np.array(dataset)