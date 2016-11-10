*** Settings ***
Library       Selenium2Library
Test Timeout    2 minutes

*** Test Cases ***
Register User
  Open Purcha.es
  Register
  Check Login
  Exit Purcha.es

*** Keywords ***
Open Purcha.es
  Open Browser                 http://128.199.192.241:8000  googlechrome

Register
  Wait Until Page Contains     Register
  Click Element                link=Register
  Wait Until Page Contains     Username:
  Input Text                   id=register-form-username   test998
  Input Text                   id=register-form-password   pass
  Input Text                   id=register-form-email      test@mail.com
  Input Text                   id=register-form-bio        test bio
  Click Element                id=register-form-register

Check Login
  Wait Until Page Contains      Profile

Exit Purcha.es
  Close Browser
