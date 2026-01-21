from pages.login_page import LoginPage
from config.config import LOGIN_URL, VENDOR_EMAIL, VENDOR_PASSWORD


def test_vendor_login_valid_credentials(setup):
    driver = setup

    login_page = LoginPage(driver)
    login_page.open(LOGIN_URL)
    login_page.login(VENDOR_EMAIL, VENDOR_PASSWORD)

    assert "dashboard" in driver.current_url
