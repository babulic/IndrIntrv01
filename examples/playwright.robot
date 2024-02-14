*** Settings ***
Documentation     Example of using Playwright library to test web application

Library  RPA.Browser.Playwright
Resource  ../../Common/Keywords/Logging.resource

*** Variables ***
*** Keywords ***

validate entity in Vusion web
  [Arguments]  ${shouldBeFound}  ${WEB_URL}  ${WEB_TITLE}  ${WEB_EMAIL}  ${WEB_PASSWORD}

  RPA.Browser.Playwright.New Browser    chromium    headless=false
  RPA.Browser.Playwright.Set Browser Timeout  timeout=25s

  #RPA.Browser.Playwright.New Context    viewport={'width': 1920, 'height': 1080}
  RPA.Browser.Playwright.New Page    ${WEB_URL}
  RPA.Browser.Playwright.Get Title      ==    VUSION Manager
  RPA.Browser.Playwright.Click  "Personal Account"

  #RPA.Browser.Playwright.Wait Until Network Is Idle  #timeout=1s
  ${WEB_EMAIL_decoded}=  EncryptDecrypt.decrypt  ${WEB_EMAIL}
  ${WEB_PASSWORD_decoded}=  EncryptDecrypt.decrypt  ${WEB_PASSWORD}
  RPA.Browser.Playwright.Type Text  input#email  ${WEB_EMAIL_decoded}
  RPA.Browser.Playwright.Type Text  input#password  ${WEB_PASSWORD_decoded}
  RPA.Browser.Playwright.Click  button#next

  #RPA.Browser.Playwright.Wait Until Network Is Idle
  RPA.Browser.Playwright.Click  "Items"

  FOR  ${strElementTextPart}  IN  @{lstElementTextPart}
    RPA.Browser.Playwright.Wait Until Network Is Idle  timeout=10s
    RPA.Browser.Playwright.Clear Text    input#mat-input-0
    RPA.Browser.Playwright.Type Text  input#mat-input-0  ${strElementTextPart}
    RPA.Browser.Playwright.Click  "search"
    switchLog  strElementTextPart: ${strElementTextPart}

    RPA.Browser.Playwright.Wait Until Network Is Idle  timeout=10s
    #${intCnt}=  RPA.Browser.Playwright.Get Element Count    text=${strElementTextPart}
    ${blnWasFound}=  Builtin.Run Keyword And Return Status  RPA.Browser.Playwright.Get Text    text=${strElementTextPart}
    #switchLog  intCnt: ${intCnt}
    IF  ${blnWasFound}  #${intCnt} > ${0}
      ${strElementTextFull}=  RPA.Browser.Playwright.Get Text    text=${strElementTextPart}
      switchLog  Element text: ${strElementTextFull}
      IF  ${shouldBeFound}
        switchLog  PASSED: Element was found. Text: ${strElementTextFull}
      ELSE
        Run Keyword And Continue On Failure   Fail  Fail: Element was found. Text: ${strElementTextFull}
      END
    ELSE
      IF  ${shouldBeFound}
        Run Keyword And Continue On Failure   Fail  Fail: Element that contains ${strElementTextPart} was not found
      ELSE
        switchLog  PASSED: Element that contains ${strElementTextPart} was not found
      END
    END
    RPA.Browser.Playwright.Close Page
    RPA.Browser.Playwright.Close Context
    RPA.Browser.Playwright.Close Browser