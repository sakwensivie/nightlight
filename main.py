
basic.show_string('Hello World')
basic.pause(500)

list1 = [1, 2, 3, 4]
input.calibrate_compass()
for i in list1:
    basic.show_number(i)
    basic.pause(300)

def forever():
    if input.light_level() <= 125:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    else:
        basic.clear_screen()
basic.forever(forever)
