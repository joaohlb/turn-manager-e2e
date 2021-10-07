from behave import given, when, then


@given('character creation is "{state}"')
def step_impl(context, state):
    if (state == 'shown') != context.browser.find_element_by_css_selector('form.char-form').is_displayed():
        context.browser.find_element_by_id('add-char').click()


@when('user toggles character creation')
def step_impl(context):
    context.browser.find_element_by_id('add-char').click()


@then('character form is "{display}"')
def step_impl(context, display):
    assert (display == 'shown') is context.browser.find_element_by_css_selector('form.char-form').is_displayed()
