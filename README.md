# Flask ML App

see deployed website here: 
https://radiant-scrubland-39025.herokuapp.com/

Housing Price Estimator

This app takes in a user's information about their house and predicts the price of their house using a Gradient Boosting model with huber loss and 1000 regression trees of depth 6.

Technologies used: Flask 0.12.2, Python 3, sklearn, pandas

http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html

## How to deploy your flask app

1. install the virtualenv python package

```
$ pip install virtualenv
```

2. Create a virtual environment using python 3 and update name-goes-here to the name of your virtual environment. You should do this in the directory of your app.

```
$ virtualenv -p `which python3` name-goes-here
```

3. install all your python packages 

```
$ pip install ...
```

replace the ... with a package you used. Repeat until you have no more packages to install. 

The packages are being installed to your virtual environment.

4. make sure you install gunicorn for your deployed app

```
$ pip install gunicorn
```

5. freeze your python package versions (dependencies) into a requirements.txt file

```
$  pip install -r requirements.txt
```

6. make sure you have a Procfile with its contents like in this repository

7. make sure your app.py file's bottom looks like this:

```
if __name__ == "__main__":
    app.run()
```

8. make a gitignore file and ignore your virtual environment folder. It's whatever you named your python virtual environment. You'll see a new folder.

You're basically creating a .gitignore file like I have (yes it has no filename)

9. create an aws instance with heroku in your app's directory:

```
$ heroku create
```

10. push up any changes to github

```
$ git add .
$ git commit -m 'get ready to deploy'
$ git push origin master
```

11. deploy to heroku

```
$ git push heroku master
```

12. open your site in the browser

```
$ heroku open
```
-----------------------------------

## How to start up app

1. to start this up, start a new python 3 virtual environment:

```
$ virtualenv -p `which python3` flask-ml-app
```

2. install all of the dependencies

```
$  pip install -r requirements.txt
```

3. start up the app

```
$  python app.py
```

## quick code snippets

-----------------------------------

#### to start a new python virtual environment

```
$ virtualenv -p `which python3` flask-ml-app

$ source flask-ml-app/bin/activate
```

#### to shut it down:

```
$ deactivate
```

-----------------------------------

#### to freeze dependencies of your virtual environment to a requirements.txt file 

```
$ pip freeze > requirements.txt
```

#### to uninstall something 

```
$ pip uninstall SomePackage
```

-----------------------------------

#### install everything from the requirements.txt file

```
$ pip install -r requirements.txt
```

-----------------------------------

#### To access parameters submitted in the URL (?key=value) you can use the args attribute:

```
searchword = request.args.get('key', '')
```

-----------------------------------

#### different ways to get data from a form in a flask endpoint

request.data Contains the incoming request data as string in case it came with a mimetype Flask does not handle.

request.args: the key/value pairs in the URL query string

request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded

request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.

request.values: combined args and form, preferring args if keys overlap

-----------------------------------

#### detailed information about how to get data from forms in a flask endpoint

For URL Query parameter, use request.args

```
search = request.args.get("search")
page = request.args.get("page")
```

For Form input, use request.form

```
email = request.form.get('email')
password = request.form.get('password')
```

For data type application/json, use request.data

```
# data in string format and you have to parse into dictionary
data = request.data
dataDict = json.loads(data)
```

-----------------------------------