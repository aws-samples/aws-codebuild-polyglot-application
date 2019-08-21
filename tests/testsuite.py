import inspect
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


main_url = 'http://127.0.0.1:8080'


def tc001(browser):
    """Testcase to validate whether home page is displayed properly"""
    print('Executing Testcase: tc001')
    print('Started execution at %s' % datetime.strftime(datetime.today(), '%d-%m-%Y %H:%M:%S,%f'))
    browser.get(main_url)
    assert 'AWS CodeBuild - Polyglot Application.' in browser.title
    print(browser.title)
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, 'listusers')))
    print('Completed test tc001')
    print('Completed execution at %s' % datetime.strftime(datetime.today(), '%d-%m-%Y %H:%M:%S,%f'))


def tc002(browser):
    """Testcase to validate List users"""
    print('Executing Testcase: tc002')
    print('Started execution at %s' % datetime.strftime(datetime.today(), '%d-%m-%Y %H:%M:%S,%f'))
    browser.get(main_url)
    print(browser.title)
    assert 'AWS CodeBuild - Polyglot Application.' in browser.title
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, 'listusers')))
    browser.find_element_by_id('listusers').click()
    WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='allusers']/thead")))
    col1 = ['Id', '1', '2', '3', '4', '5', '6', '7']
    col2 = ['Name', 'Prakash', 'Sheldon', 'Leonard', 'Howard', 'Raj', 'Amy', 'Bernadette']
    for i in range(len(col1)):
        assert browser.find_element_by_xpath("//*[@id='allusers']/thead/tr[" + str(i + 1) + "]/td[1]").text == col1[i]
        assert browser.find_element_by_xpath("//*[@id='allusers']/thead/tr[" + str(i + 1) + "]/td[2]").text == col2[i]
    print('Completed test tc002')
    print('Completed execution at %s' % datetime.strftime(datetime.today(), '%d-%m-%Y %H:%M:%S,%f'))


def tc003(browser):
    """Testcase to validate Get users"""
    print('Executing Testcase: tc003')
    print('Started execution at %s' % datetime.strftime(datetime.today(), '%d-%m-%Y %H:%M:%S,%f'))
    browser.get(main_url)
    assert 'AWS CodeBuild - Polyglot Application.' in browser.title
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, 'userID')))
    browser.find_element_by_id('userID').send_keys('5')
    browser.find_element_by_id('submitUser').click()
    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='userdetails']")))
    print(browser.find_element_by_id('userdetails').text)
    assert browser.find_element_by_id('userdetails').text == 'Name of user with Id 5 is "Raj".'
    print('Completed test tc003')
    print('Completed execution at %s' % datetime.strftime(datetime.today(), '%d-%m-%Y %H:%M:%S,%f'))


def tc004(browser):
    """Testcase to validate user greetings"""
    print('Executing Testcase: tc004')
    print('Started execution at %s' % datetime.strftime(datetime.today(), '%d-%m-%Y %H:%M:%S,%f'))
    browser.get(main_url)
    assert 'AWS CodeBuild - Polyglot Application.' in browser.title
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, 'userID')))
    browser.find_element_by_id('userID').send_keys('5')
    browser.find_element_by_id('submitUser').click()
    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='userdetails']")))
    print(browser.find_element_by_id('userdetails').text)
    assert browser.find_element_by_id('userdetails').text == 'Name of user with Id 5 is "Raj".'
    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='usergreeting']")))
    print(browser.find_element_by_id('usergreeting').text)
    assert browser.find_element_by_id('usergreeting').text == 'Hello "Raj"'
    print('Completed test tc004')
    print('Completed execution at %s' % datetime.strftime(datetime.today(), '%d-%m-%Y %H:%M:%S,%f'))


if __name__ == '__main__':
    allmthd = globals().copy()
    allmthd.update(locals())
    for br in ['firefox', 'chrome']:
        if br.lower() == 'chrome':
            options = ChromeOptions()
            options.add_argument("--headless")
            browser = webdriver.Chrome(options=options)
            print('Running tests on headless Chrome')
        elif br.lower() == 'firefox':
            options = FirefoxOptions()
            options.add_argument("-headless")
            browser = webdriver.Firefox(options=options)
            print('Running tests on headless Firefox')

        for tc in ['tc001', 'tc002', 'tc003', 'tc004']:
            method = allmthd.get(tc)
            method(browser)

        if browser:
            browser.quit()
