#include "Std_Types.h"
#include "Macros.h"
#include "DIO_interface.h"
#include "APP_interface.h"

void main(void)
{
	APP_vidInit();

	while(1) {
		APP_vidControl();
	}
}
