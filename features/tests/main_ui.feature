Feature: Main Page tests

  Scenario: User can see Login form
    Given Open main page
    When Close ad
    And Click Pre-loved department
    When Click account button
    Then Verify Login form is present

    Scenario: Secondary nav has correct amount of links
      Given Open main page
      When Close ad
      And Verify secondary nav is present
      Then Verify secondary nav has 7 links
