from flask import Flask, render_template, request, make_response
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
import json
import boto3
from aws_comprehend_detect import ComprehendDetect

app = Flask(__name__)
comprehend_client = boto3.client(
    "comprehend",
    region_name=AWS_REGION
)


def format_entities(entities_string):
    
    entities = response['Entities']
    formatted_text = ""
    count = 1
    
  # Define the regular expression pattern (adjust based on your entity data format)
  formatted_text = f"Detect Entities: {len(entities)}"
  for entity in entities:
      formatted_text += f"\n\n{count}: {entity['Text']}\n"
      for e in entity:
        formatted_text += f"{e}: {entity[e]}\n"
      count += 1

  return formatted_text

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/detect_entity", methods=["GET", "POST"])
def analyze_sentiment():
    if request.method=='POST':
        input = request.form["user_input"]
        
        comp_detect = ComprehendDetect(comprehend_client)
        lang = comp_detect.detect_languages(input)
        language_code = lang[0]['LanguageCode']

        entities = comprehend_client.detect_entities(Text=input,
                                                   LanguageCode=language_code)
        pos = comprehend_client.detect_syntax(Text=input,
                                                   LanguageCode=language_code)

        #t = "[{'Score': 0.9994252920150757, 'Type': 'PERSON', 'Text': 'Barack Obama', 'BeginOffset': 0, 'EndOffset': 12}, {'Score': 0.8225329518318176, 'Type': 'QUANTITY', 'Text': '44th president', 'BeginOffset': 18, 'EndOffset': 32}]"
        return render_template("index.html", text=input, NER=format_entities(entities), POS=pos)
    
#Insert the line below to to run on Cloud9
#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    app.debug(True)

