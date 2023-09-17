import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import accuracy

# Load the MovieLens dataset (replace with your dataset)
# Dataset source: https://grouplens.org/datasets/movielens/
data = pd.read_csv('C:\\Users\\Elitebook\\Desktop\\codsoft\\codsoft tasks\\task4\\movielens\\ml-latest-small\\ratings.csv')


# Define the rating scale (e.g., 1 to 5)
reader = Reader(rating_scale=(1, 5))

# Load the data into the Surprise format
data = Dataset.load_from_df(data[['userId', 'movieId', 'rating']], reader)

# Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.2)

# Use the SVD algorithm for collaborative filtering
model = SVD()

# Train the model on the training set
model.fit(trainset)

# Make predictions on the testing set
predictions = model.test(testset)

# Evaluate the model using RMSE (Root Mean Squared Error)
rmse = accuracy.rmse(predictions)
print('RMSE:', rmse)

# Function to recommend movies for a user
def get_top_n_recommendations(predictions, n=10):
    top_n = {}
    for uid, iid, true_r, est, _ in predictions:
        if est >= 3.5:  # Recommend if estimated rating is above a threshold (e.g., 3.5)
            if uid not in top_n:
                top_n[uid] = []
            top_n[uid].append((iid, est))

    # Sort recommendations by estimated rating
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

# Get top N recommendations for a user (replace user_id with an actual user ID)
user_id = 1  # Replace with the user ID for whom you want to get recommendations
user_recommendations = get_top_n_recommendations(predictions, n=10).get(user_id, [])

# Print the top N recommendations for the user
print(f"Top recommendations for user {user_id}:")
for movie_id, est_rating in user_recommendations:
    print(f"Movie ID: {movie_id}, Estimated Rating: {est_rating}")
