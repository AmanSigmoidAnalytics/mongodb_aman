import pymongo

# Manually enter user data
user_data = {
    "_id": {"oid": "59b99db5cfa9a34dcd788597"},
    "name": "Aman Pandey",
    "email": "amanpandey3007@gmail.com",
    "password": "$2b$12$6vz7wiwO.EI5Rilvq1zUc./9480gb1uPtXcahDxIadgyC3PS8XCUK"
    # Add other fields as needed
}

theater_data = {
    "_id": {"oid": "59a47286cfa9a3a73f24e73c"},
    "theaterId": {"$numberInt": "10000"},
    "location": {
        "address": {
            "street1": "1-B Whitefield rose layout",
            "city": "Bangalore",
            "state": "KN",
            "zipcode": "560037"
        },
        "geo": {
            "type": "Point",
            "coordinates": [
                {"$numberDouble": "-93.24565"},
                {"$numberDouble": "44.85466"}
            ]
        }
    }
}


movies_data={
        "_id": {
            "oid": "573a1390x49313caabcd7632"
        },
        "plot": "Kung Fu Panda.",
        "genres": [
            "Animated"
        ],
        "runtime": {
            "$numberInt": "2"
        },
        "cast": [
            "Po",
            "Shifu"
        ],
        "num_mflix_comments": {
            "$numberInt": "1"
        },
        "title": "Blacksmith Scene",
        "fullplot": "A stationary camera looks at a large anvil with a blacksmith behind it and one on either side. The smith in the middle draws a heated metal rod from the fire, places it on the anvil, and all three begin a rhythmic hammering. After several blows, the metal goes back in the fire. One smith pulls out a bottle of beer, and they each take a swig. Then, out comes the glowing metal and the hammering resumes.",
        "countries": [
            "USA"
        ],
        "released": {
            "$date": {
                "$numberLong": "-2418768000000"
            }
        },
        "directors": [
            "William K.L. Dickson"
        ],
        "rated": "UNRATED",
        "awards": {
            "wins": {
                "$numberInt": "1"
            },
            "nominations": {
                "$numberInt": "0"
            },
            "text": "1 win."
        },
        "lastupdated": "2015-08-26 00:03:50.133000000",
        "year": {
            "$numberInt": "1893"
        },
        "imdb": {
            "rating": {
                "$numberDouble": "6.2"
            },
            "votes": {
                "$numberInt": "1189"
            },
            "id": {
                "$numberInt": "5"
            }
        },
        "type": "movie",
        "tomatoes": {
            "viewer": {
                "rating": {
                    "$numberInt": "3"
                },
                "numReviews": {
                    "$numberInt": "184"
                },
                "meter": {
                    "$numberInt": "32"
                }
            },
            "lastUpdated": {
                "$date": {
                    "$numberLong": "1435516449000"
                }
            }
        }
    }


comments_data={
        "_id": {
            "oid": "5a9427648b0xkkbeb67579cc"
        },
        "name": "Aman Pandey",
        "email": "amanpandey3007@gmail.com",
        "movie_id": {
            "$oid": "573a1390f29313caabcd418c"
        },
        "text": "Superb.",
        "date": {
            "$date": {
                "$numberLong": "1332804016000"
            }
        }
}

# Establish MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mongodb_assignment_aman"]

# Define functions to insert data into MongoDB collections
def insert_new_comment(comments_data):
    db.comments.insert_one(comments_data)

def insert_new_movie(movies_data):
    db.movies.insert_one(movies_data)

def insert_new_theater(theater_data):
    db.theaters.insert_one(theater_data)

def insert_new_user(user_data):
    db.users.insert_one(user_data)


# Call the functions to insert data
insert_new_comment(comments_data)
insert_new_movie(movies_data)
insert_new_theater(theater_data)
insert_new_user(user_data)


