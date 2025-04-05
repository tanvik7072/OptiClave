
# **OptiClave**
At OptiClave we aim to provide to tackle the problem to microscopy within tissue hoods by providing a simple to assemble, open-source and autoclavable microscope that can accurately image inside a tissue hood.

<img src="OptiClave.png" alt="alt tag" width="300" />

## Printing
The STL files for OptiClave can be found in this repository

## Wiring

## Programming
OptiClave comes with prewritten Python to work

Install the correct dependencies:
#### PiCamera2 (for camera control)
```
sudo apt update
sudo apt install python3-picamera2
```

#### OpenCV (image processing/display)

```
sudo apt install python3-opencv
```

#### RPi.GPIO (for GPIO control)

```
sudo apt install python3-rpi.gpio
```

### Running the script
Save the script into the pi using

```
git add https://github.com/tanvik7072/OptiClave
```

Make it executable:

```
chmod +x PiCamera.py
```

Run it:

```
python3 PiCamera.py
```







