from faker import Faker

fake = Faker('en_AU')  # Australian locale

def generate_medicare_number():
    """Generates a random Medicare number."""
    return fake.random_number(digits=10, fix_len=True)

def generate_ihi_number():
    """Generates a random Individual Healthcare Identifier (IHI)."""
    return fake.random_number(digits=16, fix_len=True)

def generate_dva_number():
    """Generates a random Department of Veterans' Affairs (DVA) number."""
    return fake.lexify(text="??????")
