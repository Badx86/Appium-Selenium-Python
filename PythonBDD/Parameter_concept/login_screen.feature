# This is a Feature file

Feature: Fill the Contact Form

    Scenario: User Login credentials

        Given Launch the App and Click on Login Button
        When Enter 'abc@gmail.com' UserID
        When Enter '12345' password
        When click on Login Button
        And Home page opens
        Then Verify Home Screen
        Then Take screenshot
