#ifndef _APP_INTERFACE_H
#define _APP_INTERFACE_H

/*Function declarations*/
void APP_vidInit(void);
void APP_vidCountOneSec(void);
void APP_vidControl(void);
void APP_vidReceiveControlFrame(void);

/*Macros*/
#define MESSAGESIZE 4

#endif
