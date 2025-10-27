#include <ESP8266WiFi.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <ESP8266WebServer.h>
#include <SPI.h>
#include <SD.h>

// ====== Datos de tu red WiFi ======
const char* ssid = "Redmi9";
const char* password = "12345678";

// ====== Pines ======
#define ONE_WIRE_BUS 4      // D2 = GPIO4
#define ANEMO_PIN A0        // Entrada analógica para anemómetro
#define SD_CS_PIN 15        // D8 = GPIO15, CS de la microSD

// ====== Variables globales ======
float tempC = 0.0;
float velocidad = 0.0;
float riesgo = 0.0;

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
ESP8266WebServer server(80);
File archivo;

// ====== FUNCIONES DE MEMBRESÍA ======
float trapecio(float x, float a, float b, float c, float d) {
  return max(0.0f, min(min((x - a) / (b - a), 1.0f), (d - x) / (d - c)));
}

float triangulo(float x, float a, float b, float c) {
  return max(0.0f, min((x - a) / (b - a), (c - x) / (c - b)));
}

// Temperatura
float temperatura_normal(float x)    { return trapecio(x, 70, 80, 85, 90); }
float temperatura_alta(float x)      { return triangulo(x, 88, 93, 98); }
float temperatura_critica(float x)   { return trapecio(x, 95, 98, 100, 105); }

// Flujo
float flujo_bajo(float x)    { return trapecio(x, 0, 2, 4, 6); }
float flujo_regular(float x) { return triangulo(x, 5, 10, 15); }
float flujo_optimo(float x)  { return trapecio(x, 14, 18, 22, 26); }

// ====== INFERENCIA TAKAGI-SUGENO (9 reglas) ======
float inferencia_ts(float temp, float flujo) {
  // Grados de pertenencia de la temperatura
  float t_normal   = temperatura_normal(temp);
  float t_alta     = temperatura_alta(temp);
  float t_critica  = temperatura_critica(temp);

  // Grados de pertenencia del flujo
  float f_bajo     = flujo_bajo(flujo);
  float f_regular  = flujo_regular(flujo);
  float f_optimo   = flujo_optimo(flujo);

  // Variables acumuladoras
  float num = 0.0;
  float den = 0.0;

  // === Reglas Takagi-Sugeno (0=bajo, 0.5=medio, 1=alto) ===
  // Temperatura normal
  float r1 = min(t_normal, f_bajo);    num += r1 * 0.5;  den += r1;
  float r2 = min(t_normal, f_regular); num += r2 * 0.5;  den += r2;
  float r3 = min(t_normal, f_optimo);  num += r3 * 0.0;  den += r3;

  // Temperatura alta
  float r4 = min(t_alta, f_bajo);      num += r4 * 1.0;  den += r4;
  float r5 = min(t_alta, f_regular);   num += r5 * 0.5;  den += r5;
  float r6 = min(t_alta, f_optimo);    num += r6 * 0.0;  den += r6;

  // Temperatura crítica
  float r7 = min(t_critica, f_bajo);   num += r7 * 1.0;  den += r7;
  float r8 = min(t_critica, f_regular);num += r8 * 1.0;  den += r8;
  float r9 = min(t_critica, f_optimo); num += r9 * 0.5;  den += r9;

  // Salida final normalizada
  return (den != 0.0) ? num / den : 0.0;
}

// ====== SETUP ======
void setup() {
  Serial.begin(115200);
  sensors.begin();
  Serial.println("✅ Sensor de temperatura iniciado");

  // Inicializa SD
  if (!SD.begin(SD_CS_PIN)) {
    Serial.println("❌ No se pudo inicializar la tarjeta SD.");
  } else {
    Serial.println("✅ Tarjeta SD lista.");
  }

  // Conexión WiFi
  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n✅ WiFi conectado");
  Serial.print("📶 IP: ");
  Serial.println(WiFi.localIP());

  // Rutas del servidor
  server.on("/temperatura", HTTP_GET, []() {
    sensors.requestTemperatures();
    float tempC_local = sensors.getTempCByIndex(0);
    if (tempC_local == DEVICE_DISCONNECTED_C) {
      server.send(200, "text/plain", "Sensor no conectado");
    } else {
      server.send(200, "text/plain", String(tempC_local));
    }
  });

  server.on("/viento", HTTP_GET, []() {
    server.send(200, "text/plain", String(velocidad));
  });

  server.on("/riesgo", HTTP_GET, []() {
    server.send(200, "text/plain", String(riesgo));
  });

  server.begin();
  Serial.println("🟢 Servidor iniciado en /temperatura, /viento y /riesgo");
}

// ====== LOOP ======
void loop() {
  server.handleClient();

  static unsigned long lastPrint = 0;
  if (millis() - lastPrint > 5000) {
    // Lectura de temperatura
    sensors.requestTemperatures();
    tempC = sensors.getTempCByIndex(0);

    // Velocidad del viento (anemómetro)
    float voltaje = analogRead(ANEMO_PIN) * (3.3 / 1023.0);
    velocidad = voltaje * 2 * 14;  // Ajusta según tu calibración real

    // Riesgo calculado con lógica difusa
    riesgo = inferencia_ts(tempC, velocidad);

    // 📡 Salida por Serial
    Serial.print("T:"); Serial.print(tempC, 2);
    Serial.print("; V:"); Serial.print(velocidad, 2);
    Serial.print("; R:"); Serial.println(riesgo, 2);

    // Guardar en microSD si está lista
    if (SD.begin(SD_CS_PIN)) {
      String linea = String("ms:") + String(millis()) +
                     "; T:" + String(tempC, 2) +
                     "; V:" + String(velocidad, 2) +
                     "; R:" + String(riesgo, 2);
      archivo = SD.open("datos.txt", FILE_WRITE);
      if (archivo) {
        archivo.println(linea);
        archivo.close();
        Serial.println("📁 Guardado en SD: " + linea);
      }
    }

    lastPrint = millis();
  }
}
