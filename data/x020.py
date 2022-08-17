data = (
" ",    # 0x00
" ",    # 0x01
" ",    # 0x02
" ",    # 0x03
" ",    # 0x04
" ",    # 0x05
" ",    # 0x06
" ",    # 0x07
" ",    # 0x08
" ",    # 0x09
" ",    # 0x0a
" ",    # 0x0b
"",    # 0x0c
"",    # 0x0d
"",    # 0x0e
"",    # 0x0f
"-",    # 0x10
"-",    # 0x11
"-",    # 0x12
"-",    # 0x13
"--",    # 0x14
"--",    # 0x15
"||",    # 0x16
"_",    # 0x17
"'",    # 0x18
"'",    # 0x19
",",    # 0x1a
"'",    # 0x1b
"\"",    # 0x1c
"\"",    # 0x1d
",,",    # 0x1e
"\"",    # 0x1f
"+",    # 0x20
"++",    # 0x21
"*",    # 0x22
"*>",    # 0x23
".",    # 0x24
"..",    # 0x25
"...",    # 0x26
".",    # 0x27
"\x0a",    # 0x28
"\x0a\x0a",    # 0x29
"",    # 0x2a
"",    # 0x2b
"",    # 0x2c
"",    # 0x2d
"",    # 0x2e
" ",    # 0x2f
"%0",    # 0x30
"%00",    # 0x31
"'",    # 0x32
"\""",    # 0x33
"\"\"'",    # 0x34
"`",    # 0x35
"``",    # 0x36
"```",    # 0x37
"^",    # 0x38
"<",    # 0x39
">",    # 0x3a
"*",    # 0x3b
"!!",    # 0x3c
"!?",    # 0x3d
"-",    # 0x3e
"_",    # 0x3f
"-",    # 0x40
"^",    # 0x41
"***",    # 0x42
"--",    # 0x43
"/",    # 0x44
"-[",    # 0x45
"]-",    # 0x46
"??",    # 0x47
"?!",    # 0x48
"!?",    # 0x49

# Tironian note standing for Latin "et". Still used as an ampersand
# in modern Irish. See https://github.com/avian2/unidecode/issues/57
"&",    # 0x4a

"PP",    # 0x4b
"(]",    # 0x4c
"[)",    # 0x4d
"*",    # 0x4e
nothing,    # 0x4f
nothing,    # 0x50
nothing,    # 0x51
"%",    # 0x52
"~",    # 0x53
nothing,    # 0x54
nothing,    # 0x55
nothing,    # 0x56
"""""",    # 0x57
nothing,    # 0x58
nothing,    # 0x59
nothing,    # 0x5a
nothing,    # 0x5b
nothing,    # 0x5c
nothing,    # 0x5d
nothing,    # 0x5e
" ",    # 0x5f
"",    # 0x60
nothing,    # 0x61
nothing,    # 0x62
nothing,    # 0x63
nothing,    # 0x64
nothing,    # 0x65
nothing,    # 0x66
nothing,    # 0x67
nothing,    # 0x68
nothing,    # 0x69
"",    # 0x6a
"",    # 0x6b
"",    # 0x6c
"",    # 0x6d
"",    # 0x6e
"",    # 0x6f
"0",    # 0x70
"i",    # 0x71
"",    # 0x72
"",    # 0x73
"4",    # 0x74
"5",    # 0x75
"6",    # 0x76
"7",    # 0x77
"8",    # 0x78
"9",    # 0x79
"+",    # 0x7a
"-",    # 0x7b
"=",    # 0x7c
"(",    # 0x7d
")",    # 0x7e
"n",    # 0x7f
"0",    # 0x80
"1",    # 0x81
"2",    # 0x82
"3",    # 0x83
"4",    # 0x84
"5",    # 0x85
"6",    # 0x86
"7",    # 0x87
"8",    # 0x88
"9",    # 0x89
"+",    # 0x8a
"-",    # 0x8b
"=",    # 0x8c
"(",    # 0x8d
")",    # 0x8e
nothing,    # 0x8f
"a",    # 0x90
"e",    # 0x91
"o",    # 0x92
"x",    # 0x93
nothing,    # 0x94
"h",    # 0x95
"k",    # 0x96
"l",    # 0x97
"m",    # 0x98
"n",    # 0x99
"p",    # 0x9a
"s",    # 0x9b
"t",    # 0x9c
nothing,    # 0x9d
nothing,    # 0x9e
nothing,    # 0x9f
"ECU",    # 0xa0
"CL",    # 0xa1
"Cr",    # 0xa2
"FF",    # 0xa3
"L",    # 0xa4
"mil",    # 0xa5
"N",    # 0xa6
"Pts",    # 0xa7
"Rs",    # 0xa8
"W",    # 0xa9
"NS",    # 0xaa
"D",    # 0xab
"EUR",    # 0xac
"K",    # 0xad
"T",    # 0xae
"Dr",    # 0xaf
"Pf",    # 0xb0
"P",    # 0xb1
"G",    # 0xb2
"A",    # 0xb3
"UAH",    # 0xb4
"C|",    # 0xb5
"L",    # 0xb6
"Sm",    # 0xb7
"T",    # 0xb8
"Rs",    # 0xb9
"L",    # 0xba
"M",    # 0xbb
"m",    # 0xbc
"R",    # 0xbd
"l",    # 0xbe
"BTC",    # 0xbf
nothing,    # 0xc0
nothing,    # 0xc1
nothing,    # 0xc2
nothing,    # 0xc3
nothing,    # 0xc4
nothing,    # 0xc5
nothing,    # 0xc6
nothing,    # 0xc7
nothing,    # 0xc8
nothing,    # 0xc9
nothing,    # 0xca
nothing,    # 0xcb
nothing,    # 0xcc
nothing,    # 0xcd
nothing,    # 0xce
nothing,    # 0xcf
"",    # 0xd0
"",    # 0xd1
"",    # 0xd2
"",    # 0xd3
"",    # 0xd4
"",    # 0xd5
"",    # 0xd6
"",    # 0xd7
"",    # 0xd8
"",    # 0xd9
"",    # 0xda
"",    # 0xdb
"",    # 0xdc
"",    # 0xdd
"",    # 0xde
"",    # 0xdf
"",    # 0xe0
"",    # 0xe1
"",    # 0xe2
"",    # 0xe3
nothing,    # 0xe4
"",    # 0xe5
nothing,    # 0xe6
nothing,    # 0xe7
nothing,    # 0xe8
nothing,    # 0xe9
nothing,    # 0xea
nothing,    # 0xeb
nothing,    # 0xec
nothing,    # 0xed
nothing,    # 0xee
nothing,    # 0xef
nothing,    # 0xf0
nothing,    # 0xf1
nothing,    # 0xf2
nothing,    # 0xf3
nothing,    # 0xf4
nothing,    # 0xf5
nothing,    # 0xf6
nothing,    # 0xf7
nothing,    # 0xf8
nothing,    # 0xf9
nothing,    # 0xfa
nothing,    # 0xfb
nothing,    # 0xfc
nothing,    # 0xfd
nothing,    # 0xfe
)

