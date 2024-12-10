from faker import Faker

# Initialize Faker with Australian locale
fake = Faker('en_AU')

def generate_medicare_number():
    """Generates a 10-digit Medicare number."""
    return fake.random_number(digits=10, fix_len=True)

def generate_ihi_number():
    """Generates a 16-digit Individual Healthcare Identifier (IHI)."""
    return fake.random_number(digits=16, fix_len=True)

def generate_dva_number():
    """Generates a 6-character DVA number."""
    return fake.lexify(text="??????").upper()

def generate_referral():
    """
    Generates a FHIR referral payload with dynamically generated fields,
    including healthcare identifiers and a contained Patient resource.

    Returns:
        dict: A JSON representation of a FHIR ServiceRequest with synthetic data.
    """
    patient_id = fake.random_number(digits=6)  # Unique Patient ID

    return {
        "resourceType": "ServiceRequest",
        "id": f"AURF-{fake.random_number(digits=3, fix_len=True)}",
        "identifier": [
            {
                "system": "http://ns.electronichealth.net.au/id/medicare-number",
                "value": generate_medicare_number()
            },
            {
                "system": "http://ns.electronichealth.net.au/id/hi/ihi/1.0",
                "value": generate_ihi_number()
            },
            {
                "system": "http://ns.electronichealth.net.au/id/dva",
                "value": generate_dva_number()
            }
        ],
        "status": "active",
        "intent": "order",
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
            "reference": f"Patient/{patient_id}",
            "type": "Patient"
        },
        "authoredOn": f"{fake.date_between(start_date='-2y', end_date='today')}T{fake.time()}+00:00",
        "requester": {
            "reference": f"Practitioner/{fake.random_number(digits=6)}",
            "type": "Practitioner"
        },
        "contained": [
            {
                "resourceType": "Patient",
                "id": str(patient_id),
                "name": [
                    {
                        "use": "official",
                        "family": fake.last_name(),
                        "given": [fake.first_name()]
                    }
                ],
                "gender": fake.random_element(elements=["male", "female"]),
                "birthDate": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
                "address": [
                    {
                        "use": "home",
                        "line": [fake.street_address()],
                        "city": fake.city(),
                        "state": fake.state(),
                        "postalCode": fake.postcode(),
                        "country": "Australia"
                    }
                ]
            }
        ]
    }

# Example usage:
if __name__ == "__main__":
    for _ in range(3):  # Generate and print 3 unique referrals
        referral = generate_referral()
        print(referral)
