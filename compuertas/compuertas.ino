//////////////////////////////////////////////////////////////////////////////
// Arduino button tutorial 1.
//
// Demonstrates:
// - detection of pressing state
//
// Push-button must be connected as follows:
//              __,__
//   Pin2 ------o   o------ GND
//
// (C) 2011 By P. Bauermeister
// This example code is in the public domain.
//
//////////////////////////////////////////////////////////////////////////////

// Adapt these to your board and application timings:

#define BUTTON_PIN        2  // Button
#define DELAY            100  // Delay per loop in ms
boolean flag[] = {false, false, false, false, false, false};
int gol = 2;
boolean subiendo = true;

//////////////////////////////////////////////////////////////////////////////

void setup()
{
  
  for (int i = 0; i <= 6; i++) {
    pinMode(i, INPUT);
  }

  
  Serial.begin(9600);

  //gol_cambia();
}

boolean handle_button(int pin)
{
  int button_pressed = digitalRead(pin); // pin low -> pressed
  return button_pressed;
  
}

void gol_cambia()
{
 if ((gol == 8) && (subiendo == true)) {
  gol = 7;
  subiendo = false; 
 } else if ((gol == 3) && (subiendo == false)) {
  gol = 2;
  subiendo = true;
 } else if (subiendo == true) {
  gol++;
 } else {
  gol--;
 }

 Serial.println("El gol actual se hará en " + String(gol));

 delay(1000);

 gol_cambia();
}

void loop()
{

  for (int i = 0; i <= 6; i++) {
    // handle button
    
  
    if ((!handle_button(i)) && (flag[i] == false)) {
      Serial.println("Puerta " + String(i) + " abierta");
      flag[i] = true;
    } else if (handle_button(i)) {
      flag[i] = false;
    }
    
  }

  
  delay(DELAY);
}
