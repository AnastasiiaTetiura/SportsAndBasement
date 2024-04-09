# Created by anastasiiatetiura at 4/8/24
Feature: Help page tests

  Scenario: Verify Hep Page has 9 topics
    Given Open main page
    When Close ad
    And Open Help page
    Then Verify there are 9 topics
