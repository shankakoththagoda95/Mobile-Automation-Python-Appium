import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

def test_valid_login(login_page):
    login_page.login("valid_user", "valid_password")
    assert "Welcome" in login_page.get_text((By.ID, "com.example:id/welcome_message"))

def test_invalid_login(login_page):
    login_page.login("invalid_user", "invalid_password")
    assert "Invalid credentials" in login_page.get_text((By.ID, "com.example:id/error_message"))
