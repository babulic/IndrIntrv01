Feature: Create and Send an Email

  Scenario: Successfully create and send an email
    Given I am logged in to my email account
    When I click on the compose button
    And I fill in the recipient with my email from contacts
    And I fill in the subject and body of the email
    And I click on the send button
    Then the email should be sent successfully
    When I logout
    Then I should be logged out successfully
