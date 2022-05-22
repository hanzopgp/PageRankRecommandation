from global_ import *
from global_var_ import MINIMUM_SEEN_MOVIES, MINIMUM_SEEN_USERS

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.preprocessing import MultiLabelBinarizer
import scipy
from tqdm import tqdm
import itertools as it


# Loading data
def load_data(path, dataset_type="small"):
	if dataset_type == "small":
		movies = pd.read_csv(path + "ml-latest-small/movies.csv")
		ratings = pd.read_csv(path + "ml-latest-small/ratings.csv")
	elif dataset_type == "full":
		movies = pd.read_csv(path + "ml-latest/movies.csv")
		ratings = pd.read_csv(path + "ml-latest/ratings.csv")
	return movies, ratings

# Preprocessing data

# Delete films seen only by a certain number of users
def get_id_delete_solo_films(data, threshold, nom_colonne) :
    '''
    data -> movies ou ratings ( dataframe qui contient une colonne movieId )
    '''
    list_key_values = np.array(list(Counter(data[nom_colonne].values).items()))
    key,values = list_key_values[:,0],list_key_values[:,1]
    id_delete =  np.where(values < threshold)[0]
    return key[id_delete]

def delete_solo_films(data,id_delete,nom_colonne) :
    '''
    data -> movies ou ratings ( dataframe qui contient une colonne movieId )
    '''
    array_movieId = data[nom_colonne].values
    ind = [i for i in range(len(array_movieId)) if array_movieId[i] not in id_delete ]
    return data.iloc[ind]

# Building ratings and movies dataframe which both contains the same movieId
def clear_dataset(movies, ratings):

	id_delete = get_id_delete_solo_films(ratings, MINIMUM_SEEN_MOVIES,'movieId')
	ratings = delete_solo_films(ratings,id_delete,'movieId')
	movies = delete_solo_films(movies,id_delete,'movieId')
	id_delete = get_id_delete_solo_films(ratings, MINIMUM_SEEN_USERS,'userId')
	ratings = delete_solo_films(ratings,id_delete,'userId')
	
	list_movieId = list(set(movies["movieId"].values).intersection(set(ratings["movieId"].values)))
	movies_old = movies['movieId'].values
	l = []
	for i in range(len(movies_old)):
		if movies_old[i] in list_movieId:
			l.append(i)
	movies = movies.iloc[l,:]

	a = sorted(list(list_movieId))
	b = range(len(a))
	d = dict(zip(a,b))
	movies = movies.replace({'movieId' : d})

	a = sorted(list(list_movieId))
	b = range(len(a))
	d = dict(zip(a,b))
	ratings = ratings.replace({'movieId' : d})
    
	ratings.index = range(len(ratings))
	movies.index = range(len(movies))

	return movies, ratings

# Building one hot encoded genres in movies dataframe
def one_hot_encode_genres(movies):
	tmp = []
	for elt in movies["genres"]:
		tmp.append(elt.split("|"))
	movies["genres"] = tmp
	mlb = MultiLabelBinarizer(sparse_output=True)
	movies = movies.join(
				pd.DataFrame.sparse.from_spmatrix(
												mlb.fit_transform(movies.pop('genres')),
												index=movies.index,
												columns=mlb.classes_))
	return movies

# Cleaning ratings datagrame
def preprocess_ratings(ratings):
	ratings = ratings.drop(columns=["timestamp"])
	ratings['userId'] = ratings['userId'].to_numpy() - 1 # car pas de user 0
	return ratings

# Split for computing metrics on test later
def split_set(userId, train_size, ratings):
	rating_user = ratings[ratings["userId"] == userId]
	train_rating_user, test_rating_user = rating_user.to_numpy()[:int(train_size*len(rating_user))], rating_user.to_numpy()[int(train_size*len(rating_user)):]
	return train_rating_user, test_rating_user

# Get informations on users watched/unwatched movies...
def get_infos_user(userId, ratings):
	watched_user = set(ratings[ratings["userId"] == userId]["movieId"])
	watched_all = set(ratings['movieId'])
	unwatched_user = list(watched_all.difference(watched_user))
	return watched_user, watched_all, unwatched_user

# Building matrix

