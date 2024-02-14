Feature: Create and Send an Email with Attachment

  Scenario: Successfully create and send an email with an attachment
    Given I am logged in to my email account
    When I click on the compose button
    And I fill in the recipient with my email from contacts
    And I fill in the subject and body of the email
    And I attach a file
    And I click on the send button
    Then the email with the attachment should be sent successfully
    When I logout
    Then I should be logged out successfully
