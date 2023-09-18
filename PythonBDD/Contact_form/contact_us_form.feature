
Feature: Logging in with valid credentials

    Scenario Outline: User login successfully

        Given I create a new user
        When I type "abc@gmail.com" email
        When I type 'abcd' password
        When I click on 'Login'
        When Enter uname '<username>'
        When Enter passw '<password>'
        Then I should see the text Welcome



        Examples:
            | username  | password |
            | abc@gmail | 123456   |


