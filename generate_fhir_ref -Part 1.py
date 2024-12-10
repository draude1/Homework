# generate_fhir_ref.py

def generate_referral():
    """
    Generates a static FHIR referral payload.

    Returns:
        dict: A JSON representation of a FHIR ServiceRequest.
    """
    return {
        "resourceType": "ServiceRequest",
        "id": "AURF-001",
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
            "reference": "Patient/123",
            "type": "Patient"
        },
        "authoredOn": "2023-12-01T12:00:00+00:00",
        "requester": {
            "reference": "Practitioner/456",
            "type": "Practitioner"
        }
    }

# Example usage:
if __name__ == "__main__":
    referral = generate_referral()
    print(referral)
