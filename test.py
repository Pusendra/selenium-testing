from selenium import webdriver
from  selenium.webdriver.common.by import By
import time

class Login():
    def test(self):
        baseURL = "https://github.com/"
        driverLocation = "C:\\Users\\No Distraction\\PycharmProjects\\GithubAutomator\\driver\\chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        login_click = driver.find_element(By.XPATH,"//a[@class='HeaderMenu-link no-underline mr-3']")
        login_click.click()

        emailField = driver.find_element(By.ID,"login_field")
        emailField.send_keys("cpusendra@gmail.com")

        passwordField = driver.find_element(By.ID,"password")
        passwordField.send_keys("Pushy@bby1")

        sign_in_button = driver.find_element(By.NAME,"commit")
        sign_in_button.click()
        time.sleep(5)

        profile_btn = driver.find_element(By.XPATH,"//details[@class='details-overlay details-reset js-feature-preview-indicator-container']//summary[@class='Header-link']")
        profile_btn.click()

        click_your_repo = driver.find_element(By.XPATH,"//a[contains(text(),'Your repositories')]")
        click_your_repo.click()
        '''Creating New Repositort'''
        time.sleep(5)
        repository_name = "selenium-testing"
        repository_to_be_clicked = driver.find_element(By.XPATH, f"//a[contains(text(),'{repository_name}')]")
        if repository_to_be_clicked is  None:
            driver.get("https://github.com")
            new_button = driver.find_element(By.LINK_TEXT,"New")

            new_button.click()
            repository = driver.find_element(By.ID,"repository_name")

            repository.send_keys(repository_name)
            time.sleep(2)
            description = driver.find_element(By.ID,"repository_description")
            description_content = "Selenium testing"
            description.send_keys(description_content)
            time.sleep(2)
            initialize = driver.find_element(By.ID,"repository_auto_init")
            initialize.click()

            create_repository_button = driver.find_element(By.CSS_SELECTOR,".btn.btn-primary.first-in-line")
            create_repository_button.click()
            time.sleep(3)

        elif (repository_to_be_clicked):
            repository_to_be_clicked.click()
            time.sleep(3)

            upload_files_btn = driver.find_element(By.XPATH,"//a[@class='btn btn-sm BtnGroup-item']")
            upload_files_btn.click()
            time.sleep(1)

            upload_files = driver.find_element(By.ID,"upload-manifest-files-input")
            upload_files.send_keys(r"C:\Users\No Distraction\PycharmProjects\GithubAutomator\test.py")
            time.sleep(5)
            commit_message = driver.find_element(By.ID,"commit-summary-input")
            commit_message.send_keys("Files added")
            time.sleep(1)

            commit_upload = driver.find_element(By.XPATH,"//button[@class='btn btn-primary js-blob-submit']")
            commit_upload.click()
            time.sleep(10)








ll = Login()
ll.test()