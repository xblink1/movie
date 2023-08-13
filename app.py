from bottle import Bottle, run, template

app = Bottle()

@app.route('/')
def index():
    return "Welcome to the Movie Recommendation System!"

@app.route('/recommend')
def recommend():
    # Your recommendation system logic here
    # Replace this with your actual recommendation logic
    movie_recommendation = "Movie 1, Movie 2, Movie 3"
    return template("Recommended movies: {{ movies }}", movies=movie_recommendation)

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080)
    
