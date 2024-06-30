from flask import Flask, render_template, request
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
import os
import boto3

app = Flask(__name__)
comprehend_client = boto3.client(
    "comprehend",
    region_name=AWS_REGION
)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def analyze_sentiment():
    if request.method=='POST':
        input = request.form["user_input"]
        # comp_detect = ComprehendDetect(boto3.client("comprehend"))
        # lang = comp_detect.detect_languages(input)
        # language_code = lang[0]['LanguageCode']

        response = comprehend_client.detect_entity(Text=text,
                                                   LanguageCode='en')

    return render_template("index.html", result=f"{response["Entities"]}")

#Insert the line below to to run on Cloud9
#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run()
    app.debug(True)

