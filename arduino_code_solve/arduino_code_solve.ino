#include <Stepper.h>
#include <Servo.h> 
#include <string.h>

const int stepsPerRevolution = 200 ;
const int stepstaken = 50; //90 degree
// Create Instance of Stepper library
Servo servo_down;
Servo servo_front;
Servo servo_right;
Servo servo_left;
Servo servo_back;


void F()
{
  //Serial.println("arm clockwise");
  servo_front.write(135);
  delay(150);
  servo_front.write(90);
  delay(1000);
  }
  

void F2()
{
    serial_front.write(135);
    delay(300);
    servo_front.write(90);
    delay(1000);
    }


void AF()
{
  //Serial.println("arm clockwise");
  servo_front.write(45);
  delay(150);
  servo_front.write(90);
  delay(1000);
  }
  

void AF2()
{
    serial_front.write(45);
    delay(300);
    servo_front.write(90);
    delay(1000);
    }


void R()
{
  //Serial.println("arm clockwise");
  servo_right.write(135);
  delay(150);
  servo_right.write(90);
  delay(1000);
  }
  

void R2()
{
    serial_right.write(135);
    delay(300);
    servo_right.write(90);
    delay(1000);
    }


void AR()
{
  //Serial.println("arm clockwise");
  servo_right.write(45);
  delay(150);
  servo_right.write(90);
  delay(1000);
  }
  

void AR2()
{
    serial_right.write(45);
    delay(300);
    servo_right.write(90);
    delay(1000);
    }


void B()
{
  //Serial.println("arm clockwise");
  servo_back.write(135);
  delay(150);
  servo_back.write(90);
  delay(1000);
  }
  

void B2()
{
    serial_back.write(135);
    delay(300);
    servo_back.write(90);
    delay(1000);
    }


void AB()
{
  //Serial.println("arm clockwise");
  servo_back.write(45);
  delay(150);
  servo_back.write(90);
  delay(1000);
  }
  

void AB2()
{
    serial_back.write(45);
    delay(300);
    servo_back.write(90);
    delay(1000);
    }


void L()
{
  //Serial.println("arm clockwise");
  servo_left.write(135);
  delay(150);
  servo_left.write(90);
  delay(1000);
  }
  

void L2()
{
    serial_left.write(135);
    delay(300);
    servo_left.write(90);
    delay(1000);
    }


void AL()
{
  //Serial.println("arm clockwise");
  servo_left.write(45);
  delay(150);
  servo_left.write(90);
  delay(1000);
  }
  

void AL2()
{
    serial_left.write(45);
    delay(300);
    servo_left.write(90);
    delay(1000);
    }


void D()
{
  //Serial.println("arm clockwise");
  servo_down.write(135);
  delay(150);
  servo_down.write(90);
  delay(1000);
  }
  

void D2()
{
    serial_down.write(135);
    delay(300);
    servo_down.write(90);
    delay(1000);
    }


void AD()
{
  //Serial.println("arm clockwise");
  servo_down.write(45);
  delay(150);
  servo_down.write(90);
  delay(1000);
  }
  

void AD2()
{
    serial_down.write(45);
    delay(300);
    servo_down.write(90);
    delay(1000);
    }


void setup() {

  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  // set the speed at 60 rpm:
  servo_bottom.attach(2);
  servo_front.attach(3);
  servo_right.attach(4);
  servo_left.attach(5);
  servo_back.attach(6);
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
    else
    {
        F();
    }
    
    if (j == 1){
        digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
        delay(1000);                      // wait for a second
        digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
        delay(1000);
    
        for (i=0; i<y.length(); i++){
            if (y[i] == 'A')
            {
                F();    
            }
            else if  (y[i] == 'B')
            {
                F2(); 
            }
            else if  (y[i] == 'C')
            {
                AF();
            }
            else if  (y[i] == 'D')
            {
                AF2();
            }
            else if  (y[i] == 'E')
            { 
                R();
            }
            else if  (y[i] == 'F')
            {
                R2();
            }
            else if  (y[i] == 'G')
            {
                AR();
            }
            else if  (y[i] == 'H')
            {
                AR2();
            }
            else if  (y[i] == 'I')
            {
                B();
            }
            else if  (y[i] == 'J')
            {
                B2();
            }
            else if  (y[i] == 'K')
            {
                AB();
            }
            else if  (y[i] == 'L')
            {
                AB2();
            }
            else if  (y[i] == 'M')
            {
                L();
            }
            else if  (y[i] == 'N')
            {
                L2();
            }
            else if  (y[i] == 'O')
            {
                AL();
            }
            else if  (y[i] == 'P')
            {
                AL2();
            }
            else if  (y[i] == 'Q')
            {
                D();
            }
            else if  (y[i] == 'R')
            {
                D2();
            }
            else if  (y[i] == 'S')
            {
                AD();
            }
            else if  (y[i] == 'T')
            {
                AD2();
            }
          }
        }
}
