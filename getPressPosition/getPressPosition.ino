Point getPressPosition()
{

   Point p, q;
   int upCount = 0;

   // Wait for screen press
   do
   {
      q = ts.getPoint();
      delay(10);
   } while( q.z < MINPRESSURE || q.z > MAXPRESSURE );

   // Save initial touch point
   p.x = q.x; p.y = q.y; p.z = q.z;

   // Wait for finger to come up
   do
   {
      q = ts.getPoint();
      if ( q.z < MINPRESSURE || q.z > MAXPRESSURE  )
      {
         upCount++;
      }
      else
      {
         upCount = 0;
         p.x = q.x; p.y = q.y; p.z = q.z;
      }

      delay(10);             // Try varying this delay

   } while( upCount < 10 );  // and this count for different results.

   p.x = map(p.x, tsMinX, tsMaxX, 0, 239);
   p.y = map(p.y, tsMinY, tsMaxY, 0, 319);

   // I've been focused on rotation 3, with the USB connector on the right-hand side
   // so, you'll have to add your own code here.
   switch( ROTATION )
   {
      case 3:
         swap(p.x, p.y);
         p.x = (320 - p.x);
         break;
   }

   // Clean up pin modes for LCD
   pinMode(XM, OUTPUT);
   digitalWrite(XM, LOW);
   pinMode(YP, OUTPUT);
   digitalWrite(YP, HIGH);
   pinMode(YM, OUTPUT);
   digitalWrite(YM, LOW);
   pinMode(XP, OUTPUT);
   digitalWrite(XP, HIGH);

   return p;
}

