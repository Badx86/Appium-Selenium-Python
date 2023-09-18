# This is a Feature file

@regression
Feature: Fill the Contact Form

    @Login @regression
    Scenario: User Login credentials

        Given Launch the App and Click on Login Button
        When Enter UserID
        When Enter password
        Then Verify Home Screen


