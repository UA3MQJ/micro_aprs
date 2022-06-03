#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2014-2019 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.altera import AlteraPlatform
from litex.build.altera.programmer import USBBlaster

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk
    ("clk50", 0, Pins("23"), IOStandard("3.3-V LVTTL")),

    # Leds
    ("user_led", 0, Pins("86"), IOStandard("3.3-V LVTTL")),
    ("user_led", 1, Pins("85"), IOStandard("3.3-V LVTTL")),

    # Button
    ("key", 0, Pins("25"), IOStandard("3.3-V LVTTL")),
    ("key", 1, Pins("24"),  IOStandard("3.3-V LVTTL")),

    # Switches
    ("sw", 0, Pins("91"),  IOStandard("3.3-V LVTTL")),
    ("sw", 1, Pins("90"),  IOStandard("3.3-V LVTTL")),
    ("sw", 2, Pins("89"),  IOStandard("3.3-V LVTTL")),
    ("sw", 3, Pins("88"), IOStandard("3.3-V LVTTL")),

    # SDR SDRAM H57V2562GTR
    ("sdram_clock", 0, Pins("44"), IOStandard("3.3-V LVTTL")),
    ("sdram", 0,
        Subsignal("a",     Pins("33 34 38 39 58 59 60 64 65 66 32 67 68")),
        Subsignal("ba",    Pins("30 31")),
        Subsignal("cs_n",  Pins("28")),
        Subsignal("cke",   Pins("43")),
        Subsignal("ras_n", Pins("42")),
        Subsignal("cas_n", Pins("46")),
        Subsignal("we_n",  Pins("49")),
        Subsignal("dq", Pins("73 74 75 55 54 53 52 51 70 71 72 76 77 80 83 84")),
        Subsignal("dm", Pins("50 69")),
        IOStandard("3.3-V LVTTL")
    ),

    # Seven Segment
    ("seven_seg", 0, Pins("87 98 100 106 104 99 101 103"), IOStandard("3.3-V LVTTL")),

    # Serial
    ("serial", 0,
        Subsignal("tx", Pins("11"), IOStandard("3.3-V LVTTL")), # JP5 GPIO[0]
        Subsignal("rx", Pins("10"), IOStandard("3.3-V LVTTL"))  # JP5 GPIO[1]
    ),

    # GPIOs extension
    ("gpio_0", 0, Pins(
        "11 10 7 3 2 1 144 143 142 141 138 137 136 135 133 132 129 128 127 126",
        "125 124 121 120 119 115 114 113 112 111 106 110 104 105 101 103 99 100 87 98"
        ),
        IOStandard("3.3-V LVTTL")
    ),

    # SPIFlash w25q128fvsg
    # 1 - /CS                        VCC   - 8
    # 2 - DO (IO1)   /HOLD or /RESET (IO3) - 7
    # 3 - /WP (IO2)                  CLK   - 6
    # 4 - GND           DI (IO0)           - 5    
    ("spiflash", 0,
        Subsignal("cs_n", Pins("7"), IOStandard("3.3-V LVTTL")),
        Subsignal("clk",  Pins("3"), IOStandard("3.3-V LVTTL")),
        Subsignal("mosi", Pins("2"), IOStandard("3.3-V LVTTL")),
        Subsignal("miso", Pins("1"), IOStandard("3.3-V LVTTL")),
        Subsignal("wp",   Pins("144"), IOStandard("3.3-V LVTTL")),
        Subsignal("hold", Pins("143"), IOStandard("3.3-V LVTTL"))
    ),

]

# Platform -----------------------------------------------------------------------------------------

class Platform(AlteraPlatform):
    default_clk_name   = "clk50"
    default_clk_period = 1e9/50e6

    def __init__(self):
        AlteraPlatform.__init__(self, "EP4CE10E22C8", _io)

    def create_programmer(self):
        return USBBlaster()

    def do_finalize(self, fragment):
        AlteraPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk50", loose=True), 1e9/50e6)
