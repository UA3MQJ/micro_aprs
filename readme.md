Записи о том, как сделать APRS KISS TNC Modem на базе китайской ардуино нано и проекта micromodem

https://unsigned.io/micromodem/

flash

```
avrdude -c usbasp -P usb -p m328p -U flash:w:microaprs-3v-kiss-latest.hex
```

board
https://aliexpress.ru/item/32832366092.html?spm=a2g0s.9042311.0.0.264d33ed59A3In&_ga=2.151585785.1129748883.1593168073-215828394.1578562924

programmer + adapter
https://aliexpress.ru/item/2055099231.html?spm=a2g0s.9042311.0.0.264d33edZYWpLo&_ga=2.76262357.1129748883.1593168073-215828394.1578562924

board pinout
https://sun9-49.userapi.com/c857332/v857332621/147316/EGOfI8KifQY.jpg
![board-pinout](https://github.com/UA3MQJ/micro_arps/blob/master/board-pinout.jpg?raw=true)

Micro modem schematic
https://unsigned.io/wp-content/uploads/2014/12/Schematic-1.pdf
![Micro-modem scheme](https://github.com/UA3MQJ/micro_arps/blob/master/scheme.png?raw=true)

Куда подключаться к плате с алиэкспресс

```
DAC
d4-d5-d6-d7
8k 4k 2k 1k

led tx pin13 - D9
led rx pin14 - D10

ADC
pin23 pc0 - A0
```

# see also

https://zftlab.org/pages/2015012200.html

https://eax.me/sdr-aprs/

http://goryham.qrz.ru/pr/aprs/dir300b1.htm


Arduino digi

extdigi, an APRS Digipeater for Arduino - http://extradio.sourceforge.net/extdigi.html

https://github.com/ZS6TVB/Arduino-APRS-Digipeater/tree/master/Software/APRS%20Digi

https://github.com/markqvist/MicroDigi



Arduino igate

http://hamradioprojects.com/authors/dl8rds/+airgate/



