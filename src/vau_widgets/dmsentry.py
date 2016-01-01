#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2016 January. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : Date & Time Entry Components for tKinter & TTK
    Script Name  : dmsentry.py
    License      : GNU General Public License v3.0


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
from tkinter import *
from tkinter.ttk import *


class DMSEntry(Frame):
    def __init__(self, parent, text_label):
        super(DMSEntry, self).__init__(parent)

        self.deg_var = IntVar()
        self.min_var = IntVar()
        self.sec_var = IntVar()
        self.nano_var = IntVar()

        self.deg_var.set(1)
        self.min_var.set(59)
        self.sec_var.set(59)
        self.nano_var.set(0)

        self.hints = True
        self.ld = Label(self, text=" Arc. Degrees ")
        self.ld.grid(row=0, column=1)
        self.lm = Label(self, text="| Arc. Minutes |")
        self.lm.grid(row=0, column=2)
        self.ls = Label(self, text=" Arc. Seconds ")
        self.ls.grid(row=0, column=3)
        self.lp = Label(self, text=" Arc. Seconds's Fractions ")
        self.lp.grid(row=0, column=4)

        self.lmain = Label(self, text=text_label)
        self.lmain.grid(row=1, column=0, padx=(5, 5), pady=(5, 5))

        # Entry widget for entering Arc Degree portion of Angular measurement
        self.ed = Spinbox(self, width=5, from_=0, to=359, increment=10, wrap=True,
                          textvariable=self.deg_var, state='readonly',
                          justify=RIGHT)
        self.ed.grid(row=1, column=1)

        # Entry widget for entering Minutes portion of Angular measurement
        self.em = Spinbox(self, width=5, from_=0, to=59, increment=1, wrap=True,
                          textvariable=self.min_var, state='readonly',
                          justify=RIGHT)
        self.em.grid(row=1, column=2)

        # Entry widget for entering Seconds portion of Angular measurement
        self.es = Spinbox(self, width=5, from_=0, to=59, increment=1,
                          wrap=True, textvariable=self.sec_var, state='readonly',
                          justify=RIGHT)
        self.es.grid(row=1, column=3)

        # Entry widget for entering fractions of Seconds portion of Angular measurement
        self.ef = Spinbox(self, width=7, from_=0, to=99999, increment=1,
                          wrap=True, textvariable=self.nano_var, state='readonly',
                          justify=RIGHT)
        self.ef.grid(row=1, column=4)

    @property
    def get(self):
        return self.deg_var.get() + \
               (self.min_var.get() / 60) + \
               (self.sec_var.get() / 3600) + \
               (self.nano_var.get() / 360000000)

    @property
    def get_as_dms(self):
        return self.deg_var.get(), self.min_var.get(), \
               self.sec_var.get(), self.nano_var.get()

    def set_using_float(self, value_as_float):
        if isinstance(value_as_float, float):

            if value_as_float < 0:
                value_as_float = value_as_float * -1

            x = int(value_as_float)
            y = int((value_as_float - x) * 60)
            z = int((value_as_float - (x + (y / 60))) * 3600)
            f = int((value_as_float - (x + (y / 60) + (z / 3600))) * 100000)
            self.deg_var.set(x)
            self.min_var.set(y)
            self.sec_var.set(z)
            self.nano_var.set(f)
        else:
            raise ValueError("Expected Float, found {}".format(value_as_float))
        return None

    def set_using_dms(self, degree_value, minute_value,
                      seconds_value, fraction_value):
        if isinstance(degree_value, int) and isinstance(minute_value, int) and \
                isinstance(seconds_value, int) and isinstance(fraction_value, int):

            if degree_value < 0:
                degree_value = degree_value * -1

            if minute_value < 0:
                minute_value = minute_value * -1

            if seconds_value < 0:
                seconds_value = seconds_value * -1

            if fraction_value < 0:
                fraction_value = fraction_value * -1

            self.deg_var.set(degree_value)
            self.min_var.set(minute_value)
            self.sec_var.set(seconds_value)
            self.nano_var.set(fraction_value)
        else:
            raise ValueError("Expected Int, Int and Float, found {},{}and{} "
                             .format(degree_value, minute_value,
                                     seconds_value, fraction_value))
        return None

    def set(self, value):
        if isinstance(value, float):
            self.set_using_float(value)
        elif isinstance(value, tuple):
            if len(value) == 4:
                self.set_using_dms(value[0], value[1], value[2], value[3])
            elif len(value) == 3:
                self.set_using_dms(value[0], value[1], value[2], 0)
            else:
                raise ValueError("Tuple must have 3 or 4 elements, "
                                 "this one has {}".format(len(value)))
        elif isinstance(value, dict) and (len(value) == 4 or
                                          len(value) == 3):
            if "deg" in value and "min" in value and \
                    "sec" in value and "frac" in value:
                self.set_using_dms(value["deg"], value["min"],
                                   value["sec"], value["frac"])
            elif "deg" in value and "min" in value and "sec" in value:
                self.set_using_dms(value["deg"], value["min"],
                                   value["sec"], 0)
            else:
                raise ValueError("Invalid Dictionary, found {}".format(value))
        else:
            raise ValueError("Expected Float, found {}".format(value))
        return None

    def hide_hints(self):
        if self.hints:
            self.ld.grid(row=0, column=1)
            self.lm.grid(row=0, column=2)
            self.ls.grid(row=0, column=3)
            self.lp.grid(row=0, column=4)
            self.hints = False
        else:
            print("Hints are already hidden!")
        return None

    def show_hints(self):
        if self.hints:
            print("Hints are already visible!")
        else:
            self.ld.grid_forget()
            self.lm.grid_forget()
            self.ls.grid_forget()
            self.lp.grid_forget()
            self.hints = False
        return None

    def toggle_hints(self):
        if self.hints:
            self.hide_hints()
        else:
            self.show_hints()
        return self.hints


def main():
    root = Tk()
    e = DMSEntry(root, "Enter Degrees Minutes, Seconds : ")
    e.grid(padx=50, pady=50)
    e.set({"deg": 10, "min": 30, "sec": 59, "frac": 999})
    b = Button(root, text="Toggle Hints")
    b.grid(padx=50, pady=50)
    root.mainloop()
    print(e.get_as_dms)


if __name__ == '__main__':
    main()
