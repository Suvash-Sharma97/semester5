class Review:
    def __init__(self, productId, customerId, date, rating, content):
        self.productId = productId
        self.customerId = customerId
        self.date = date
        self.rating = rating
        self.content = content


def read_reviews_from_file(filename):
    global valid, invalid
    array_of_all_reviews = []
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split(maxsplit=4)
            if len(data) == 5 and data[3].isdigit():
                obj = Review(data[0], data[1], data[2], int(data[3]), data[4])
                array_of_all_reviews.append(obj)
    return array_of_all_reviews


def calculate_average_rating(review_list):
    product_rating_pair = {}
    average_rating = {}

    for each_review in review_list:
        if each_review.productId not in product_rating_pair:
            product_rating_pair[each_review.productId] = [0, 0]
        product_rating_pair[each_review.productId][0] += each_review.rating
        product_rating_pair[each_review.productId][1] += 1

    for product_id, rating_data in product_rating_pair.items():
        average_rating[product_id] = rating_data[0] / rating_data[1]

    return average_rating


arr = read_reviews_from_file("./reviews/review1.txt")
print(calculate_average_rating(arr))
