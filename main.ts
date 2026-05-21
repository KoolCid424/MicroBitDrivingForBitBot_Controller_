basic.forever(function () {
    if (input.logoIsPressed()) {
        radio.sendNumber(0)
    }
})
basic.forever(function () {
    if (input.isGesture(Gesture.ScreenDown)) {
        radio.sendNumber(1)
    }
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.B)) {
        radio.sendNumber(2)
    }
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        radio.sendNumber(3)
    }
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.AB)) {
        radio.sendNumber(4)
    }
})
basic.forever(function () {
    basic.showLeds(`
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        `)
    basic.pause(1000)
    basic.showLeds(`
        # # # # #
        # . . . .
        # . # # #
        # . . . #
        # # # # #
        `)
    basic.pause(1000)
    basic.showLeds(`
        # # # # #
        # . . . .
        # # # # #
        . . . . #
        # # # # #
        `)
    basic.pause(1000)
    basic.clearScreen()
    basic.pause(2000)
})
