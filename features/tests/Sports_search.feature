# Created by anastasiiatetiura at 4/8/24
Feature: Search tests

  Scenario: User can search by brand
    Given Open main page
    When Close ad
    And Search for teva
    Then Verify search worked for teva
    Then Verify teva in search result url

  Scenario Outline: User can search for product
      Given Open main page
      When Close ad
      And Search for <product>
      Then Verify <expected_product> in search result url
      Examples:
     |product        |   expected_product  |
     | sleeping bag  |   sleeping%20bag    |
     | tent          |   tent              |
     | trekking poles |  trekking%20poles  |





