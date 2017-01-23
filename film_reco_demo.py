import numpy as np 
from lightfm.datasets import fetch_movielens
from lightfm import LightFM 

#fetch and format data
data = fetch_movielens(min_rating=4.0)

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
# WARP stands for Weighted Approximate Rate Pairwise and uses the 
# gradient descent algo to iteratively discover weights to improve
# prediction over time, and represents a hybrid system which takes
# both content and collaborative into account.
model = LightFM(loss='warp')

#train model
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):

	#number of users and films in the training data
	n_users, n_items = data['train'].shape

	#generate recommendations for each user input
	for user_id in user_ids:

		#films they already like
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

		#films our model predicts they will like
		scores = model.predict(user_id, np.arange(n_items))

		#rank predicted films in descending order
		top_items = data['item_labels'][np.argsort(-scores)]

		#print results
		print("User %s" % user_id)
		print ("	Known positives:")

		for x in known_positives[:3]:
			print("			%s" % x)

		print("			Recommended:")

		for x in top_items[:3]:
			print("			%s" % x)

sample_recommendation(model, data, [3,25,450])

