from behave import given, when, then


@given("Launch the feed page")
def methodOne(context):
    print("L1 - Launching the feed page")


@when("publish the feed")
def methodTwo(context):
    print("L2 - published the feed")


@then("Verify feed")
def methodSix(context):
    print("L3 - verified feed ")
