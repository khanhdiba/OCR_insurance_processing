import re

def extract_key_info(text):
    result = {}

    patterns = {
        "Policy No": r"Policy\s*No[:\s]*([A-Z0-9\-]+)",
        "Claim Number": r"Claim\s*Number[:\s]*([A-Z0-9\-]+)",
        "Date of Loss": r"Date\s*of\s*(Loss|Incident)[:\s]*(\d{2}/\d{2}/\d{4})",
        "Claimant Name": r"Name[:\s]*(.+)",
        "Phone Number": r"Phone[:\s]*(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})",
        "Email": r"Email[:\s]*([\w\.-]+@[\w\.-]+)",
        "Location of Loss": r"Location\s*of\s*Loss[:\s]*(.+)",
        "Claim Amount": r"Amount\s*Claimed[:\s]*\$?([\d,]+\.\d{2})",
        "Police Report Number": r"Police\s*Report\s*Number[:\s]*(\w+)",
        "Description of Loss": r"Description\s*of\s*Loss[:\s]*(.+)",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            result[key] = match.group(1).strip()

    return result