import os
from collections import defaultdict

class Review:
    def __init__(self, productId, cId, date, rating, text):
        self.productId = productId
        self.cId = cId
        self.date = date
        self.rating = rating
        self.text = text

invalid = 0
valid = 0

# Sets and lists to store the required data
product_ids = set()
customer_ids = set()
review_dates = set()
ratings = []
messages = []

def read_reviews_from_file(filename):
    global invalid, valid
    reviews = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(maxsplit=4)
            if len(data) == 5:
                productId, cId, date, rating, text = data
                try:
                    rating = int(rating)
                    reviews.append(Review(productId, cId, date, rating, text))
                    
                    # Collecting data
                    product_ids.add(productId)
                    customer_ids.add(cId)
                    review_dates.add(date)
                    ratings.append(rating)
                    messages.append(text)
                    
                    valid += 1
                except ValueError:
                    invalid += 1
            else:
                invalid += 1
    return reviews

def calculate_average(reviews):
    product_ratings = defaultdict(list)

    for review in reviews:
        product_ratings[review.productId].append(review.rating)

    average_ratings = {}
    for productId, ratings in product_ratings.items():
        average_ratings[productId] = sum(ratings) / len(ratings) if ratings else 0.0

    return average_ratings

folder_path = '/home/suvash/Desktop/python/reviews'
all_reviews = []

if os.path.isdir(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            all_reviews.extend(read_reviews_from_file(file_path))
else:
    print(f"Error: {folder_path} is not a valid directory.")

average_ratings = calculate_average(all_reviews)
sorted_average_ratings = sorted(average_ratings.items(), key=lambda x: x[1], reverse=True)

# Print the average ratings for all products
for productId, avg_rating in average_ratings.items():
    print(f"Product ID: {productId}, Average Rating: {avg_rating:.2f}")

# Print the top three products based on average ratings
print("\nTop 3 Products Based on Average Ratings:")
for productId, avg_rating in sorted_average_ratings[:3]:
    print(f"Product ID: {productId}, Average Rating: {avg_rating:.2f}")

# Print the collected data
print(f"\nValid reviews: {valid}, Invalid reviews: {invalid}")
print()
print()
print(f"All product IDs: {product_ids}")
print()
print(f"All customer IDs: {customer_ids}")
print()
print(f"All review dates: {review_dates}")
print()
print(f"All ratings: {ratings}")
print()
print(f"All messages: {messages}")
