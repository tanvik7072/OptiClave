# -*- coding: utf-8 -*-
"""
@author: Calum Robertson - Opticlave
2025

This is an open source script for use with the 
Opticlave microscope on a Raspberry pi with 
camera module 3

"""

import time
import cv2
import RPi.GPIO as GPIO
from picamera2 import Picamera2

def RunCamera():
    #Initialising

     # --- GPIO SETUP ---
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

    
    # --- CAMERA SETUP ---
    picam2 = Picamera2()
    preview_config = picam2.create_preview_configuration({"size": (640, 480)})
    picam2.configure(preview_config)
    picam2.start()

    #Turn LED on
    GPIO.output(LED_PIN, GPIO.HIGH)
    
    print("Press 's' to take a screenshot, 'q' to quit.\n")
    
    while True:
        
        frame = picam2.capture_array()
        
        cv2.imshow("Camera Preview",frame)
        
        key = cv2.waitKey(1) & 0xFF

        #User controls
        #Screenshot
        if key == ord('s'):
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.jpg"   
            
            cv2.imwrite(filename,frame)
            print(f"Screenshot saved: {filename}\n")
            print("Press 's' to take a screenshot, 'q' to quit.\n")

        #Quit
        elif key == ord('q'):
            
            break
    
    #Clean up    
    GPIO.output(LED_PIN, GPIO.LOW)
    cv2.destroyAllWindows()
    picam2.close()
    GPIO.cleanup()


if __name__ == "__main__":
    RunCamera()
