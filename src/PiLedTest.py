from hal import hal_input_switch as input_switch
from hal import hal_led as led
from time import sleep

def main():
    i = 0
    led.init()
    input_switch.init()
    while(1):
        if (input_switch.read_slide_switch() == 1):
            i = 0
            led.set_output(24, 1)
            sleep(0.2)
            led.set_output(24, 0)
            sleep(0.2)
        else:
            if i < 25:
                led.set_output(24, 1)
                sleep(0.1)
                led.set_output(24, 0)
                sleep(0.1)
                i += 1

if __name__ == "__main__":
    main()