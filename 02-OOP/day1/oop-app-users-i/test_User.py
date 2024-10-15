import pytest
from User import User

def test_user_creation():
    user1 = User("Alice", "alice@example.com")
    assert user1.name == "Alice"
    assert user1.email == "alice@example.com"
    assert user1.drivers_license is None

    user2 = User("Bob", "bob@example.com", "XYZ123")
    assert user2.name == "Bob"
    assert user2.email == "bob@example.com"
    assert user2.drivers_license == "XYZ123"
    
def test_user_with_a_totally_normal_name():
    user = User("Bartholomew Oobleck", "bartholomew@oobleck.edu")
    assert user.name == "Bartholomew Oobleck"

def test_user_with_an_obviously_fake_email():
    user = User("Agent 47", "hitman@ica.org")  # This email is totally legit, right?
    assert user.email == "hitman@ica.org"

def test_user_with_a_suspiciously_familiar_drivers_license():
    user = User("James Bond", "007@mi6.gov.uk", "007JB007")  # You never know who's signing up
    assert user.drivers_license == "007JB007"  # Easter egg!