def on_received_number(receivedNumber):
    global superove_cislo, dostane
    superove_cislo = receivedNumber
    dostane = True
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global raz_dva_tri_A
    raz_dva_tri_A = raz_dva_tri_A + 1
    if raz_dva_tri_A > 3:
        raz_dva_tri_A = 1
    if raz_dva_tri_A == 1:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
    elif raz_dva_tri_A == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    elif raz_dva_tri_A == 3:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
    basic.show_string("" + str(skore[0]) + ":" + str(skore[1]))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global poslane
    radio.send_number(raz_dva_tri_A)
    poslane = True
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

poslane = False
dostane = False
superove_cislo = 0
skore: List[number] = []
raz_dva_tri_A = 0
radio.set_group(10)
raz_dva_tri_A = 0
skore = [0, 0]

def on_forever():
    global poslane, dostane, superove_cislo, raz_dva_tri_A, skore
    if poslane == True and dostane == True:
        poslane = False
        dostane = False
        if raz_dva_tri_A == superove_cislo:
            basic.show_icon(IconNames.SILLY)
        elif raz_dva_tri_A == 1 and superove_cislo == 2:
            basic.show_icon(IconNames.NO)
            skore[1] = skore[1] + 1
        elif raz_dva_tri_A == 1 and superove_cislo == 3:
            basic.show_icon(IconNames.YES)
            skore[0] = skore[0] + 1
        elif raz_dva_tri_A == 3 and superove_cislo == 2:
            basic.show_icon(IconNames.YES)
            skore[0] = skore[0] + 1
        elif raz_dva_tri_A == 2 and superove_cislo == 1:
            basic.show_icon(IconNames.YES)
            skore[0] = skore[0] + 1
        elif raz_dva_tri_A == 2 and superove_cislo == 3:
            basic.show_icon(IconNames.NO)
            skore[1] = skore[1] + 1
        elif raz_dva_tri_A == 3 and superove_cislo == 1:
            basic.show_icon(IconNames.NO)
            skore[1] = skore[1] + 1
        else:
            pass
        superove_cislo = 0
        raz_dva_tri_A = 0
        if skore[0] == 5:
            for index in range(3):
                basic.show_string("VITEZ")
                basic.show_icon(IconNames.HEART)
                basic.pause(500)
            skore = [0, 0]
        elif skore[1] == 5:
            for index2 in range(5):
                basic.show_icon(IconNames.SKULL)
                basic.clear_screen()
                basic.pause(500)
            skore = [0, 0]
        else:
            pass
basic.forever(on_forever)
