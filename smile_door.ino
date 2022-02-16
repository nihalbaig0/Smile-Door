/*
 * Project Name : Smile Door
 * Steps:
 * 1. Gets signal from Raspberry Pi if Smile Detected
 * 2. Rotates the servo from 0 degree to 90 degree ( Door opens)
 * 3. After 10 seconds the servo rotates from 90 degree to 0 degree automatically.(Door Closes)
 * 4. Waits for another Smile signal
 * 
 * Made By : Mirza Nihal Baig
 * Github Profile : nihalbaig0
 */
#include<Servo.h>

#define SERVO_PIN 12
Servo servo;

unsigned long last_time = millis();
unsigned long delayOfServo = 10000;

int flag = 0;
String cmd;

void setup() {
  // put your setup code here, to run once:
  servo.attach(SERVO_PIN);
  servo.write(0);
  
 Serial.begin(115200);
  
while(!Serial){
  
}
}

void loop() {
  if(Serial.available() > 0){
  
 //receives signal from pi and stores in cmd variable 
 cmd = Serial.readStringUntil('\n');
 }

 // waits for 10 seconds after Door opens and sets flag to 0
unsigned int timeNow = millis();
if(timeNow - last_time >= delayOfServo){
  last_time = timeNow;
  if(flag==1){
 Serial.println("start");
  servo.write(0);
  flag = 0;
  }
 }

// if door is open then cmd is overwritten 
if(flag==1){
    cmd = " ";
}

// if Smile is Detected then door opens and flag is set to 1
if(cmd == "Smile Detected" && flag==0){
  Serial.println("stop");
  servo.write(90);
  flag = 1;
 }
 }
  
