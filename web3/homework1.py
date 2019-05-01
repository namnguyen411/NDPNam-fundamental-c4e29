from pymongo import MongoClient
from bson.objectid import ObjectId
import matplotlib.pyplot as plt

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.c4e
# posts = db.posts

# post = [
#         {'title' : 'Để cho anh khóc - C4E29',
#         'author' : 'Lê Bảo Bình',
#         'content': 'Có bao giờ em nghĩ về anh Về những đắng cay anh đang gánh chịu'
# }]

# posts.insert_many(post)

data = db.customers
x = data.count({'ref':'events'})
y = data.count({'ref':'ads'})
z = data.count({'ref':'wom'}) 
labels = ['events', 'advertisements', 'word of mouth']
sizes = [x, y, z]
colors = ['red', 'blue', 'yellow']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.show()