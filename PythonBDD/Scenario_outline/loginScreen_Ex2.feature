# This is a Feature file

Feature: Fill the Contact Form

    Scenario Outline: User Login credentials

        Given Launch the App and Click on Login Button
        When Enter <emailid> UserID
        When Enter  <password> password
        Then Verify Home Screen


        Examples:
             | emailid         |password|
             | student@gmail.com| S1234 |
             | teacher@gmail.com| T1234 |