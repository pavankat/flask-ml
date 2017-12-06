from flask import Flask, render_template, jsonify, redirect, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    listings = [{price : 10, headline : 'abc', hood : '123'}, {price : 13, headline : 'abdc', hood : '1323'}, {price : 101, headline : '3abc', hood : '1423'} ] 
    return render_template("index.html", listings=listings) 


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
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)
