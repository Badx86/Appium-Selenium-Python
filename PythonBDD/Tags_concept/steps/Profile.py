from behave import given, when, then


@given("Launch the profile page")
def methodOne(context):
    print("L1 - Launching the feed page")


@when("Change profile pic")
def methodTwo(context):
    print("L2 - published the feed")


@then("Verify profile pic")
def methodSix(context):
    print("L3 - verified feed ")