# USB FM Transmitter

This project is a compact USB controlled FM transmitter module designed to stream and transmit audio directly from your computer to a FM band. This is a plug and play module and will work without installing any drivers or running any custom commands. Just simply plug it into your PC and start transmitting audio. This project uses the PCM2704 to receive audio from the host device and sends it off to the KT0803L chip to transmit over FM band. There are test pads on the board for the PCM2704 chips HID controls such as Mute, Volume Up/Down and Suspend. There is also a connector on board for communicating over I2C with the KT0803L. You can use I2C to change KT0803L's Transmitting Frequency, calibration parameters, operation statues, mode and power controller. 

*V2 pcb*
![image](https://hc-cdn.hel1.your-objectstorage.com/s/v3/da5789aecfb35969c07a151e8e7cfbb73c472d54_image.png)

## Demo

https://github.com/user-attachments/assets/b6735c28-1eea-4149-aa80-006a72d71160


## Code
Even though this board is plug and play, you can still program it over I2C to change settings on the KT0803 chip.
The code in `src/code.py` lets you change the output frequency of the chip. To run that code you must first connected the sda and scl pins on the board to any microcontroller that supports micro/circuitpython and that they both are connected to the same device (share the same ground). there is no need to add external pull up resistors as the KT0803 chip already has them inbuilt.

## Images

### Schematic
![Img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/df4a7e674726c389d2cc1d2b192aa18bff15f17f_image.png)

### PCB
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/2bc89705e76e783c74b9b033e74583064a40296f_image.png)

### 3D 

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/4a8cfe7315386cb579cf01ebbd98e6bb95372c2d_image.png)


# V2!!

Version 2 of this board includes an onboard USB hub and MCU that way you no longer need to use an external devboard to change frequencies. It also has two onboard buttons and led to change and display the frequency!!

### Schematic
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/ac813004bed33ba8df7195441967da05aeefb407_image.png)

### PCB
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/183721bdc23d810c98c669a93f3827c5e7008402_image.png)

### 3D
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/da5789aecfb35969c07a151e8e7cfbb73c472d54_image.png)