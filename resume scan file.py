# Resume Keyword Scanner
# Beginner-friendly version

def load_keywords():
    return [
        "python", "data analysis", "machine learning", "communication",
        "sql", "teamwork", "problem solving", "excel"
    ]

def read_resume(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().lower()
    except FileNotFoundError:
        print("❌ Resume file not found!")
        return ""

def scan_resume(resume_text, keywords):
    found = []
    missing = []
    for keyword in keywords:
        if keyword.lower() in resume_text:
            found.append(keyword)
        else:
            missing.append(keyword)
    return found, missing

def main():
    file_path = input("Enter resume file name (e.g., resume.txt): ")
    keywords = load_keywords()
    resume_text = read_resume(file_path)

    if resume_text:
        found, missing = scan_resume(resume_text, keywords)
        
        print("\n✅ Found Keywords:", found)
        print("\n❌ Missing Keywords:", missing)
        print(f"\n📊 Keyword Match: {len(found)}/{len(keywords)} keywords found.")

if __name__ == "__main__":
    main()
