from time import sleep
from selenium import webdriver
import pytest


@pytest.mark.usefixtures('oneTimeSetUp')
class Test_opration:

    def test_multi(self,):

        drop_down=self.driver.find_element_by_xpath("(//i[@class='caret pull-right'])[2]")

        sleep(4)
        drop_down_text=self.driver.find_element_by_xpath("//div[text()='English']")
        print(drop_down_text.text)
        sleep(2)
        #self.driver.save_screenshot("../Screenshot/dropdown.png")
        drop_down_text.click()

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
        #self.driver.save_screenshot("../Screenshot/requires_data_submit.png")
        sleep(2)
        get_start=self.driver.find_element_by_xpath("//button[text()='Get Started']")
        get_start.click()
        sleep(2)
        #self.driver.save_screenshot("../Screenshot/confirmation_send.png")
        sleep(2)
        assert drop_down_text.text==" English"