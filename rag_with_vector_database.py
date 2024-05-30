import openai
import math

# Set up OpenAI API key
openai.api_key = 'your_openai_api_key'

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
    squared_diff_sum = sum((v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2))
    return math.sqrt(squared_diff_sum)

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def get_city_info(db, city):
    vector = db.fetch(city)
    if vector:
        return f"{city}: Population {vector[0]} million, Latitude {vector[1]}, Longitude {vector[2]}, Avg. Temperature {vector[3]}°F"
    else:
        return f"Sorry, I don't have information about {city}."

if __name__ == "__main__":
    db = VectorDatabase()

    # Storing data
    db.insert("New York", [8, 40.7128, -74.0060, 55])
    db.insert("Los Angeles", [4, 34.0522, -118.2437, 70])
    db.insert("Tokyo", [9, 35.6895, 139.6917, 60])

    # Humanized Bot Example
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # Fetch city information if asked
        if "info about" in user_input.lower():
            city = user_input.split("info about")[1].strip()
            city_info = get_city_info(db, city)
            print(f"Bot: {city_info}")
            continue

        # Generate human-like response using GPT-3.5
        response = generate_response(user_input)
        print(f"Bot: {response}")
