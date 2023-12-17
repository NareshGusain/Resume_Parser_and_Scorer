import os 
from flask import Flask, render_template, redirect, url_for, request, session, flash, app, Blueprint, jsonify
import json
import function 

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def main():
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse():
    resume_file = None  # Initialize the variable
    if 'resumeFile' not in request.files or request.files['resumeFile'].filename == '':
        return jsonify({'error': 'No resume file uploaded'})
    
    if (request.method == "POST"):
        resume_file = request.files['resumeFile']
    
    text_data = function.extract_text_from_pdf(resume_file)
    skills = function.extract_skills(text_data)
    experience = function.extract_experience(text_data)

    job_description = request.form.get('jobDescription','')
    print(job_description)

    return render_template('index.html', experience=experience, skills=skills, job_description=job_description)

if __name__ == '__main__':
    app.run(debug=True)


