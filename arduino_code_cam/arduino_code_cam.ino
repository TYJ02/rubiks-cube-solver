// this is a arduino code to learn how to command python
// to capture image through serial communication

// need to think of a way to create functions that listen for different cues
// or use hardware as switch (most plausible solution)


#include <Arduino.h>
#include <Servo.h> 
#include <string.h>

void setup()
{
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);

    }

void loop()
{
    Serial.println("turn 1");
    delay(1000);
    Serial.println("capture");
    Serial.println("turn 2");
    delay(1000);
    Serial.println("capture");
    Serial.println("turn 3");
    delay(1000);
    Serial.println("capture");
    Serial.println("turn 4");
    delay(1000);
    Serial.println("capture");
    Serial.println("turn 5");
    delay(1000);
    Serial.println("capture");
    }
