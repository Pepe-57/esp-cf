# Release Notes

## Development Version 1.1 (23.6.2023)
### Bug fixes:
- Fixed word 'None' from appearing to the last line in console
### New features and improvements:
- Added 'Exit to console' to settings.
- More commands to console.
- Led control: Added the ability to control an LED connected to Pin 2.
- Small improvements.
### New console commands
- update: Provides information about the current version and instructions for downloading the latest version from [GitHub](https://github.com/Pepe-57/esp-cf).
- blink 'speed' 'times': Blinks the LED at a specified speed and number of times.
- repeat 'word': Repeats a given word.
- run 'program': Launches the specified program (calculator, settings, sysinfo, console).
- programs: Displays the available programs.

## Name chanced to ESP-CF (23.6.2023)
The name of the ESP-OS has officially changed to 'ESP-CF' because its more like a custom firmware that an operating system.

## Development Version 1.0 (20.6.2023)
- Initial release of ESP-OS DEV 1.0
- Basic functionalities implemented:
  - Calculator: Perform basic mathematical operations.
  - Settings: Configure CPU clockspeed and Wi-Fi settings.
  - SysInfo: View information about the operating system.
  - Console: Execute commands
  - Desktop: Main interface to access different programs.
- Known issues:
  - When executed 'systeminfo' or an unknown command, 'None' appears in the last line.
