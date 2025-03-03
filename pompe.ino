#include <Servo.h>

Servo myservo; // Objet Servo pour contrôler la pompe
int speed = 1500; // Vitesse initiale (1500 = arrêt)
const int minSpeed = 500; // Vitesse minimale
const int maxSpeed = 1500; // Vitesse maximale (1500 = arrêt)

void setup() {
    myservo.attach(9); // Attacher le servo sur la broche 9
    Serial.begin(9600); // Initialisation de la communication série
}

void loop() {
    if (Serial.available() > 0) { // Vérifie si des données sont reçues
        int newSpeed = Serial.parseInt(); // Lire une valeur entière

        if (newSpeed == -1) { // Commande pour arrêter la pompe
            speed = 1500;
        } else if (newSpeed >= minSpeed && newSpeed <= maxSpeed) { 
            speed = newSpeed; // Met à jour la vitesse
        }

        myservo.writeMicroseconds(speed); // Applique la nouvelle vitesse
    }
}
