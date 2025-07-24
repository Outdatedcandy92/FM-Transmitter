import time
import board
import busio
from adafruit_bus_device.i2c_device import I2CDevice

DEVICE_ADDRESS = 0x36  # KT0803L I2C address

# Initialize I2C on Pico (adjust pins if necessary)
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)

# Wait for I2C bus ready
while not i2c.try_lock():
    pass
i2c.unlock()

# Wait until device is detected on I2C bus with timeout
timeout = 5  # seconds
start_time = time.monotonic()
device_found = False

while (time.monotonic() - start_time) < timeout:
    while not i2c.try_lock():
        pass
    devices = i2c.scan()
    i2c.unlock()

    if DEVICE_ADDRESS in devices:
        device_found = True
        print(f"Device 0x{DEVICE_ADDRESS:02X} found on I2C bus.")
        break
    else:
        print(f"Device 0x{DEVICE_ADDRESS:02X} not found, retrying...")
        time.sleep(0.5)

if not device_found:
    raise RuntimeError(f"Device 0x{DEVICE_ADDRESS:02X} not found after {timeout} seconds.")

device = I2CDevice(i2c, DEVICE_ADDRESS)

def write_register(register, value):
    with device:
        device.write(bytes([register, value]))

def read_register(register):
    result = bytearray(1)
    with device:
        device.write_then_readinto(bytes([register]), result)
    return result[0]

def set_frequency_mhz(freq_mhz):
    chsel = int(freq_mhz * 20) & 0xFFF
    chsel_11_9 = (chsel >> 9) & 0x7
    chsel_8_1 = (chsel >> 1) & 0xFF
    chsel_0 = chsel & 0x1

    current_reg_2 = read_register(0x02)
    reg_2_new = (current_reg_2 & 0x7F) | (chsel_0 << 7)

    current_reg_1 = read_register(0x01)
    reg_1_new = (current_reg_1 & 0xF8) | chsel_11_9

    write_register(0x00, chsel_8_1)
    time.sleep(0.05)
    write_register(0x01, reg_1_new)
    time.sleep(0.05)
    write_register(0x02, reg_2_new)
    time.sleep(0.05)

    print(f"Frequency set to {freq_mhz} MHz (CHSEL=0x{chsel:03X})")
    print("Register 0x00:", hex(read_register(0x00)))
    print("Register 0x01:", hex(read_register(0x01)))
    print("Register 0x02:", hex(read_register(0x02)))

# Input loop
while True:
    try:
        user_input = input("Enter FM frequency in MHz (e.g. 106.5) or 'exit': ").strip().lower()
        if user_input == "exit":
            print("Exiting program.")
            break
        freq = float(user_input)
        if 70.0 <= freq <= 108.0:
            set_frequency_mhz(freq)
        else:
            print("Please enter a frequency between 70.0 and 108.0 MHz.")
    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")
