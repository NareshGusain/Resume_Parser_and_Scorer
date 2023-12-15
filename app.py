import os 
from flask import Flask, render_template, redirect, url_for, request, session, flash, app, Blueprint, jsonify
import json
import function 

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def main():
    return render_template('index.html')

@app.route('/parse', methods=['POST','GET'])
def parse():

    if 'resumeFile' not in request.files:
        return jsonify({'error': 'No resume file uploaded'})
    
    resume_file = request.files['resumeFile']
    
    text_data = function.extract_text_from_pdf(resume_file)

    print(text_data)

    # job_description = request.form.get('jobDescription')
    return jsonify({'success': 'Resume parsed successfully'})

if __name__ == '__main__':
    app.run(debug=True)