# Building a matrix M = (n_movies, n_movies) which contains the number of users who'se seen m_i and m_j
def build_M_matrix(ratings, train_size):
	data_dict = dict()
	train_rating_user_list = []
	test_rating_user_list = []
	for userId in tqdm(set(ratings["userId"])):
		train_rating_user, test_rating_user = split_set(userId, train_size, ratings)
		train_rating_user_list.append(np.array(train_rating_user))
		test_rating_user_list.append(np.array(test_rating_user))
		iterator = it.combinations(train_rating_user[:,1], 2)
		for x, y in iterator:
			data_dict[(x,y)] = data_dict.get((x,y), 0.) + 1.
			data_dict[(y,x)] = data_dict.get((y,x), 0.) + 1.
		iterator = it.combinations(test_rating_user[:,1], 2)
		for x, y in iterator:
			# We need to ignore the test movies
			data_dict[(x,y)] = 0
			data_dict[(y,x)] = 0
	keys = np.array(list(data_dict.keys())).astype(int)
	values = np.array(list(data_dict.values())).astype(float)
	M_coo = scipy.sparse.coo_matrix((values, (keys[:,0], keys[:,1])))
	M_csr = M_coo.tocsr()
	M_norm = M_csr
	return M_norm, train_rating_user_list, test_rating_user_list

# Computing probabilites of genres P_ig
def build_P_ig(movies):
	sum_ = movies[[i for i in movies.columns if i != "movieId" and i != "title"]].to_numpy().sum(axis=0).astype(int)
	P_ig = sum_ / sum(sum_)
	return P_ig.reshape(-1, 1)

# Initialisation of R_uk before iterative algorithm
def init_R_uk(movies):
	n_genres = len(movies.columns) - 2
	n_movies = len(movies)
	r = 1/(n_movies*n_genres)
	R_uk = np.full((n_movies, n_genres), r)
	return R_uk

# Computing F_ig for each user
def build_F_ig(R_uk, P_ig):
	F_ig = np.sum(R_uk, axis=1).reshape(-1,1) @ P_ig.reshape(1,-1)
	return F_ig

# Matrix user X movie
def build_ratings_matrix(ratings):
	values = ratings["rating"]
	rows = ratings["userId"]
	cols = ratings["movieId"]
	M_coo = scipy.sparse.coo_matrix((values, (rows, cols)))
	M_csr = M_coo.tocsr()
	return M_csr

# Build I_uk for each user
def build_I_uk(tmp_M, id_user, P_ig):
	I_uk = tmp_M[id_user,:].T @ P_ig.reshape(1,-1)
	I_uk = I_uk / I_uk.sum(axis=0).T
	return I_uk

# Init the matrix needed before running the iterative algorithm
def init(movies, ratings, train_size):
	print("Init R_uk...")
	R_uk = init_R_uk(movies)
	print(R_uk.shape)
	print("Building P_ig...")
	tmp_M = build_ratings_matrix(ratings)
	P_ig = build_P_ig(movies)
	print(P_ig.shape)
	print("Building M_csr...")
	M_csr, train_rating_user_list, test_rating_user_list = build_M_matrix(ratings, train_size)
	print(M_csr.shape)
	return R_uk, tmp_M, P_ig, M_csr, np.array(train_rating_user_list, dtype=object), np.array(test_rating_user_list, dtype=object)

# Run the algorithm

# Compute TR_ki for a specific user
def compute_TR_ki(id_user, R_uk, tmp_M, P_ig, M_csr, d, alpha, iter_max):
	I_uk = build_I_uk(tmp_M, id_user, P_ig)
	for _ in range(iter_max):
		F_ig = build_F_ig(R_uk, P_ig)
		R_uk = d * alpha * M_csr @ R_uk + d * (1-alpha) * M_csr @ F_ig + (1-d) * I_uk

		# This part is useful if you want to normalize + break if converge
		# R_uk = (R_uk / R_uk.sum(axis=1)).T # Normalization isn't working
		#     print(np.abs(np.sum(R_uk - R_uk_old)))
		#     if np.abs(np.sum(R_uk - R_uk_old)) < eps :
		#         print(i)
		#         break
		# R_uk_old = R_uk.copy()
	
	TR_ki = np.array(R_uk @ P_ig) # It returns a np.mat object which can't be reduced to dimension 1
	return TR_ki.reshape(-1)

# Compute TR_ki for all users
def iterative_TR_ki(n_user, R_uk, tmp_M, P_ig, M_csr, d=0.15, alpha=0.1, iter_max=5):
	print("Computing TR_ki for all users...")
	TR_ki_all_user = []
	for id_user in tqdm(range(n_user)):
		TR_ki_all_user.append(compute_TR_ki(id_user, R_uk, tmp_M, P_ig, M_csr, d, alpha, iter_max))
	return np.array(TR_ki_all_user)

# Running some test for a test user

# Returns the recommandation for the users
def sort_by_best_movie(TR_ki_all_user):
	sorted_movies_all_user = np.zeros_like(TR_ki_all_user)
	for i in range(len(TR_ki_all_user)):
		sorted_movies_all_user[i,:] = np.argsort(TR_ki_all_user[i,:])[::-1]
	return sorted_movies_all_user

