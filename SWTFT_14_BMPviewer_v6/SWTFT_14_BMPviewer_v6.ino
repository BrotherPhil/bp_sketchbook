#define LCD_CS A3    
#define LCD_CD A2    
#define LCD_WR A1   
#define LCD_RD A0    
#define LCD_RESET A4
#define SD_CS 10 // Card select for shield use

#include <Adafruit_GFX.h>    // Core graphics library
#include <SWTFT.h> // Hardware-specific library
#include <SD.h>


#define BUFFPIXEL 20

File root;
File bmpImage;

SWTFT tft;

void setup(void) {

  Serial.begin(115200);
  Serial.println("APC magazine LCD BMP image viewer");
  Serial.println("Modified for SWTFT by Phil Culmer");
 
  tft.reset();

  uint16_t identifier = tft.readID();

  
    Serial.print(F("Found LCD driver chip ID: "));
    Serial.println(identifier, HEX);
    
  tft.begin(identifier);

  Serial.print(F("Initializing SD card..."));
  if (!SD.begin(SD_CS)) {
    Serial.println(F("failed!"));
    return;
  }
  Serial.println(F("OK!"));


  root = SD.open("/");

}

void loop(void) {

    tft.fillScreen(0x0000); // fill screen with BLACK
    bmpDrawFromRoot();
    delay(5000);
}

void bmpDrawFromRoot() {
  File     bmpFile;
  int      bmpWidth, bmpHeight;   // W+H in pixels
  uint8_t  bmpDepth;              // Bit depth (currently must be 24)
  uint32_t bmpImageoffset;        // Start of image data in file
  uint32_t rowSize;               // Not always = bmpWidth; may have padding
  uint8_t  sdbuffer[3*BUFFPIXEL]; // pixel in buffer (R+G+B per pixel)
  uint16_t lcdbuffer[BUFFPIXEL];  // pixel out buffer (16-bit per pixel)
  uint8_t  buffidx = sizeof(sdbuffer); // Current position in sdbuffer
  boolean  goodBmp = false;       // Set to true on valid header parse
  boolean  flip    = true;        // BMP is stored bottom-to-top
  int      w, h, row, col, tW, tH;
  uint8_t  r, g, b;
  uint32_t pos = 0, startTime = millis();
  uint8_t  lcdidx = 0;
  boolean  first = true;
  String test;
  
  tW = tft.width(); tH = tft.height();
  
  bmpFile = root.openNextFile();
  test = bmpFile.name();
  if (! bmpFile ) { root.rewindDirectory(); return; } 
  if ( (! test.endsWith(".bmp")) and (! test.endsWith(".BMP"))) { Serial.print("."); return; }
  

  Serial.println();
  Serial.print("Loading image '");
  Serial.print(bmpFile.name());
  Serial.println('\'');

  // Parse BMP header
  if(read16(bmpFile) == 0x4D42) { // BMP signature
    Serial.print(F("File size: ")); Serial.println(read32(bmpFile));
    (void)read32(bmpFile); // Read & ignore creator bytes
    bmpImageoffset = read32(bmpFile); // Start of image data
    Serial.print(F("Image Offset: ")); Serial.println(bmpImageoffset, DEC);
    // Read DIB header
    Serial.print(F("Header size: ")); Serial.println(read32(bmpFile));
    bmpWidth  = read32(bmpFile);
    bmpHeight = read32(bmpFile);
    if(read16(bmpFile) == 1) { // # planes -- must be '1'
      bmpDepth = read16(bmpFile); // bits per pixel
      Serial.print(F("Bit Depth: ")); Serial.println(bmpDepth);
      if((bmpDepth == 24) && (read32(bmpFile) == 0)) { // 0 = uncompressed

        goodBmp = true; // Supported BMP format -- proceed!
        Serial.print(F("Image size: "));
        Serial.print(bmpWidth);
        Serial.print('x');
        Serial.println(bmpHeight);

        // BMP rows are padded (if needed) to 4-byte boundary
        rowSize = (bmpWidth * 3 + 3) & ~3;
        Serial.print(F("Row Size: ")); Serial.println(rowSize);

        // If bmpHeight is negative, image is in top-down order.
        // This is not canon but has been observed in the wild.
       if(bmpHeight < 0) {
          bmpHeight = -bmpHeight;
          flip      = false;
        }

        // Crop area to be loaded
        w = bmpWidth;
        h = bmpHeight;
        if((w-1) >= tft.width())  w = tft.width();
        if((h-1) >= tft.height()) h = tft.height();

        // Set TFT address window to clipped image bounds
        tft.setAddrWindow(0, 0, w-1, h-1);
        
        for (row=0; row<bmpHeight; row++) { // For each scanline...
            pos = bmpImageoffset + (row * rowSize);
            bmpFile.seek(pos);
            buffidx = sizeof(sdbuffer); // Force buffer reload
         

          for (col=0; col<bmpWidth; col++) { // For each column...
            if (buffidx >= sizeof(sdbuffer)) { // Indeed
              bmpFile.read(sdbuffer, sizeof(sdbuffer));
              buffidx = 0; // Set index to beginning
            }

            // Convert pixel from BMP to TFT format
            b = sdbuffer[buffidx++];
            g = sdbuffer[buffidx++];
            r = sdbuffer[buffidx++];
            lcdbuffer[lcdidx++] = tft.color565(r,g,b); 
          }// end pixel
        } // end scanline
        // Write any remaining data to LCD
        if(lcdidx > 0) {
          tft.pushColors(lcdbuffer, lcdidx, first);
        } 
    
        Serial.print(F("Loaded in ")); Serial.print(millis() - startTime); Serial.println(" ms");
      } // end goodBmp
    }
  }

  bmpFile.close();
  if(!goodBmp) Serial.println("BMP format not recognized.");
}

uint16_t read16(File f) {
  uint16_t result;
  ((uint8_t *)&result)[0] = f.read(); // LSB
  ((uint8_t *)&result)[1] = f.read(); // MSB
  return result;
}

uint32_t read32(File f) {
  uint32_t result;
  ((uint8_t *)&result)[0] = f.read(); // LSB
  ((uint8_t *)&result)[1] = f.read();
  ((uint8_t *)&result)[2] = f.read();
  ((uint8_t *)&result)[3] = f.read(); // MSB
  return result;
}
