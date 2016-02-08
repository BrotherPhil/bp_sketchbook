/*
 *
 * System3x5
 *
 *
 * File Name           : System3x5.h
 * Date                : 14 Jan 2014
 * Font size in bytes  : 470
 * Font width          : 3
 * Font height         : 5
 * Font first char     : 32
 * Font last char      : 127
 * Font used chars     : 94
 *
 * The font data are defined as
 *
 * struct _FONT_ {
 *     uint16_t   font_Size_in_Bytes_over_all_included_Size_it_self;
 *     uint8_t    font_Width_in_Pixel_for_fixed_drawing;
 *     uint8_t    font_Height_in_Pixel_for_all_characters;
 *     unit8_t    font_First_Char;
 *     uint8_t    font_Char_Count;
 *
 *     uint8_t    font_Char_Widths[font_Last_Char - font_First_Char +1];
 *                  // for each character the separate width in pixels,
 *                  // characters < 128 have an implicit virtual right empty row
 *
 *     uint8_t    font_data[];
 *                  // bit field of all characters
 */

#include <inttypes.h>
#include <avr/pgmspace.h>

#ifndef SYSTEM3x5_H
#define SYSTEM3x5_H

#define SYSTEM3x5_WIDTH 3
#define SYSTEM3x5_HEIGHT 3

/*
 * added to allow fontname to match header file name. 
 * as well as keep the old name for backward compability
 */

#define SystemFont3x5 System3x5

static uint8_t System3x5[] PROGMEM = {
    0x0, 0x0, // size of zero indicates fixed width font, actual length is width * height
    0x03, // width
    0x05, // height
    0x20, // first char
    0x60, // char count
    
    // Fixed width; char width table not used !!!!
    
    // font data
    0x00, 0x00, 0x00,// (space)
