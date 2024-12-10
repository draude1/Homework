from faker import Faker
from lib.common_health import generate_medicare_number, generate_ihi_number, generate_dva_number

fake = Faker('en_AU')  # Australian locale

def generate_referral():
    """
    Generates a FHIR referral payload with dynamic identifiers.

    Returns:
        dict: A JSON representation of a FHIR ServiceRequest.
    """
    return {
        "resourceType": "ServiceRequest",
        "id": f"AURF-{fake.random_number(digits=3, fix_len=True)}",
        "status": "active",
        "intent": "order",
        "identifier": [
            {"system": "http://ns.electronichealth.net.au/id/medicare-number", "value": generate_medicare_number()},
            {"system": "http://ns.electronichealth.net.au/id/hi/ihi/1.0", "value": generate_ihi_number()},
            {"system": "http://ns.electronichealth.net.au/id/dva", "value": generate_dva_number()}
        ],
        "code": {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "dummy",
                    "display": "Referral to service"
                }
            ],
            "text": "Referral to a specialist"
        },
        "subject": {
            "reference": f"Patient/{fake.random_number(digits=6)}",
            "type": "Patient"
        },
        "authoredOn": f"{fake.date_between(start_date='-2y', end_date='today')}T{fake.time()}+00:00",
        "requester": {
            "reference": f"Practitioner/{fake.random_number(digits=6)}",
            "type": "Practitioner"
        },
        "contained": [
            {
                "resourceType": "Practitioner",
                "id": f"Practitioner-{fake.random_number(digits=4)}",
                "name": [
                    {
                        "family": fake.last_name(),
                        "given": [fake.first_name()]
                    }
                ],
                "telecom": [
                    {"system": "phone", "value": fake.phone_number(), "use": "work"},
                    {"system": "email", "value": fake.email(), "use": "work"}
                ]
            }
        ]
    }

# Example usage:
if __name__ == "__main__":
    referral = generate_referral()
    print(referral)
