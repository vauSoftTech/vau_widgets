#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2016 January. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : Date & Time Entry Components for tKinter & TTK
    Script Name  : latlonentry.py
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


class LatLonEntry(Frame):

    def __init__(self, parent, lat_label, lon_label):
        super(LatLonEntry, self).__init__(parent)

        # if lat_is_N is True, given latitudes are Northern latitudes or else
        # they are Southern latitudes
        self.lat_is_N = BooleanVar()
        self.lat_deg_var = IntVar()
        self.lat_min_var = IntVar()
        self.lat_sec_var = IntVar()
        self.lat_fra_var = IntVar()

        # if lon_is_E is True, given latitudes are Eastern latitudes or else
        # they are Western latitudes
        self.lon_is_E = BooleanVar()
        self.lon_deg_var = IntVar()
        self.lon_min_var = IntVar()
        self.lon_sec_var = IntVar()
        self.lon_fra_var = IntVar()

        # By default assign Ahmedabad's Lat & lon
        self.lat_is_N.set(True)
        self.lat_deg_var.set(23)
        self.lat_min_var.set(3)
        self.lat_sec_var.set(0)
        self.lat_fra_var.set(0)
        self.lon_is_E.set(True)
        self.lon_deg_var.set(72)
        self.lon_min_var.set(58)
        self.lon_sec_var.set(0)
        self.lon_fra_var.set(0)

        self.deg_hint = Label(self, text=" Degrees ")
        self.deg_hint.grid(row=0, column=1)
        self.min_hint = Label(self, text=" Minutes ")
        self.min_hint.grid(row=0, column=2)
        self.sec_hint = Label(self, text=" Seconds ")
        self.sec_hint.grid(row=0, column=3)
        self.fra_hint = Label(self, text=" Fractions ")
        self.fra_hint.grid(row=0, column=4)
        self.hints = True

        self.lat_label = Label(self, text=lat_label)
        self.lat_label.grid(row=1, column=0, sticky=E)

        self.lon_label = Label(self, text=lon_label)
        self.lon_label.grid(row=2, column=0, sticky=E)

        # Latitude Entry Classes
        self.lat_deg_e = Spinbox(self, from_=0, to=180, state="readonly",
                                 textvar=self.lat_deg_var, justify=RIGHT,
                                 width=5)
        self.lat_deg_e.grid(row=1, column=1)

        self.lat_min_e = Spinbox(self, from_=0, to=59, state="readonly",
                                 textvar=self.lat_min_var, justify=RIGHT,
                                 width=5)
        self.lat_min_e.grid(row=1, column=2)

        self.lat_sec_e = Spinbox(self, from_=0, to=59, state="readonly",
                                 textvar=self.lat_sec_var, justify=RIGHT,
                                 width=5)
        self.lat_sec_e.grid(row=1, column=3)

        self.lat_fra_e = Spinbox(self, from_=0, to=59, state="readonly",
                                 textvar=self.lat_fra_var, justify=RIGHT,
                                 width=5)
        self.lat_fra_e.grid(row=1, column=4)

        # North or South Hemisphere selection Radiobuttons
        self.lat_rb_n = Radiobutton(self, text='North', variable=self.lat_is_N,
                                    value=True, command=self.rb_ns_command)
        self.lat_rb_n.grid(row=1, column=5, sticky=W)

        self.lat_rb_s = Radiobutton(self, text='South', variable=self.lat_is_N,
                                    value=False, command=self.rb_ns_command)
        self.lat_rb_s.grid(row=1, column=6, sticky=W)

        # Longitude Entry Classes
        self.lon_deg_e = Spinbox(self, from_=0, to=180, state="readonly",
                                 textvar=self.lon_deg_var, justify=RIGHT,
                                 width=5)
        self.lon_deg_e.grid(row=2, column=1)

        self.lon_min_e = Spinbox(self, from_=0, to=59, state="readonly",
                                 textvar=self.lon_min_var, justify=RIGHT,
                                 width=5)
        self.lon_min_e.grid(row=2, column=2)

        self.lon_sec_e = Spinbox(self, from_=0, to=59, state="readonly",
                                 textvar=self.lon_sec_var, justify=RIGHT,
                                 width=5)
        self.lon_sec_e.grid(row=2, column=3)

        self.lon_fra_e = Spinbox(self, from_=0, to=59, state="readonly",
                                 textvar=self.lon_fra_var, justify=RIGHT,
                                 width=5)
        self.lon_fra_e.grid(row=2, column=4)

        # East or West Direction selection Radiobuttons
        self.lon_rb_n = Radiobutton(self, text='East', variable=self.lon_is_E,
                                    value=True, command=self.rb_ew_command)
        self.lon_rb_n.grid(row=2, column=5, sticky=W)

        self.lon_rb_s = Radiobutton(self, text='West', variable=self.lon_is_E,
                                    value=False, command=self.rb_ew_command)
        self.lon_rb_s.grid(row=2, column=6, sticky=W)

        return

    def rb_ns_command(self):
        if self.lat_is_N.get():
            print("Northern hemisphere selected.")
        else:
            print("Southern hemisphere selected.")
        self.bell()
        return

    def rb_ew_command(self):
        if self.lon_is_E.get():
            print("Eastern Direction selected.")
        else:
            print("Western Direction selected.")
        self.bell()
        return

    def show_hints(self):
        if self.hints:
            print("Hints are already visible!")
        else:
            self.deg_hint.grid(row=0, column=1)
            self.min_hint.grid(row=0, column=2)
            self.sec_hint.grid(row=0, column=3)
            self.fra_hint.grid(row=0, column=4)
            self.hints = True
        return

    def hide_hints(self):
        if self.hints:
            self.deg_hint.grid_forget()
            self.min_hint.grid_forget()
            self.sec_hint.grid_forget()
            self.fra_hint.grid_forget()
            self.hints = False
        else:
            print("Hints are already hidden!")
        return

    def toggle_hints(self):
        if self.hints:
            self.hide_hints()
        else:
            self.show_hints()
        return

    @property
    def get_latitude_tuple(self):
        h = "N" if self.lat_is_N.get() else "S"
        return (h, self.lat_deg_var.get(),
                self.lat_min_var.get(), self.lat_sec_var.get(),
                self.lat_fra_var.get())

    @property
    def get_longitude_tuple(self):
        d = "E" if self.lon_is_E.get() else "W"
        return (d, self.lon_deg_var.get(),
                self.lon_min_var.get(), self.lon_sec_var.get(),
                self.lon_fra_var.get())

    @property
    def get_latitude_dict(self):
        h = "N" if self.lat_is_N.get() else "S"
        return dict(hemisphere=h, deg=self.lat_deg_var.get(),
                    min=self.lat_min_var.get(), sec=self.lat_sec_var.get(),
                    fra=self.lat_fra_var.get())

    @property
    def get_longitude_dict(self):
        d = "E" if self.lat_is_N.get() else "W"
        return dict(direction=d, deg=self.lat_deg_var.get(),
                    min=self.lat_min_var.get(), sec=self.lat_sec_var.get(),
                    fra=self.lat_fra_var.get())

    @property
    def get_latitude_decimal(self):
        a = 1 if self.lat_is_N.get() else -1
        b = self.lat_deg_var.get()
        c = self.lat_min_var.get()
        d = self.lat_sec_var.get()
        e = self.lat_fra_var.get()
        print(a, b, c, d, e)
        result = (b + (c / 60.0) + (d / 3600.0) + (e / (3600 * 100000))) * a
        return result

    @property
    def get_longitude_decimal(self):
        a = 1 if self.lon_is_E.get() else -1
        b = self.lon_deg_var.get()
        c = self.lon_min_var.get()
        d = self.lon_sec_var.get()
        e = self.lon_fra_var.get()
        result = (b + (c / 60.0) + (d / 3600.0) + (e / (3600 * 100000))) * a
        return result

    @property
    def get_latitude_str(self):
        a = "N" if self.lat_is_N.get() else "S"
        b = self.lat_deg_var.get()
        c = self.lat_min_var.get()
        d = self.lat_sec_var.get()
        e = self.lat_fra_var.get()
        result = "{}:{:02d}:{:02d}.{} {}".format(b, c, d, e, a)
        return result

    @property
    def get_longitude_str(self):
        a = "E" if self.lon_is_E.get() else "W"
        b = self.lon_deg_var.get()
        c = self.lon_min_var.get()
        d = self.lon_sec_var.get()
        e = self.lon_fra_var.get()
        result = "{}:{:02d}:{:02d}.{} {}".format(b, c, d, e, a)
        return result

    @property
    def get(self):
        return self.get_latitude_tuple, self.get_longitude_tuple

    @property
    def get_as_decimal_tuple(self):
        return self.get_latitude_decimal, self.get_longitude_decimal

    @property
    def get_as_dict_tuple(self):
        return dict(lat=self.get_latitude_dict, lon=self.get_longitude_dict)

    @property
    def get_as_str_tuple(self):
        return self.get_latitude_str, self.get_longitude_str

    def set_latitude_using_dict(self, dict_value):
        if isinstance(dict_value, dict):

            if "hemisphere" not in dict_value:
                raise ValueError("Hemisphere value not provided in {}".format(dict_value))

            if "deg" not in dict_value:
                raise ValueError("degree value not provided in {}".format(dict_value))

            if "min" not in dict_value:
                raise ValueError("minute value not provided in {}".format(dict_value))

            if "sec" in dict_value:
                x = dict_value["sec"]
            else:
                x = 0

            if "fra" in dict_value:
                y = dict_value["fra"]
            else:
                y = 0

            self.lat_is_N.set(True if dict_value['hemisphere'] else False)
            self.lat_deg_var.set(dict_value['deg'])
            self.lat_min_var.set(dict_value['min'])
            self.lat_sec_var.set(x)
            self.lat_fra_var.set(y)

        else:
            raise ValueError("Expected a dict, got {}".format(dict_value))
        return

    def set_longitude_using_dict(self, dict_value):
        if isinstance(dict_value, dict):
            if "hemisphere" not in dict_value:
                raise ValueError("Hemisphere value not provided in {}".format(dict_value))

            if "deg" not in dict_value:
                raise ValueError("degree value not provided in {}".format(dict_value))

            if "min" not in dict_value:
                raise ValueError("minute value not provided in {}".format(dict_value))

            if "sec" in dict_value:
                x = dict_value["sec"]
            else:
                x = 0

            if "fra" in dict_value:
                y = dict_value["fra"]
            else:
                y = 0

            self.lon_is_E.set(True if dict_value['direction'] else False)
            self.lon_deg_var.set(dict_value['deg'])
            self.lon_min_var.set(dict_value['min'])
            self.lon_sec_var.set(x)
            self.lon_fra_var.set(y)
        else:
            raise ValueError("Expected a dict, got {}".format(dict_value))
        return

    def set_latitude_using_decimal(self, decimal_value):
        if isinstance(decimal_value, float):
            self.lat_is_N.set(decimal_value >= 0)
            x = int(decimal_value)
            y = int((decimal_value - x) * 60)
            z = int((decimal_value - (x + (y / 60))) * 3600)
            self.lat_deg_var.set(x)
            self.lat_min_var.set(y)
            self.lat_sec_var.set(z)
        else:
            raise ValueError("Expected a decimal, got {}".format(decimal_value))
        return

    def set_longitude_using_decimal(self, decimal_value):
        if isinstance(decimal_value, float):
            self.lon_is_E.set(decimal_value >= 0)
            x = int(decimal_value)
            y = int((decimal_value - x) * 60)
            z = int((decimal_value - (x + (y / 60))) * 3600)
            self.lon_deg_var.set(x)
            self.lon_min_var.set(y)
            self.lon_sec_var.set(z)
        else:
            raise ValueError("Expected a decimal, got {}".format(decimal_value))
        return

    def set_using_decimal_tuple(self, decimal_tuple):
        if isinstance(decimal_tuple, tuple) and len(decimal_tuple) == 2:
            self.set_latitude_using_decimal(decimal_tuple[0])
            self.set_longitude_using_decimal(decimal_tuple[1])
        else:
            raise ValueError("Expected a decimal tuple, got {}".format(decimal_tuple))
        return


def main():
    root = Tk()
    e = LatLonEntry(root, " Latitude : ", " Longitude : ")
    e.grid(padx=50, pady=50)
    b = Button(root, text="Toggle Hints", command=e.toggle_hints)
    b.grid(padx=50, pady=50)
    e.set_using_decimal_tuple((23.05, 72.58))
    root.mainloop()
    print(e.get_latitude_str, ", ", e.get_longitude_str)


if __name__ == '__main__':
    main()
