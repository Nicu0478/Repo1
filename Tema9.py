from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.wait import WebDriverWait
chrome = webdriver.Chrome()

#1

class Login(unittest.TestCase):

    def setUp(self):
        chrome.get("https://the-internet.herokuapp.com/login")

    def tearDown(self):
        chrome.quit()

    def test_new_url_is_correct(self):
        actual_url = chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        self.assertEqual(expected_url, actual_url, "URL nu este corect")
        sleep(3)

#2

    def test_page_tile_corect(self):
        actual = chrome.find_element(By.XPATH, '//*[@id="content"]/div/h2').text
        expected = "Login Page"
        self.assertEqual(actual, expected, "testul esueaza")
        sleep(3)

#3

    def test_element_xpath(self):
            text = chrome.find_element(By.XPATH, "//h2[text()='Login Page']")
    sleep(3)

#4

    def test_buton_login(self):
        actual = chrome.find_element(By.CLASS_NAME, "radius").text
        expected = "Login"
        self.assertEqual(actual, expected, "testul esueaza")

#5

    def test_atribut_herf(self):
        element = chrome.find_element(By.XPATH, '//a[@target="_blank"]').text
        actual = element.__getattribute__("href")
        expected = "http://elementalselenium.com/"
        assert actual == expected, f"Valoarea atributului href este incorecta.ne asteptam la {actual},dar a fost afisat {expected}"
        sleep(4)

#6

    def test_login_eroare(self):
        chrome.find_element(By.ID, "username").send_keys()
        chrome.find_element(By.ID, "password").send_keys()
        chrome.find_element(By.CLASS_NAME, "radius").click()
        assert "Your username is invalid!" in chrome.page_source
        sleep(3)


#7

    def test_login_invalide(self):
        chrome.find_element(By.ID, "username").send_keys("aaaaaaaa")
        chrome.find_element(By.ID, "password").send_keys("sssssss")
        chrome.find_element(By.CLASS_NAME, "radius").click()
        actual = chrome.find_element(By.ID, "flash").text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')
        sleep(2)


#8

    def test_login_x_eroare(self):
        chrome.set_window_size(1920, 1080)
        chrome.find_element(By.ID, "username").send_keys()
        chrome.find_element(By.ID, "password").send_keys()
        chrome.find_element(By.CLASS_NAME, "radius").click()
        chrome.find_element(By.CLASS_NAME, "close").click()
        assert "Your username is invalid!" in chrome.page_source
        sleep(2)

#9

    def test_lista_label(self):
        labels = ['username', 'password']
        actual = chrome.find_element(By.CSS_SELECTOR, 'div label[for*="username"]').text
        expected = "Username"
        self.assertEqual(actual, expected, "Nu sunt corecte")
        actual = chrome.find_element(By.CSS_SELECTOR, 'div label[for*="password"]').text
        expected = "Password"
        self.assertEqual(actual, expected, "Nu sunt corecte")
        sleep(2)

#10

    def test_login_corecte(self):
        chrome.find_element(By.ID, "username").send_keys("tomsmith")
        chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        chrome.find_element(By.CLASS_NAME, "radius").click()
        assert "secure" in chrome.page_source
        flash = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "flash success")))
        element = chrome.find_element(By.CLASS_NAME, "flash success").is_displayed()
        actual = chrome.find_element(By.ID, "flash").text
        expected = "secure area!"
        self.assertEqual(actual, expected, "Login in incorect")
        sleep(3)

#11

    def test_log_out(self):
        chrome.find_element(By.ID, "username").send_keys("tomsmith")
        chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        chrome.find_element(By.CLASS_NAME, "radius").click()
        chrome.find_element(By.LINK_TEXT, "Logout").click()
        actual = chrome.current_url
        expected = "https://the-internet.herokuapp.com/login"
        self.assertEqual(expected, actual, "URL is incorrect")
        sleep(3)