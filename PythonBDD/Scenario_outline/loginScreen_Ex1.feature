# This is a Feature file

Feature: Fill the Contact Form

    Scenario: Student Login credentials

        Given Launch the App and Click on Login Button
        When Enter "student@gmail.com" UserID
        When Enter "S1234" password
        Then Verify Home Screen


    Scenario: Teacher Login credentials

        Given Launch the App and Click on Login Button
        When Enter "teacher@gmail.com" UserID
        When Enter "T1234" password
        Then Verify Home Screen
