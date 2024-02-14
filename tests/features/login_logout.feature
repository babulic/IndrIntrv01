Feature: Login and Logout from Email

  Scenario: Successful login and logout
    Given I am on the login page
    When I enter my username and password
    And I click on the login button
    Then I should be redirected to the inbox page
    When I click on the logout button
    Then I should be redirected to the login page
