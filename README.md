# AVR LED Controller
## Summary
Controlling 4 LEDs by sending signals from a computer connected to the AVR ATMega MCU via UART. From the computer side, the connection and signaling is done via a GUI developed using Python  with the Tkinter library.

## Features
Control LEDs by toggling or turning each of them on for a specfic time.

## Notes
`pyserial` is used in the python script. To install it on your system run `pip3 install pyserial`.

Turn GUI Python script into an executable using `pyinstaller.exe --noconsole ./gui.py`

## Pictures
![image](/images/gui_screenshot.png)
