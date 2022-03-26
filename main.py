import json
import sqlite3
import subprocess
import os
from datetime import datetime


# Zhijun Li
def open_json_file(filename):
    file = open(filename, "r+")
    x = file.read()
    file.close()
    return json.loads(x)


def process_data():
    y = open_json_file("ip.json")
    con = sqlite3.connect("weatherData.db")
    ip = y['query']
    lat = y['lat']
    long = y['lon']
    timezone = y['timezone']
    cur = con.cursor()
    cur.execute("INSERT INTO visit_information (remote_ip,visit_time,lat,lon,timezone) VALUES (?, ?, ?, ?, ?)", (ip, "hello", lat, long, timezone))
    vid = cur.execute("SELECT last_insert_rowid()").lastrowid
    con.commit()
    con.close()
    process_weather_data(vid)


def time_stamp_converter(timestamp, timezone_offset):
    timestamp -= timezone_offset
    ts = int(timestamp)
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def process_weather_data(vid):
    y = open_json_file("weatherData.json")
    timezone_offset = abs(y['timezone_offset'])
    con = sqlite3.connect('weatherData.db')
    dt = time_stamp_converter(y['current']['dt'], timezone_offset)
    sunrise = time_stamp_converter(y['current']['sunrise'], timezone_offset)
    sunset = time_stamp_converter(y['current']['sunset'], timezone_offset)
    temp = y['current']['temp']
    pressure = y['current']['pressure']
    humidity = y['current']['humidity']
    wind_speed = y['current']['wind_speed']
    wind_deg = y['current']['wind_deg']
    cur = con.cursor()
    cur.execute(
        "INSERT INTO weather_current ( vid, dt, sunrise, sunset, temp, pressure, humidity, wind_speed, wind_deg) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (vid, dt, sunrise, sunset, temp, pressure, humidity, wind_speed, wind_deg))

    for x in range(8):
        day = x + 1
        dt = time_stamp_converter(y['daily'][x]['dt'], timezone_offset)
        sunrise = time_stamp_converter(y['daily'][x]['sunrise'], timezone_offset)
        sunset = time_stamp_converter(y['daily'][x]['sunset'], timezone_offset)
        day_temp = y['daily'][x]['temp']['day']
        day_max = y['daily'][x]['temp']['max']
        day_min = y['daily'][x]['temp']['min']
        day_night = y['daily'][x]['temp']['night']
        humidity = y['daily'][x]['humidity']
        pressure = y['daily'][x]['pressure']
        wind_speed = y['daily'][x]['wind_speed']
        wind_deg = y['daily'][x]['wind_deg']
        cur.execute(
            "INSERT INTO weather_daily (vid, day, dt, sunrise, sunset, temp_day, temp_min, temp_max, temp_night, pressure, humidity, wind_speed, wind_deg) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (vid, day, dt, sunrise, sunset, day_temp, day_min, day_max, day_night, pressure, humidity, wind_speed, wind_deg))
    con.commit()
    con.close()


process_data()
