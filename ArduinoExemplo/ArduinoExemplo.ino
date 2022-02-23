                                                              CÓDIGO ESP32
int ledAzul = 18;
int ledVermelho = 14;
int valor_recebido;

void setup() {
  Serial.begin(9600);
  pinMode(ledVermelho, OUTPUT);
  pinMode(ledAzul, OUTPUT);

}

void loop() {
  if(Serial.available() > 0)
  {
    valor_recebido = Serial.read();
  }
  if(valor_recebido == '1'){
    digitalWrite(ledVermelho,HIGH);
  }
  else if(valor_recebido == '0'){
    digitalWrite(ledVermelho,LOW);
  }
   else if(valor_recebido == '2'){
    digitalWrite(ledAzul,HIGH);
  }
   else if(valor_recebido == '3'){
    digitalWrite(ledAzul,LOW);
  }

}
