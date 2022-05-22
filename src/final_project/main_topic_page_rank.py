from global_ import *
from global_var_ import PATH, DATASET_TYPE, TRAIN_SIZE


# Small: 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users.
# Average computation time without optimization : 10s/user --> 6100s --> less than 2 hours
# Full: 27,000,000 ratings and 1,100,000 tag applications applied to 58,000 movies by 280,000 users.
# Average computation time without optimization : 

# Loading data
movies, ratings = load_data(PATH, DATASET_TYPE)

# Preprocessing data
movies, ratings = clear_dataset(movies, ratings)
movies = one_hot_encode_genres(movies)
ratings = preprocess_ratings(ratings)

# Building matrix
R_uk, tmp_M, P_ig, M_csr, train_rating_user_list, test_rating_user_list = init(movies, ratings, TRAIN_SIZE)

# Run the algorithm
n_user = len(np.unique(ratings["userId"]))
n_user = 3 ## Use when testing
TR_ki_all_user = iterative_TR_ki(n_user, R_uk, tmp_M, P_ig, M_csr, d=0.15, alpha=0.1, iter_max=15)

# Running some test for a test user
test_user_id = 1

print("TR_ki_all_user shape:", TR_ki_all_user.shape)
print("test_rating_user_list shape:", test_rating_user_list.shape)
print("TR_ki for test user :\n", TR_ki_all_user[test_user_id, :10])

sorted_movies_all_user = sort_by_best_movie(TR_ki_all_user)
print("sorted_movies_all_user shape:", sorted_movies_all_user.shape)
print("Sorted best movies recommandation for test user :\n", sorted_movies_all_user[test_user_id,:10])

# Running some test for the DOA metrics before computing it on whole user list
print(test_doa_user(1, 4, TR_ki_all_user, test_rating_user_list, ratings))

# Computing final DOA metric for the whole dataset
print("DOA for all users :", compute_all_doa(TR_ki_all_user, test_rating_user_list, ratings))

# Computing final DOA metric for the whole dataset
dataset = build_experimental_dataset(movies, ratings, TR_ki_all_user, train_rating_user_list, test_rating_user_list, n_user, n_film_test=5)

# Testing our experiment dataset
userId = 30
print(dataset[userId])
userId = 60
print(dataset[userId])
userId = 50
print(dataset[userId])

test = []
for i in range(len(dataset[:,1])):
	test.append(list(dataset[:,1][i].values()))
test = np.array(test).flatten()

print(len(np.unique(test, return_counts=True)[0]), "movies recommanded for all our users with a database of", TR_ki_all_user.shape[1], "movies")
# np.unique(test, return_counts=True)

userId = 1
print(dataset[userId])

n_user_experiment = 50
print(dataset[:n_user_experiment])

print(np.array(dataset[:n_user_experiment]).shape)