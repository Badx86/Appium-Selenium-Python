# This is a Feature file

@webpage
Feature: SocialNetwork Webpage Tests

    @profile @login @logout
    Scenario: Profile related cases

        Given Launch the profile page
        When Change profile pic
        Then Verify profile pic

    @feed @login
    Scenario: Feeds related cases

        Given Launch the feed page
        When publish the feed
        Then Verify feed



    @pages
    Scenario: Pages related cases

        Given Launch the page
        When update the page data
        Then Verify page

    @group @profile
    Scenario: Group related cases

        Given Launch the group
        When update the group details
        Then Verify group

