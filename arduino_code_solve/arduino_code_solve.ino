#include <Stepper.h>
#include <Servo.h> 
#include <string.h>

const int stepsPerRevolution = 200 ;
const int stepstaken = 50; //90 degree
// Create Instance of Stepper library
Stepper mystepper_1(stepsPerRevolution, 8, 9, 10, 11);
Stepper mystepper_2(stepsPerRevolution, 4, 5, 6, 7);
Servo myservo_1;
Servo myservo_2;


void ST1a()
{
  // step one revolution in one direction:
  //Serial.println("stepper motor front counterclockwise");
  mystepper_1.step(stepstaken);
  delay(500);
}

void ST1()
{
  // step one revolution in the other direction:
  mystepper_1.step(-stepstaken);
  delay(500);
}

void ST2a()
{
  // step one revolution in one direction:
  //Serial.println("stepper motor back counterclockwise");
  mystepper_2.step(stepstaken);
  delay(500);
}

void ST2()
{
  // step one revolution in the other direction:
  //Serial.println("stepper motor back clockwise");
  mystepper_2.step(-stepstaken);
  delay(500);
}

void rt()
{
  //Serial.println("rotate clockwise");
  for(int a=0; a<=10; a++)
  {
  mystepper_1.step(a);
  mystepper_2.step(a);
  }
}

void rta()
{
  //Serial.println("rotate counterclockwise");
  for(int s=0; s<10; s++)
  {
  mystepper_1.step(-s);
  mystepper_2.step(-s);
  }
}


void SV1()
{
  //Serial.println("arm clockwise");
  for(int pos = 50; pos <= 180; pos += 4)
  {                                  
    myservo_1.write(pos);      
    delay(15);
    //myservo_1.detach();
    
  }
  
}

void SV1a()
{
  //Serial.println("arm anticlockwise");
  for(int pos = 180; pos >=50; pos -= 4) 
  {                                  
    myservo_1.write(pos);      
    delay(15);
    //myservo.detach();
    
  }
}

void SV2a()
{
  //Serial.println("arm engage");
  for(int pos = 0; pos <= 180; pos += 5) 
    myservo_2.write(pos);      
    delay(15);
    //myservo.detach();
  }


void SV2()
{
  //Serial.println("arm disengage");
  for(int pos = 360; pos >=0; pos -= 5) 
  {                                  
    myservo_2.write(pos);      
    delay(15);
    //myservo.detach();
    
  }
}

void setup() {

  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  // set the speed at 60 rpm:
  mystepper_1.setSpeed(60);
  mystepper_2.setSpeed(60);
  myservo_1.attach(12);
  myservo_2.attach(13);
  Serial.begin(19200);
  //Serial.setTimeout(1);
}

void loop() {
  // put your main code here, to run repeatedly:
    String x;
    String y;
    String z;
    int i;
    int j;
    j = 0;

    if(Serial.available()){
        
        x = Serial.readString();
        //Serial.println(x[x.length()-1]);
        y = x.substring(1,x.length()-1);
        if (y.length() > 4){
            Serial.println(y);
            j = 1;
        }
        else
            Serial.println("none");
    }
    
    if (j == 1){
        digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
        delay(1000);                      // wait for a second
        digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
        delay(1000);
        for (i=0; i<y.length(); i++){
            if (y[i] == 'A')
                {
                ST1();
                
            }
            else if  (y[i] == 'B')
            {
                ST1a();
                
            }
            else if  (y[i] == 'C')
            {
                ST2();
                
            }
            else if  (y[i] == 'D')
            {
                ST2a();
                
            }
            else if  (y[i] == 'E')
            { 
                SV2a();
                
            }
            else if  (y[i] == 'F')
            {
                SV2();
                
            }
            else if  (y[i] == 'G')
            {
                rt();
                
            }
            else if  (y[i] == 'H')
            {
                rta();
                
            }
            else if  (y[i] == 'I')
            {
                SV1();
                
            }
            else if  (y[i] == 'J')
            {
                SV1a();
                
            }
          }
        }
}
