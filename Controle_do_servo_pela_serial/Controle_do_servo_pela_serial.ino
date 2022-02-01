include <Servo.h>   //inclui biblioteca para controle de servo


// ========================================================================================================
// --- Objetos ---
String fraseRecebida = ""; // a String to hold incoming data
bool fraseCompleta = false;  // whether the string is complete

Servo myservoA = 90;       //cria objeto para 1 servo motor
Servo myservoB = 90; 

// ========================================================================================================
// --- Configurações Iniciais ---
void setup()
{

  Serial.begin(9600);   //inicializa serial em 9600 bps
  while (!Serial);      //aguarda iniciliazação da serial
  fraseRecebida.reserve(100);    //reserve 200 bytes pra inputString
  
  myservoA.attach(9);    //associa servoA ao pino 9
  myservoB.attach(8);    //associa servoB ao pino 8

  Serial.println("Digite o grau de movimento para A e/ou B e tecle enter...");

 
} //end setup


// ========================================================================================================
// --- Loop Infinito ---
void loop() 
{
  
  if(Serial.available())
  {
    if (
    int state = Serial.parseInt();
  
  
    if (state > 0 && state <= 180)
    {
      Serial.print(" | ");
      Serial.println(estadoa);
      Serial.print(" | ");
      Serial.println(estadob);
      Serial.print("ServoA em");
      Serial.print(estadoa);
      Serial.print("/nServoB em");
      Serial.print(estadob);
      Serial.println(" graus");
      myservoA.write(estadoa);
      myservoB.write(estadob);
      
    }
  
  } //end if serial available

} //end loop
