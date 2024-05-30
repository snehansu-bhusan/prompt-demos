import math

class VectorDatabase:
    def __init__(self):
        self.data = {}

    def insert(self, city, vector):
        self.data[city] = vector

    def fetch(self, city):
        return self.data.get(city, None)

    def display(self):
        for city, vector in self.data.items():
            print(f"{city}: {vector}")

def euclidean_distance(vector1, vector2):
    # Assuming both vectors have 4 dimensions: [Population, Latitude, Longitude, Avg. Temperature]
    squared_diff_sum = sum((v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2))
    return math.sqrt(squared_diff_sum)

# Sample usage
if __name__ == "__main__":
    db = VectorDatabase()

    # Storing data
    db.insert("New York", [8, 40.7128, -74.0060, 55])
    db.insert("Los Angeles", [4, 34.0522, -118.2437, 70])
    db.insert("Tokyo", [9, 35.6895, 139.6917, 60])

    # Displaying data
    print("Data in Vector Database:")
    db.display()

    # Fetching data
    city = "New York"
    vector = db.fetch(city)
    if vector:
        print(f"\nVector for {city}: {vector}")
    else:
        print(f"\n{city} not found in the database")

    # Calculating Euclidean distance
    city1 = "New York"
    city2 = "Los Angeles"
    vector1 = db.fetch(city1)
    vector2 = db.fetch(city2)
    if vector1 and vector2:
        distance = euclidean_distance(vector1, vector2)
        print(f"\nEuclidean distance between {city1} and {city2}: {distance}")
    else:
        print(f"\nEither {city1} or {city2} not found in the database")
