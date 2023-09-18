from behave import given, when, then


@given("Launch the group")
def methodOne(context):
    print("L1 - Launching the group")


@when("update the group details")
def methodTwo(context):
    print("L2 - published the group")


@then("Verify group")
def methodSix(context):
    print("L3 - verified group ")