#include "Std_Types.h"
#include "Macros.h"
#include "DIO_interface.h"
#include "TIMER0_interface.h"
#include "UART_interface.h"
#include "INTERRUPTS_interface.h"
#include "APP_interface.h"


volatile u16 u16OVFCount = 0;
volatile u8 u8Byte = 0;
volatile u8 u8index = 0;
volatile u8 u8MessageArray[MESSAGESIZE];

void APP_vidInit(void)
{
	/*LED pins configuration*/
	DIO_vidSetPinDirection(DIO_PORTA,DIO_PIN0,DIO_OUTPUT);
	DIO_vidSetPinDirection(DIO_PORTA,DIO_PIN1,DIO_OUTPUT);
	DIO_vidSetPinDirection(DIO_PORTA,DIO_PIN2,DIO_OUTPUT);
	DIO_vidSetPinDirection(DIO_PORTA,DIO_PIN3,DIO_OUTPUT);


	/*Initiating timer*/
//	TIMER0_vidInit(TIMER0_WGM_NORMAL,TIMER0_COM_NORMAL,TIMER0_CLK_1);

	/*Enabling timer interrupt*/
	INTERRUPTS_vidEnableInterrupt(INTERRUPTS_TIMER0_OVF);
	INTERRUPTS_vidPutISRFunction(INTERRUPTS_TIMER0_OVF,APP_vidCountOneSec);

	/*Enabling UART*/
	UART_vidInit();

	/*Enabling UART interrupt*/
	INTERRUPTS_vidEnableInterrupt(INTERRUPTS_USART_RXC);
	INTERRUPTS_vidPutISRFunction(INTERRUPTS_USART_RXC,APP_vidReceiveControlFrame);

	/*Enabling global interrupt*/
	INTERRUPTS_vidSetGlobalInterruptFlag();
}

void APP_vidCountOneSec(void)
{
	u16OVFCount++;
}

void APP_vidReceiveControlFrame(void)
{
	/*Get received bytes*/
	u8Byte = UART_u8GetReceivedByte();
	u8MessageArray[u8index] = u8Byte;
	u8index++;
	/*Check if the number of byte received equals the message size*/
	if (u8index == MESSAGESIZE)
	{
		u8index = 0;
		if (u8MessageArray[0] == 'a')
		{
			DIO_vidTogglePin(DIO_PORTA,DIO_PIN0);
		}
		else if (u8MessageArray[0] == 'b')
		{
			DIO_vidTogglePin(DIO_PORTA,DIO_PIN1);
		}
		else if (u8MessageArray[0] == 'c')
		{
			DIO_vidTogglePin(DIO_PORTA,DIO_PIN2);
		}
		
	}	
}

void APP_vidControl(void)
{
	
}
