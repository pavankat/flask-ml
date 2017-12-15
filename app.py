from flask import Flask, render_template, jsonify, redirect, request

from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html") 

@app.route("/scrape", methods=['GET']) 
def scrape():
    listings = mongo.db.listings
    listings_data = scrape_craigslist.scrape()
    listings.update(
        {},
        listings_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

@app.route('/get-user-data', methods=['POST'])
def predict_stuff():
    if request.method == 'POST':
        model = joblib.load('trained_house_classifier_model.pkl')

        print('-----line 27--------')
        print(request.form.get('year_built'))

        year_built = int(request.form.get('year_built'))

        print('line 31')

        stories = int(request.form.get('stories'))
        num_bedrooms = int(request.form.get('num_bedrooms'))
        full_bathrooms = int(request.form.get('full_bathrooms'))
        half_bathrooms = int(request.form.get('half_bathrooms'))
        livable_sqft = int(request.form.get('livable_sqft'))
        total_sqft = int(request.form.get('total_sqft'))
        garage_sqft = int(request.form.get('garage_sqft'))

        carport_sqft = int(request.form.get('carport_sqft'))
        has_fireplace = request.form.get('has_fireplace')

        has_pool = request.form.get('has_pool')

        has_central_heating = request.form.get('has_central_heating')

        has_central_cooling = request.form.get('has_central_cooling')


        has_fireplace = request.form.get('has_fireplace')

        garage_type = request.form.get('garage_type')
 
        city = request.form.get('city')

        house_to_value = [
            # House features
            year_built,   # year_built
            stories,      # stories
            num_bedrooms,      # num_bedrooms
            full_bathrooms,      # full_bathrooms
            half_bathrooms,      # half_bathrooms 
            livable_sqft,   # livable_sqft
            total_sqft,   # total_sqft
            garage_sqft,      # garage_sqft
            carport_sqft,      # carport_sqft
            1 if (has_fireplace == 'on') else 0,   # has_fireplace
            1 if (has_pool == 'on') else 0,  # has_pool
            1 if (has_central_heating == 'on') else 0,   # has_central_heating
            1 if (has_central_cooling == 'on') else 0,   # has_central_cooling
            
            # Garage type: Choose only one
            1 if (garage_type == 'attached') else 0,      # attached
            1 if (garage_type == 'detached') else 0,      # detached
            1 if (garage_type == 'none') else 0,      # none
            
            # City: Choose only one
            1 if (city == 'Amystad') else 0,      # Amystad
            1 if (city == 'Brownport') else 0,      # Brownport
            1 if (city == 'Chadstad') else 0,      # Chadstad
            1 if (city == 'Clarkberg') else 0,      # Clarkberg
            1 if (city == 'Coletown') else 0,      # Coletown
            1 if (city == 'Davidfort') else 0,      # Davidfort
            1 if (city == 'Davidtown') else 0,      # Davidtown
            0,      # East Amychester
            0,      # East Janiceville
            0,      # East Justin
            0,      # East Lucas
            0,      # Fosterberg
            0,      # Hallfort
            0,      # Jeffreyhaven
            0,      # Jenniferberg
            0,      # Joshuafurt
            0,      # Julieberg
            0,      # Justinport
            0,      # Lake Carolyn
            0,      # Lake Christinaport
            0,      # Lake Dariusborough
            0,      # Lake Jack
            0,      # Lake Jennifer
            0,      # Leahview
            0,      # Lewishaven
            0,      # Martinezfort
            0,      # Morrisport
            0,      # New Michele
            0,      # New Robinton
            0,      # North Erinville
            0,      # Port Adamtown
            0,      # Port Andrealand
            0,      # Port Daniel
            0,      # Port Jonathanborough
            0,      # Richardport
            0,      # Rickytown
            0,      # Scottberg
            0,      # South Anthony
            0,      # South Stevenfurt
            0,      # Toddshire
            0,      # Wendybury
            0,      # West Ann
            0,      # West Brittanyview
            0,      # West Gerald
            0,      # West Gregoryview
            0,      # West Lydia
            0       # West Terrence
        ]

        # scikit-learn assumes you want to predict the values for lots of houses at once, so it expects an array.
        # We just want to look at a single house, so it will be the only item in our array.
        homes_to_value = [
            house_to_value
        ]

        # return render_template("index.html", pred=house_to_value) 

        # Run the model and make a prediction for each house in the homes_to_value array
        predicted_home_values = model.predict(homes_to_value)

        # Since we are only predicting the price of one house, just look at the first prediction returned
        predicted_value = predicted_home_values[0]

        return render_template("index.html", pred=predicted_value) 


if __name__ == "__main__":
    app.run()
