from behave import given, when, then


@given("Launch the App and Click on Login Button")
def methodOne(context):
    print("L1 - Launching the App")


@when("Enter UserID")
def methodTwo(context):
    print("L2 - Enter the UserID in Login Screen")


@when("Enter password")
def methodThree(context):
    print("L3 - Enter the Password in Login Screen")


@then("Verify Home Screen")
def methodFour(context):
    print("L4 - Home Screen Opened")

