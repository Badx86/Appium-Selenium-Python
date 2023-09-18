# This is a Feature file

Feature: Fill the Contact Form

    Scenario: User Login credentials

        Given Launch the App and Click on Login Button
        When Enter UserID
        When Enter password
        When click on Login Button
        And Home page opens
        Then Verify Home Screen
        Then Take screenshot


    Scenario: Enter the data in Contact Form

        Given Launch the App and Click on ContactForm
        When Enter Name
        When Enter Email
        When Enter Mobile Number
        And we need to click on submit button
        Then Click on submit
        Then Take Screenshot of contact Form
