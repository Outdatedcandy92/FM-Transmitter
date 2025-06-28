# USB FM Transmitter

This project is a compact USB controlled FM transmitter module designed to stream and transmit audio directly from your computer to a FM band. This is a plug and play module and will work without installing any drivers or running any custom commands. Just simply plug it into your PC and start transmitting audio. This project uses the PCM2704 to receive audio from the host device and sends it off to the KT0803L chip to transmit over FM band. There are test pads on the board for the PCM2704 chips HID controls such as Mute, Volume Up/Down and Suspend. There is also a connector on board for communicating over I2C with the KT0803L. You can use I2C to change KT0803L's Transmitting Frequency, calibration parameters, operation statues, mode and power controller. 

![image](https://github.com/user-attachments/assets/5dab3f29-4b65-4304-82bd-dee0ef40d9a4)

## Demo

https://github.com/user-attachments/assets/b6735c28-1eea-4149-aa80-006a72d71160

## Images

### Schematic
![Img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/cc17f78b0bf7a4f6c3af12b0c0e1fe82bd91bd30_image.png)

### PCB
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/3717b2d04b689a615e3bf28a02f560db76c50bef_image.png)

### 3D 

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/b912fc075f5644e4bc130a5ec07b70816ee20c37_image.png)


