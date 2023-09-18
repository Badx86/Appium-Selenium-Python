from behave import given, when, then


@given("Launch the App and Click on Login Button")
def methodOne(context):
    print("L1 - Launching the App")


@when("Enter {emailid} UserID")
def methodTwo(context, emailid):
    print("L2 - Enter the UserID in Login Screen {} ".format(emailid))


@when("Enter {password} password")
def methodThree(context, password):
    print("L3 - Enter the Password {} in Login Screen".format(password))


@when("Click on Login Button")
def methodFour(context):
    print("L4 - Clicked on the login Button")


@when("Home page opens")
def methodFour(context):
    print("L5 - Home Page opened")


@then("Verify Home Screen")
def methodFive(context):
    print("L6 - Home Screen Opened")


@then("Take Screenshot")
def methodSix(context):
    print("L7 - ScreenShot taken")
