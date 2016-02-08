// Writes 16-bit data in bulk, using callback to get more
void TFTLCD::bulkWrite(uint16_t *data, uint16_t bufferSize, uint16_t (*getNextValues)(void *), void *userData)
{
	*portOutputRegister(csport) &= ~cspin;
	*portOutputRegister(cdport) |= cdpin;
	*portOutputRegister(rdport) |= rdpin;
	*portOutputRegister(wrport) |= wrpin;

	setWriteDir();
	while( bufferSize )
	{
		for(uint16_t i=0; i < bufferSize; i++)
		{
			writeData_unsafe(data[i]);
		}
		bufferSize = getNextValues(userData);
	}
	*portOutputRegister(csport) |= cspin;
}
