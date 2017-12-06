# Flask ML App
-----------------------------------

to start a new python virtual environment

$ virtualenv -p `which python3` flask-ml-app

$ source flask-ml-app/bin/activate

to shut it down:

$ deactivate

-----------------------------------

to freeze everything in your environment

$ pip freeze > requirements.txt

to uninstall something 

$ pip uninstall SomePackage

-----------------------------------

$ pip install -r requirements.txt

install everything in the requirements.txt file

-----------------------------------

# To access parameters submitted in the URL (?key=value) you can use the args attribute:

searchword = request.args.get('key', '')

-----------------------------------

request.data Contains the incoming request data as string in case it came with a mimetype Flask does not handle.

request.args: the key/value pairs in the URL query string

request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded

request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.

request.values: combined args and form, preferring args if keys overlap

-----------------------------------

It is simply as follows

For URL Query parameter, use request.args

search = request.args.get("search")
page = request.args.get("page")
For Form input, use request.form

email = request.form.get('email')
password = request.form.get('password')
For data type application/json, use request.data

# data in string format and you have to parse into dictionary
data = request.data
dataDict = json.loads(data)

-----------------------------------