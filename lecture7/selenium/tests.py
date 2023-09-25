import os
import pathlib
import unittest

from selenium import webdriver

# Finds the Uniform Resourse Identifier of a file
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Sets up web driver using Google chrome
driver = webdriver.Chrome()

# Find the URI of our newly created file
# uri = file_uri("counter.html")
# driver.get(uri)


class WebpageTests(unittest.TestCase):
    def test_title(self): 
        uri = file_uri("counter.html")
        driver.get(uri)
        self.assertEqual(driver.title, "Counter")
        print("[test_title]: Passed!")  
    
    def test_increase(self):
        uri = file_uri("counter.html")
        driver.get(uri)
        increase = driver.find_element("id","increase")
        increase.click()
        self.assertEqual(driver.find_element("id","h1").text,"1")
        print("[test_increase]: Passed!")

    def test_decrease(self):
        uri = file_uri("counter.html")
        driver.get(uri)
        decrease = driver.find_element("id","decrease")
        decrease.click()
        self.assertEqual(driver.find_element("id","h1").text,"-1")
        print("[test_decrease]: Passed!")
    
    def test_multiple_increase(self): 
        uri = file_uri("counter.html")
        driver.get(uri)
        increase = driver.find_element("id","increase")
        for i in range(100):
            increase.click()
        self.assertEqual(driver.find_element("id","h1").text,"100")  
        print("[test_multiple_increase]: Passed!")


if __name__ == "__main__":
    unittest.main()