from main import process_identity

def compute_coherence_score(data):
    score = 100
    issues = []

    # Vérification prénom
    if len(data["first_name"]) < 2:
        score -= 20
        issues.append("Invalid first name")

    # Vérification email
    if "@" not in data["email"]:
        score -= 30
        issues.append("Invalid email")

    # Vérification téléphone
    if not data["phone"].isdigit():
        score -= 25
        issues.append("Invalid phone format")

    return score, issues


def ai_decision_engine(clean_data, score):
    if score >= 90:
        status = "VALID USER"
        risk = "LOW"
    elif score >= 70:
        status = "REVIEW REQUIRED"
        risk = "MEDIUM"
    else:
        status = "SUSPICIOUS USER"
        risk = "HIGH"

    return {
        "status": status,
        "risk_level": risk,
        "ai_ready": score >= 70
    }


def run_advanced_demo():

    raw_data = {
        "first_name": "  j ",
        "last_name": "dupont",
        "email": "JEAN.DUPONTMAIL.COM",
        "phone": "06 12 XX 56 78"
    }

    print("🔴 RAW INPUT:")
    print(raw_data)

    clean_data, log = process_identity(raw_data)

    print("\n🟢 CLEANED DATA:")
    print(clean_data)

    print("\n📋 AUDIT LOG:")
    for entry in log:
        print(entry)

    score, issues = compute_coherence_score(clean_data)

    print("\n📊 COHERENCE SCORE:")
    print(f"{score}/100")

    print("\n⚠️ ISSUES DETECTED:")
    for issue in issues:
        print("-", issue)

    decision = ai_decision_engine(clean_data, score)

    print("\n🤖 AI DECISION:")
    for k, v in decision.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    run_advanced_demo()
