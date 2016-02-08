void displayBitmap(int x, int y)
{
  uint16_t bx, ex, by, ey;
  uint32_t time = millis();

  // Raw pixel data starts at position 8
  bmpFile.seek(8);

  // Save the current viewport settings and set
  tft.getViewport(&bx, &ex, &by, &ey);
  tft.setViewport(x, y, x + bmpWidth - 1, y + bmpHeight - 1);
  tft.goTo(x, y);

  // Bulk write data to LCD, loadBitmapData is a callback to refill buffer
  int bytesRead = loadBitmapData(NULL);
  tft.bulkWrite( (uint16_t *) picBuffer, bytesRead, loadBitmapData, NULL);

  // Leave the viewport like we found it
  tft.setViewport(bx, ex, by, ey);

  Serial.print("Total time: ");
  Serial.println(millis() - time, DEC);

}
