"""Cucumber steps"""
from behave import given, when, then

from pygame.math import Vector2
from pygame import K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, K_h, K_c

from rc_car.audio_effect import AudioEffect
from rc_car.car import Car
from rc_car.remote import Remote


@given('the app is connected to the race car and the race car is charged')
def the_app_is_connected_to_the_race_car_and_the_race_car_is_charged(context):
    """initialise a car and the remote"""
    init(context, True)


@given('the race car is out of battery')
def the_race_car_is_out_of_battery(context):
    """initialise a car out of battery and the remote"""
    init(context, False)


@given('the parental controls "{text}" previously been configured')
def the_parental_controls_previously_been_configured():
    """TODO, considering 'context' and 'text' as input args"""
    # have not
    # have


@given('the user has validated parental control credentials')
def the_user_has_validated_parental_control_credentials():
    """TODO, considering 'context' as input arg"""


@given('the server is online')
def the_server_is_online():
    """TODO, considering 'context' as input arg"""


@when('the user pushes a direction')
def the_user_pushes_a_direction(context):
    """moves the car forward"""
    push_button(context, K_UP)


@when('the user selects a LED colour scheme')
def the_user_selects_a_led_colour_scheme():
    """TODO, considering 'context' as input arg"""


@when('the user pushes the "{text}" button')
def the_user_pushes_the_button(context, text):
    """pushes a button on the remote"""
    # horn
    # customise driver
    # battery
    # parental control
    if text == 'horn':
        push_button(context, K_h)
    else:
        raise NotImplementedError


@when('the user tries to connect the remote')
def the_user_tries_to_connect_the_remote(context):
    """tries to drive the car"""
    push_button(context, K_UP)


@when('inserts the correct password')
def inserts_the_correct_password():
    """TODO, considering 'context' as input arg"""


@when('"{text}" is selected')
def option_is_selected():
    """TODO, considering 'context' and 'text' as input args"""
    # maximum speed


@when('a picture is uploaded')
def a_picture_is_uploaded():
    """TODO, considering 'context' as input arg"""
    # maximum speed


@when('the app is online')
def the_app_is_online():
    """TODO, considering 'context' as input arg"""


@then('the user is prompted to set "{text}"')
def the_user_is_prompted_to_set_option():
    """TODO, considering 'context' and 'text' as input args"""
    # driver’s appearance
    # a password
    # the maximum speed


@then('the car moves in that direction')
def the_car_moves_in_that_direction(context):
    """verify a forward movement"""
    assert context.car.status['velocity'].x > 0
    assert context.car.status['velocity'].y == 0
    assert context.car.status['position'].x > 0
    assert context.car.status['position'].y == 0


@then('the car sounds the horn')
def the_car_sounds_the_horn(context):
    """verify the horn"""
    assert \
        context.audio_handler_calls[len(context.audio_handler_calls)-1].value.path\
            == AudioEffect.HORN.value.path


@then('the car LEDs change colour to the selected scheme')
def the_car_leds_change_colour_to_the_selected_scheme():
    """TODO, considering 'context' as input arg"""


@then('the {text} is updated in the app')
def the_option_is_updated_in_the_app():
    """TODO, considering 'context' and 'text' as input args"""
    # driver's appearance
    # colour scheme


@then('the appearance is updated on the race car')
def the_appearance_is_updated_on_the_race_car():
    """TODO, considering 'context' as input arg"""


@then('the app displays the estimated range left in the battery')
def the_app_displays_the_estimated_range_left_in_the_battery():
    """TODO, considering 'context' as input arg"""


@then('the remote suggests that the race care is out of range or the battery is empty')
def the_remote_suggests_that_the_race_care_is_out_of_range_or_the_battery_is_empty(context):
    """verify the notification"""
    assert len(context.notifications) > 0
    assert context.notifications[len(context.notifications)-1] \
        == 'The car is unreachable or out of battery'


@then('the server is notified')
def the_server_is_notified():
    """TODO, considering 'context' as input arg"""


def init(context, battery_is_full: bool):
    """utility method to initialise the car with full/empty battery"""
    def audio_handler(effect):
        context.audio_handler_calls.append(effect)

    def notifications(message):
        context.notifications.append(message)

    def check_walls_handler():
        """TODO, considering 'position' (Vector2) as input arg"""
        return True

    context.pressed = {
        K_RIGHT: False, K_UP: False, K_LEFT: False, K_DOWN: False,
        K_SPACE: False, K_h: False, K_c: False
    }
    context.audio_handler_calls = []
    context.notifications = []
    context.car = Car(Vector2(0, 0), audio_handler, check_walls_handler)
    if not battery_is_full:
        context.car.battery.consume(100)
    context.remote = Remote(notifications)
    context.remote.connect_to(context.car)


def push_button(context, button):
    """utility method to send a command"""
    context.pressed[button] = True
    context.remote.command(context.pressed, 1)
    context.pressed[button] = False
