import PyPDF2
import re

#Function to extract data from pdf 
def extract_text_from_pdf(pdf_file):
    if isinstance(pdf_file, str):  # If the input is a file path
        with open(pdf_file, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page_obj = pdf_reader.pages[page_num]
                text += page_obj.extract_text()
        return text
    elif hasattr(pdf_file, 'read'):  # If the input is a FileStorage object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text
    else:
        raise ValueError('Invalid input. Expected file path or FileStorage object.')



#Extract Name
def extract_name(text_data):
    name_pattern = re.compile(r'^\s*([\w\s]+)\s*@')
    name_match = name_pattern.search(text_data)
    name = name_match.group(1) if name_match else None
    return name

# Extract Email
def extract_email(text_data):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    email_match = email_pattern.search(text_data)
    email = email_match.group() if email_match else None
    return email

# Extract Experience
def extract_experience(text_data):
    experience_pattern = re.compile(r'\bEXPERIENCE\b(.+?)\bSKILLS\b', re.DOTALL)
    experience_match = experience_pattern.search(text_data)
    experience = experience_match.group(1).strip() if experience_match else None
    return experience

# Extract Skills
def extract_skills(text_data):
    skills_pattern = re.compile(r'\bSKILLS\b(.+)', re.DOTALL)
    skills_match = skills_pattern.search(text_data)
    skills = skills_match.group(1).strip() if skills_match else None
    return skills
