# cv_generator.py

def generate_cv(name, education, experience, skills):
    cv_content = f"""
    # {name}'s CV

    ## Education
    - {education}

    ## Experience
    - {experience}

    ## Skills
    - {skills}
    """

    return cv_content

# Example data
name = "John Doe"
education = "Bachelor's in Computer Science, University of XYZ (Year - Year)"
experience = "Software Developer, ABC Company (Year - Present)\n  - Developed web applications using HTML, CSS, and JavaScript."
skills = "Programming Languages: Python, Java\nWeb Development: HTML, CSS, JavaScript"

# Generate the CV
generated_cv = generate_cv(name, education, experience, skills)

# Save the CV to a file (e.g., cv.md)
with open('cv.md', 'w') as file:
    file.write(generated_cv)

print("CV generated successfully!")
