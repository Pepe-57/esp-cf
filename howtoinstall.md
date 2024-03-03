# How to install ESP-CF to ESP8266

## Requirements
- MicroPython IDE, were are using [Thonny IDE](https://github.com/thonny/thonny/releases)
- ESP8266 or ESP32(Not tested)
- MicroPython compatible firmware, [ESP8266 Firmware](https://micropython.org/download/?mcu=esp8266), [ESP32 Firmware](https://micropython.org/download/?mcu=esp32)
## Installation Steps
1. Download the [ESP-CF](https://github.com/Pepe-57/esp-cf) and Thonny IDE.
2. Install Thonny IDE.
3. When the installation is done open the Thonny IDE.
4. Go to Tools->Options->Interpreter.
5. Select your device. I'm using 'MicroPython (ESP8266)'.
6. Then select your port. I'm using 'USB Serial @ COM4'. You can have for example COM3 or COM7.
7. When you are selected your device and port, click OK.
8. Create new file and paste the code of the ESP-CF to the file. Name it and then save it to your device.
9. Click 'Run current script'. If you encounter an error try 'Stop/Restart backend' or press reset button on your device.
