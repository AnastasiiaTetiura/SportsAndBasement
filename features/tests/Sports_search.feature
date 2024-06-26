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

    Scenario: User can add product to the cart
      Given Open main page
      When Close ad
      And Search for snowboard
      And Click Add to cart
      And Search for tent
      And Click Add to cart
      Then Verify cart has 2 items


    Scenario: Verify that User cans see product name and image
      Given Open main page
      When Close ad
      When Search for scott bike
      Then Verify that every product has name and image






