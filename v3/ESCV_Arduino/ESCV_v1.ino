// Эелктронная система учета посетителей v3
// Автор: Мамаев Александр (alxmamaev@mail.ru)
// GitHub: https://github.com/alxmamaev/ESCV

//============================================================================================
// Подключение модулей:
//RFID:
//    10 пин - SS(slave select) управляющий пин для выбора RFID модуля 
// Ethernet:
//    8 пин - SS(slave select) управляющий пин для выбора сетевой карты
//============================================================================================

// Билиотека для работы с SPI, необходимо для работы сетевой карты и RFID приемника.
#include <SPI.h>

// Библиотека для работы с сетевой картой
#include <EtherCard.h>

// Библиотека необходимые для работы с RFID модулем
#include <MFRC522.h>

// Библиотеки для работы с дисплеем. Библиотека работает с дмсплеем по I2C, а не по SPI
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// Создаем экземпляр класса, для работы с RFID
// Первый аргумент - номер пина к которому подключен SS (slave select)
// Второй аргумент - номер пина к которому подключен RST (reset)
MFRC522 mfrc522(10, 9);   // Create MFRC522 instance.

// Создаем экземпляр класса, для работы с дисплеем.
// Второй аргумент - количество символов в строке
// Третий аргумент - количество строк
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Буффер сетевой карты
byte Ethernet::buffer[700];

// Адрес сайта на который будем стучаться (в моем случае он запускается на одном с сервером IP) 
const char website[] PROGMEM = "192.168.0.104"; //Замените на ip адрес вашего компьютера

// IP адрес сервера.
static byte websiteip[] = { 192,168,0,104 }; //Замените на ip адрес вашего компьютера

//Мак-адрес устройства
static byte mac[] = { 0x74,0x69,0x69,0x2D,0x30,0x31 };

//RFID id который мы получили от пользователя
char rfid_id[9];

// Действия после успешной отправки данных
static void my_callback (byte status, word off, word len) {
  // Очищаем буфер сетевой карты
  Ethernet::buffer[off+300] = 0;

  // Выводим информацию об успешной отправке данных на экран
  lcd.clear();
  lcd.print("Successfully!");
  delay(1000);
  lcd.clear();
  lcd.print("Waiting label..");
}

// Выбираем сетевую карту для работы по SPI.
void select_ethernet(){
  digitalWrite(8,LOW);
  digitalWrite(10,HIGH);
}

// Выбираем RFID модуль для работы по SPI
void select_rfid(){
  digitalWrite(8,HIGH);
  digitalWrite(10,LOW);  
}

// Функция отправки данных на сервер
void send_package(){
  select_ethernet();
  ether.packetLoop(ether.packetReceive());
  // Формирование Http-Get запроса
  ether.browseUrl(PSTR("/cgi-bin/processor.py?RFIDCode="),rfid_id, website, my_callback);
}

//Получение id с RFID карты и запись в rfid_id
void get_rfid_id(byte *buffer) {
    for (byte i = 0; i <= 9; i++) {
       rfid_id[i] = char(buffer[i]);
    }
}

void setup () {
  // Инициализируем SPI для работы с модулями
  SPI.begin();
  
  // Инициализируем дисплей
  lcd.begin();
  
  // Инициализация serial-монитора
  Serial.begin(9800);
  
  // Включем подстветку
  lcd.backlight();
  lcd.print("Loading...");

  // Выбираем сетевую карту, для работы по SPI
  select_ethernet();
  // Инициализация сетевой карты, второй аргумент - мак-адрес (должен быть уникальным! Можно не менять, если в сети устройства с таким адресом нет).
  if (ether.begin(sizeof Ethernet::buffer, mac) == 0) 
    Serial.println(F("Failed to access Ethernet controller"));
  else
    Serial.println(F("Successfully to access Ethernet controller"));
  if (!ether.dhcpSetup())
    Serial.println(F("DHCP failed"));
  else
    Serial.println(F("Successfully DHCP"));
  memcpy(ether.hisip, websiteip, sizeof(websiteip));   
  ether.printIp("SRV: ", ether.hisip);
  lcd.clear();
  lcd.print("Welcome!");
  // Выбираем RFID модуль, для работы по SPI 
  select_rfid();
  // Инициализируем RFID модуль
  mfrc522.PCD_Init();
}

void loop () {
  // Смотрим есть ли новые поднеснные карты
  if (mfrc522.PICC_IsNewCardPresent()){
    // Выбираем одну из карт
    if (mfrc522.PICC_ReadCardSerial()){
      // посылаем данные на сервер
      get_rfid_id(mfrc522.uid.uidByte);
      send_package();
    }
  }
}
