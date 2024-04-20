Feature: Main Page tests

  Scenario: User can see Login form
    Given Open main page
    When Close ad
    And Click Pre-loved department
    When Click account button
    Then Verify Login form is present

    Scenario: Header has correct amount of links
      Given Open main page
      When Close ad
      And Verify header is present
      Then Verify header has 7 links
