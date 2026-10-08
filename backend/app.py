from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path

app = Flask(__name__, static_folder="../frontend", static_url_path="")

JOB_ROLES = [
    {"role":"Frontend Developer","skills":["html","css","javascript","react"],"locations":["chennai","bangalore","remote"]},
    {"role":"Python Developer","skills":["python","sql","flask","django"],"locations":["chennai","bangalore","remote"]},
    {"role":"Data Analyst","skills":["python","sql","excel","power bi"],"locations":["chennai","bangalore","remote"]},
    {"role":"UI/UX Designer","skills":["figma","ui","ux","wireframing"],"locations":["chennai","bangalore","remote"]},
    {"role":"Full Stack Developer","skills":["html","css","javascript","react","python","sql"],"locations":["chennai","bangalore","remote"]},
]

def normalize(items):
    return {x.strip().lower() for x in items if x.strip()}

@app.get("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.post("/api/recommend")
def recommend():
    data = request.get_json(force=True)
    skills = normalize(data.get("skills", []))
    location = data.get("location","").strip().lower()
    interests = normalize(data.get("interests", []))

    results = []
    for job in JOB_ROLES:
        skill_match = len(skills & set(job["skills"]))
        skill_total = len(job["skills"])
        location_match = location in job["locations"] or "remote" in job["locations"] if location else False
        interest_match = any(i in job["role"].lower() for i in interests)
        score = round((skill_match / skill_total) * 70 + (20 if location_match else 0) + (10 if interest_match else 0))
        missing = [s for s in job["skills"] if s not in skills]
        results.append({
            "role": job["role"],
            "score": min(score,100),
            "matchedSkills": sorted(skills & set(job["skills"])),
            "missingSkills": missing
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return jsonify({"recommendations": results[:5]})

if __name__ == "__main__":
    app.run(debug=True)
