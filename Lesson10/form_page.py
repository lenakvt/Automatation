from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FormPage:
    fields = ["first-name", "last-name", "address", "e-mail",
              "phone", "city", "country", "job-position", "company"]

    def __init__(self, seleniumDriver):
        self.driver = seleniumDriver

    def get_form(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def set_field(self, selector, value):
        self.driver.find_element(
            By.CSS_SELECTOR, selector).send_keys(value)

    def setup_form(self):
        self.set_field("[name=first-name]", "Иван")
        self.set_field("[name=last-name]", "Петров")
        self.set_field("[name=address]", "Ленина, 55-3")
        self.set_field("[name=e-mail]", "test@skypro.com")
        self.set_field("[name=phone]", "+7985899998787")
        self.set_field("[name=city]", "Москва")
        self.set_field("[name=country]", "Россия")
        self.set_field("[name=job-position]", "QA")
        self.set_field("[name=company]", "SkyPro")

    def submit(self):
        selector = "button.btn.btn-outline-primary.mt-3"
        button_submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        button_submit.click()

    def get_zipcode_id(self):
        zipCodeElement = self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code.alert.py-2.alert-danger")
        return zipCodeElement.get_attribute("id")

    def check_sucsess_fields(self):
        count = 0
        for name in self.fields:
            element = self.driver.find_element(
                By.CSS_SELECTOR, f'#{name}.alert.py-2.alert-success')
            if (element):
                count += 1

        return count == len(self.fields)
