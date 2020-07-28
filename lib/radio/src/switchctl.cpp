#include "/home/pi/433Utils/rc-switch/RCSwitch.h"
#include <stdlib.h>
#include <stdio.h>
     

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("more arugments\n");
        return -1;
    }

    int switchnum = atoi(argv[1]);
    int command = atoi(argv[2]);
    int code = 0;
    int endcode = 0;

    if(switchnum < 1 || switchnum > 3 || command < 0 || command > 1) {
        printf("Invalid switch/command range");
        return -1;
    }
   
    if(wiringPiSetup() == -1) return 1; 
    RCSwitch rx = RCSwitch();
    rx.setPulseLength(175);
    rx.enableTransmit(0);

    if(switchnum == 1) {
        endcode = 267520;
        if(command == 1) {
            code = 267571;
        } else {
            code = 267580;

        }
    } else if (switchnum == 2) {
        endcode = 267520;
        if(command == 1) {
            code = 267715;
        } else {
            code = 267724;
        }
    } else if (switchnum == 3) {
        endcode = 267520;
        if(command == 1) {
            code = 268035;
        } else {
            code = 268044;
        }
    }


    rx.setRepeatTransmit(8);
    rx.send(code, 24);
    rx.setRepeatTransmit(1);
    rx.send(endcode, 24);
    return 0;

}
