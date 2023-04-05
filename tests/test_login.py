from pages.login_page import LoginPage


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("testuser")
    login_page.enter_password("testpassword")
    login_page.click_login()
