from flask import Flask, render_template, request
import requests, sqlite3
import time

import boto3 
import json
import os 


from dotenv import load_dotenv
from openai import OpenAI  

load_dotenv()

api_key = os.getenv("AWS_BEARER_TOKEN_BEDROCK")
access_id = os.getenv("AWS_ACCESS_KEY_ID")

app = Flask(__name__)

client = OpenAI()  

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name")
    email = request.form.get("email")
    profession = request.form.get("profession")
    experience = request.form.get("experience")
    work_type = request.form.get("work_type")
    prior_issues = request.form.get("prior_issues")


    prompt = f"""
    
    Information:
    - Profession: {profession}
    - Experience: {experience}
    - Work type: {work_type}
    - Prior issues: {prior_issues}

    Classify this applicant's risk as LOW, MEDIUM, or HIGH. Do not assume anything not provided.
    Return a json file with:
    1. Risk Level (LOW/MEDIUM/HIGH)
    2. Short Explanation. Keep it concise
    3. Key factors considered apart from information given

    Do not give a markdown file

    """

    response = client.responses.create( 
        model="openai.gpt-oss-120b", 
        input=[ 
            {
                "role": "user", 
                "content": prompt
            }
        ],
        text={
        "format": {
            "type": "json_object"
        }
    } 
    )

    print("="*65)
    print(response.output[1].content[0].text)
    print("="*65)

    result = json.dumps(response.output[1].content[0].text, indent=2)

    # convert string to json
    obj = json.loads(result)
    obj = json.loads(obj) 
    result = json.dumps(obj, indent=2)

    conn = sqlite3.connect("risk.db")
    cur = conn.cursor()

    cur.execute("""
       INSERT INTO assessments
       (name, email, profession, experience, work_type, prior_issues, result)
       VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, email, profession, experience, work_type, prior_issues, result))

    conn.commit()
    conn.close()

    return f"""
    <h2> Risk Assessment Result </h2>
    <pre>{result}</pre>
    """

def init_db():
    conn = sqlite3.connect("risk.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        profession TEXT,
        experience TEXT,
        work_type TEXT,
        prior_issues TEXT,
        result TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)