import logging

from behave import step

from features.env_utils import get_testing_user_name
from features.steps.pages.profile_page import ProfilePage as PP


@step("I see the user name is displayed in the page")
def verify_user_name_is_displayed(context):
    user_name_expected = get_testing_user_name(context).lower()
    profile_page: PP = context.current_page
    user_name_displayed = profile_page.get_user_name_displayed()
    logging.info("User name displayed: '{}'".format(user_name_displayed))
    assert (
        user_name_displayed == user_name_expected
    ), "User name is not displayed in profile page"
    logging.info("User name is displayed in profile page")


@step("I see the profile page is displayed")
def verify_profile_page_is_displayed(context):
    profile_page: PP = context.current_page
    current_url = profile_page.get_current_url()
    assert (
        "profile" in current_url
    ), "Current url is not the profile url. Current url: {}".format(current_url)
    logging.info("Current url is the profile url")
