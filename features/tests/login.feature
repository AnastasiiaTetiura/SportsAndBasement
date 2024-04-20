# Created by anastasiiatetiura at 4/13/24
Feature: Login tests

    Scenario: User can see Login form
        Given Open main page
        When Close ad
        And Click Pre-loved department
        When Click account button
        Then Verify Login form is present

        #WILL FAIL (CAPTCHA)
    Scenario: User can register
        Given Open main page
        When Close ad
        And Click account button
        When Input email and password on SignIn page
        And Click Sign In
        Then Verify user is logged in
        #sweetdd40@suksesboss.com sweet@123