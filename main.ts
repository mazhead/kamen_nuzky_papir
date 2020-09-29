radio.onReceivedNumber(function (receivedNumber) {
    superove_cislo = receivedNumber
    dostane = true
})
input.onButtonPressed(Button.A, function () {
    raz_dva_tri_A = raz_dva_tri_A + 1
    if (raz_dva_tri_A > 3) {
        raz_dva_tri_A = 1
    }
    if (raz_dva_tri_A == 1) {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    } else if (raz_dva_tri_A == 2) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else if (raz_dva_tri_A == 3) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
    } else {
    	
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    basic.showString("" + skore[0] + ":" + skore[1])
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(raz_dva_tri_A)
    poslane = true
    basic.clearScreen()
})
let poslane = false
let dostane = false
let superove_cislo = 0
let skore: number[] = []
let raz_dva_tri_A = 0
radio.setGroup(10)
raz_dva_tri_A = 0
skore = [0, 0]
basic.forever(function () {
    if (poslane == true && dostane == true) {
        poslane = false
        dostane = false
        if (raz_dva_tri_A == superove_cislo) {
            basic.showIcon(IconNames.Silly)
        } else if (raz_dva_tri_A == 1 && superove_cislo == 2) {
            basic.showIcon(IconNames.No)
            skore[1] = skore[1] + 1
        } else if (raz_dva_tri_A == 1 && superove_cislo == 3) {
            basic.showIcon(IconNames.Yes)
            skore[0] = skore[0] + 1
        } else if (raz_dva_tri_A == 3 && superove_cislo == 2) {
            basic.showIcon(IconNames.Yes)
            skore[0] = skore[0] + 1
        } else if (raz_dva_tri_A == 2 && superove_cislo == 1) {
            basic.showIcon(IconNames.Yes)
            skore[0] = skore[0] + 1
        } else if (raz_dva_tri_A == 2 && superove_cislo == 3) {
            basic.showIcon(IconNames.No)
            skore[1] = skore[1] + 1
        } else if (raz_dva_tri_A == 3 && superove_cislo == 1) {
            basic.showIcon(IconNames.No)
            skore[1] = skore[1] + 1
        } else {
        	
        }
        superove_cislo = 0
        raz_dva_tri_A = 0
        if (skore[0] == 5) {
            for (let index = 0; index < 3; index++) {
                basic.showString("VITEZ")
                basic.showIcon(IconNames.Heart)
                basic.pause(500)
            }
            skore = [0, 0]
        } else if (skore[1] == 5) {
            for (let index = 0; index < 5; index++) {
                basic.showIcon(IconNames.Skull)
                basic.clearScreen()
                basic.pause(500)
            }
            skore = [0, 0]
        } else {
        	
        }
    }
})
