range_limits = {
    "wvht": [0.1, 19.9],
    "wmax": [0.1, 19.9],
    "dpd": [1.7, 30],
    "mwd": [0, 360],
    "wspd": [0.1, 59],
    "wdir": [0, 360],
    "gust": [0.1, 59],
    "atmp": [-39, 59],
    "pres": [501, 1099],
    "dewp": [-29, 39],
    "wtmp": [-3, 39],
    "humi": [25, 102],
    "cvel": [-4990, 4990],
    "cdir": [0, 360],
    "apd": [1.7, 30],
    }

sigma_limits = {
    "wvht": 6,
    "humi": 20,
    "pres": 21,
    "atmp": 11,
    "wspd": 25,
    "wtmp": 8.6,
    }

mis_value_limits = {
    "humi": [11, 12],
    "cvel": [409.5, 4095],
    "cdir": 511,
    "dewp": -10,
    "qtmp": -10,
    "wtmp": 40.95,
    }

climate_limits = {
    "wwht": [0, 15],
    "wmax": [0, 19],
    "dpd": [1.7, 20],
    "wspd": [0, 59],
    "gust": [0, 59],
    "atmp": [-8, 42],
    "atmp": [8, 48],
    "atmp": [15, 48],
    "pres": [950, 1050],
    "dewp": [-29, 39],
    "wtmp": [-3, 39],
    "apd": [1.7, 20],
    "cvel": [-2500, 2500],
    }

stuck_limits = 7
