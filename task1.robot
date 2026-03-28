*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Myntra Test
    Open Browser    https://www.myntra.com    chrome
    Maximize Browser Window


    Wait Until Element Is Visible    xpath=//a[@data-group='women']
    Mouse Over    xpath=//a[@data-group='women']


    Wait Until Element Is Visible    xpath=//a[contains(@href,'lehenga')]
    Click Element    xpath=//a[contains(@href,'lehenga')]


    Wait Until Page Contains Element    xpath=//li[contains(@class,'product')]
    Execute JavaScript    window.scrollTo(0, document.body.scrollHeight/3)


    Click Element    xpath=//label[contains(text(),'Blue')]

    ${name}=    Get Text    xpath=(//h3)[1]
    Log To Console    ${name}

    Close Browser