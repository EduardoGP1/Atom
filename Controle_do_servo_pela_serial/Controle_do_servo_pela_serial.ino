#include <Servo.h>

Servo myservo;       //cria objeto para 1 servo motor


// ========================================================================================================
// --- Configurações Iniciais ---
void setup()
{

  Serial.begin(2000000);   //inicializa serial em 9600 bps
  
  while (!Serial);      //aguarda iniciliazação da serial
  
  delay(1000);          //aguarda 1 segundo
   
  myservo.attach(9);    //associa servo ao pino 9

 
} //end setup


// ========================================================================================================
// --- Loop Infinito ---
void loop() 
{
  
  if(Serial.available())
  {
  
    int state = Serial.parseInt();

    if (state > 0 && state < 180)
    {
      //Serial.print(" | ");
      //Serial.println(state);
      //Serial.print("Servo posicionado em ");
      //Serial.print(state);
      //Serial.println(" graus");
      myservo.write(state);
    }

    //else
    //{
      //state = 50;
      //myservo.write(state);
    //}
    
  
  } //end if serial available

} //end loop
