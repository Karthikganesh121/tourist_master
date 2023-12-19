from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('kerala_tourist_accommodation_details.csv')

# List of Cities in Kerala
cities = [
    "Thiruvananthapuram (Trivandrum)",
    "Kochi (Cochin)",
    "Kozhikode (Calicut)",
    "Munnar",
    "Alappuzha (Alleppey)",
    "Wayanad",
    "Kumarakom",
    "Thekkady",
    "Kannur",
    "Thrissur"
]
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')
@app.route('/templates/index.html', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        max_price = float(request.form['max_price'])
        city = request.form['city']

        # Filter based on user input
        filtered_df = df[(df['Price per Night (INR)'] <= max_price) & (df['City'] == city)]

        # Sorting by price to get the nearest option in terms of pricing
        filtered_df = filtered_df.sort_values(by='Price per Night (INR)')

        # Convert DataFrame to HTML
        result = filtered_df.to_html(classes='table table-striped')

        return render_template('index.html', cities=cities, result=result)


    return render_template('index.html', cities=cities)

if __name__ == '__main__':
    app.run(debug=True)
