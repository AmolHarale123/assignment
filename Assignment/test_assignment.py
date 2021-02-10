from time import sleep
from selenium import webdriver
import pytest


@pytest.mark.usefixtures('oneTimeSetUp')
class Test_Auotomation:

    def test_dropdown(self,):

        drop_down=self.driver.find_element_by_xpath("(//i[@class='caret pull-right'])[2]")
        drop_down.click()
        sleep(2)
        self.driver.save_screenshot("../Screenshot/dropdown.png")
        drop_down_text=self.driver.find_element_by_xpath("//div[text()='English']")
        print(drop_down_text.text)
        sleep(2)
        assert drop_down_text.text == "English"

    def test_submitInfo(self):
        full_name=self.driver.find_element_by_xpath("//input[@id='name']")
        full_name.send_keys("Amol Dnyaneshwar Harale")
        sleep(2)
        Org_name=self.driver.find_element_by_xpath("//input[@id='orgName']")
        Org_name.send_keys("Avapya Web Services")
        sleep(2)
        Email_id=self.driver.find_element_by_xpath("//input[@id='singUpEmail']")
        Email_id.send_keys("haraleamol88@gmail.com")
        sleep(2)
        check_box=self.driver.find_element_by_xpath("//span[@class='black-color ng-binding']")
        check_box.click()
        sleep(1)
        self.driver.save_screenshot("../Screenshot/requires_data_submit.png")

        get_start=self.driver.find_element_by_xpath("//button[text()='Get Started']")
        sleep(2)
        #get_start.click()
        print(get_start.text)
        sleep(2)
        self.driver.save_screenshot("../Screenshot/confirmation_send.png")

        assert get_start.text =="Get Started"

        sleep(2)
