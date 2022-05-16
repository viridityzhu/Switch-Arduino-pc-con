# Switch-Fightstick
Forked from [ebith/Switch-Fightstick](https://github.com/ebith/Switch-Fightstick)  
Allow multiple keypressing  
Added python api  

## Requirement
- Arduino UNO R3
- USB to serial adapter (FT232RL)
- USB cables

## Usage
- Flash Joystick.hex into Arduino

  **Compiling and Flashing onto the Arduino UNO R3**
  
  You will need to set your [Arduino in DFU mode](https://www.arduino.cc/en/Hacking/DFUProgramming8U2), and flash its USB controller. (Note for Mac users - try [brew](https://brew.sh/index_it.html) to install the dfu-programmer with `brew install dfu-programmer`.) Setting an Arduino UNO R3 in DFU mode is quite easy, all you need is a jumper (the boards come with the needed pins in place). Please note that once the board is flashed, you will need to flash it back with the original firmware to make it work again as a standard Arduino. To compile this project you will need the AVR GCC Compiler and Tools. (Again for Mac users - try brew, adding the [osx-cross/avr](osx-cross/avr) repository, all you need to do is to type `brew tap osx-cross/avr` and `brew install avr-gcc`.) Next, you need to grab the LUFA library: download and install it following the steps described for the Teensy 2.0++.

  Finally, open a terminal window in the `Switch-Fightstick` directory, edit the `makefile` setting `MCU = atmega16u2`, and compile by typing `make`. Follow the [DFU mode directions](https://www.arduino.cc/en/Hacking/DFUProgramming8U2) to flash `Joystick.hex` onto your Arduino UNO R3 and you are done.
- Connect adapter to Arduino as following:  
		VCC -> 5V  
		GND -> GND  
		RXD -> RX  
		TX -> TX  
- PC/Mac -> Adapter -> Arduino [-> Switch Dock (optional)] -> Switch
