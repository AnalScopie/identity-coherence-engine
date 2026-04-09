from main import process_identity

def fake_ai_analysis(data):
    """
    Simule une IA qui analyse des données utilisateur
    """
    return f"""
AI Analysis Result:

User: {data['first_name']} {data['last_name']}
Email: {data['email']}
Phone: {data['phone']}

Status: VALIDATED USER DATA
"""

def run_demo():
    raw_data = {
        "first_name": "  jean ",
        "last_name": "dupont",
        "email": "JEAN.DUPONT@MAIL.COM ",
        "phone": "06 12 34 56 78"
    }

    print("🔴 RAW INPUT:")
    print(raw_data)

    clean_data, log = process_identity(raw_data)

    print("\n🟢 CLEANED DATA:")
    print(clean_data)

    print("\n📋 AUDIT LOG:")
    for entry in log:
        print(entry)

    result = fake_ai_analysis(clean_data)

    print("\n🤖 AI OUTPUT:")
    print(result)

if __name__ == "__main__":
    run_demo()
