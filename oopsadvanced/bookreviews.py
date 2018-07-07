class Book(object):
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        return repr((self.id, self.name, self.author, self.reviews))


    def add_review(self, review):
        self.reviews.append(review)


class Review:
     def __init__(self, id, description, rating):
         self.id = id
         self.description = description
         self.rating = rating

     def __repr__(self):
         return repr((self.id, self.description, self.rating))




book1 = Book(124, 'ghhjjj', 'rrr')
book1.add_review(Review(10, 'great book', 5))
book1.add_review(Review(101, "Awesome", 5))

print(book1)
#print(review1)
