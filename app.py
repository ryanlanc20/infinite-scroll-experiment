from flask import Flask,request
from flask_cors import CORS
import string
import random


app = Flask(__name__)
CORS(app)

# Create some fake search results
results = []
for i in range(10000):
    url = "https://" + "".join(random.choices(string.ascii_letters,k=random.randint(5,25)))
    desc = "".join(random.choices(string.ascii_letters,k=random.randint(15,150)))
    results.append({"url": url, "desc": desc})

@app.route("/search")
def search():
    # Default limits
    startIndex = 0
    lastIndex = 10

    if "p" in request.args:
        startIndex = int(request.args.get("p"))
        lastIndex = startIndex + 10

    if lastIndex >= len(results):
        lastIndex = len(results)

    return results[startIndex:lastIndex]

app.run()
