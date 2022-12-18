basic.showString("Hello World")
basic.pause(500)
basic.forever(function () {
    if (input.lightLevel() <= 125) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
        basic.clearScreen()
    }
})
