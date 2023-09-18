def before_all(context):
    print("1.1 Before all")


def after_all(context):
    print("1.2 After all")


def before_tag(context, tag):
    print("2.1 Before tag")


def after_tag(context, tag):
    print("2.2 After tag")


def before_feature(context, feature):
    print("3.1 Before feature")


def after_feature(context, feature):
    print("3.2 After feature")


def before_scenario(context, scenario):
    print("4.1 Before scenario")


def after_scenario(context, scenario):
    print("4.2 After scenario")


def before_step(context, step):
    print("5.1 Before step")


def after_step(context, step):
    print("5.2 After step")
