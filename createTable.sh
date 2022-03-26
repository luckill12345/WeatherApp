sqlite3 weatherData.db << EOF
CREATE TABLE "visit_information" (
    "vid" INTEGER,
    "remote_ip" TEXT, 
    "visit_time" TEXT,
    "lat" TEXT,
    "lon" TEXT, 
    "timezone" INTEGER,
    PRIMARY KEY("vid" AUTOINCREMENT));

CREATE TABLE "weather_current" (
    "cid" INTEGER,
    "vid" INTEGER,
    "dt"  NUMERIC,
    "sunrise" NUMERIC,
    "sunset" NUMERIC,
    "temp" REAL, 
    "pressure" INTEGER,
    "humidity" INTEGER,
    "wind_speed" REAL,
    "wind_deg" INTEGER,
    "weather_main" TEXT,
    "weather_description" TEXT,
    PRIMARY KEY("cid" AUTOINCREMENT));

CREATE TABLE "weather_daily" (
    "wid"   INTEGER,
    "vid"    INTEGER,
    "day"   INTEGER,
    "dt"    NUMERIC,
    "sunrise"    NUMERIC,
    "sunset"    NUMERIC,
    "temp_day"    REAL,
    "temp_min"    REAL,
    "temp_max"    REAL,
    "temp_night"    REAL,
    "pressure"    INTEGER,
    "humidity"    INTEGER,
    "wind_speed"    REAL,
    "wind_deg"    INTEGER,
    "weather_main"    TEXT,
    "weather_description"    TEXT,

    PRIMARY KEY("wid" AUTOINCREMENT));
EOF