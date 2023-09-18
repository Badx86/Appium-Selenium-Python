from behave import given, when, then


@given("Launch the App and Click on ContactForm")
def methodOne(context):
    print("C1 - Launching the App")


@when("Launch the App and Click on ContactForm")
def methodTwo(context):
    print("C2 - Enter the UserID in Login Screen")


@when("Enter Name")
def methodThree(context):
    print("C3 - Enter the Password in Login Screen")


@when("Enter Email")
def methodFour(context):
    print("C4 - Clicked on the login Button")


@when("Enter Mobile Number")
def methodFive(context):
    print("C5 - Home Screen Opened")


@when("we need to click on submit button")
def methodSix(context):
    print("C6 - Clicking on Submit button")


@then("Click on submit")
def methodSix(context):
    print("C7 - Click on the submit button")


@then("Take Screenshot of contact Form")
def methodSix(context):
    print("C8 - ScreenShot taken")
