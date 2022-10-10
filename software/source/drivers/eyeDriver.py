import time
import busio
import board
import adafruit_amg88xx



if __name__ == "__main__":
    i2c = busio.I2C(board.SCL, board.SDA)
    amg = adafruit_amg88xx.AMG88XX(i2c)
    while True:
        for row in amg.pixels:
            print(['{0:.1f}'.format(temp) for temp in row])
            print("")
        print("\n")
        time.sleep(1)