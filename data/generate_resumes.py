import os
import random

os.makedirs("data/resumes", exist_ok=True)

names = [
    "Aman Sharma","John Doe","Sarah Khan","Raj Verma","Priya Singh",
    "Rohan Gupta","Neha Jain","Arjun Mehta","Simran Kaur","Vikas Patel",
    "Rahul Yadav","Sneha Kapoor","Karan Malhotra","Pooja Sharma","Nikhil Das",
    "Ananya Roy","Harsh Vardhan","Deepak Kumar","Meera Joshi","Aditya Rana",
    "Ritika Sen","Yash Arora","Tanya Bhatia","Mohit Saini","Kriti Nair",
    "Dev Malviya","Shivam Tyagi","Naina Gupta","Varun Jain","Ishita Bose"
]

skill_sets = [
    ["Python","SQL","AWS","Flask"],
    ["Java","Spring Boot","MySQL"],
    ["React","JavaScript","CSS","HTML"],
    ["Python","Machine Learning","TensorFlow","Pandas"],
    ["Docker","Kubernetes","AWS"],
    ["Power BI","Excel","SQL"]
]

degrees = [
    "B.Tech Computer Science",
    "MCA",
    "BCA",
    "M.Tech AI"
]

for name in names:
    skills = random.choice(skill_sets)
    years = random.randint(1,8)
    degree = random.choice(degrees)

    content = f"""{name}

Skills
{", ".join(skills)}

Experience
{years} years experience working on {skills[0]} projects.

Education
{degree}
"""

    filename = name.lower().replace(" ", "_") + ".txt"

    with open(f"data/resumes/{filename}", "w") as f:
        f.write(content)

print("30 resumes created successfully!")