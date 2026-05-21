def on_forever():
    if input.logo_is_pressed():
        radio.send_number(0)
basic.forever(on_forever)

def on_forever2():
    if input.is_gesture(Gesture.SCREEN_DOWN):
        radio.send_number(1)
basic.forever(on_forever2)

def on_forever3():
    if input.button_is_pressed(Button.B):
        radio.send_number(2)
basic.forever(on_forever3)

def on_forever4():
    if input.button_is_pressed(Button.A):
        radio.send_number(3)
basic.forever(on_forever4)

def on_forever5():
    if input.button_is_pressed(Button.AB):
        radio.send_number(4)
basic.forever(on_forever5)

def on_forever6():
    basic.show_leds("""
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        # # # # #
        # . . . .
        # . # # #
        # . . . #
        # # # # #
        """)
    basic.pause(1000)
    basic.show_leds("""
        # # # # #
        # . . . .
        # # # # #
        . . . . #
        # # # # #
        """)
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(2000)
basic.forever(on_forever6)
