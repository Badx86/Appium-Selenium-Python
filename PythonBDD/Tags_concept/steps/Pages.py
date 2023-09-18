from behave import given, when, then


@given("Launch the page")
def methodOne(context):
    print("L1 - Launching the  page")


@when("update the page data")
def methodTwo(context):
    print("L2 - updated the page")


@then("Verify page")
def methodSix(context):
    print("L3 - verified page")