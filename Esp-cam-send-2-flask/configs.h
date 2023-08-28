const char *ssid = "BK Star";
const char *password = "bkstar2021";
const char *post_url = "http://192.168.1.126:81/upload-image"; // Location where images are POSTED

const int threshold = 40;
const int buzzer_pin = 16;
const int motor_pin = 12;

void pin_init(){
  pinMode(buzzer_pin, OUTPUT);
  pinMode(motor_pin, OUTPUT);
}