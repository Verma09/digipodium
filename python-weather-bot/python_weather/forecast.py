from datetime import datetime, date, time, timedelta, timezone
from typing import Generator, Optional, Tuple

from .constants import VALID_FORMATS,  DATE_REGEX

from .errors import InvalidArg
from .enums import WeatherType, MoonPhase

def _convert_to_24h(hour, ampm):
    res = (0 if ampm == 'A' else 12) + int(hour)

    if res == 24:
        return 12
    
    elif res == 0 or res == 12:
         return 0
        
    else:
        return res
    
    class NearestArea:
            __slots__ = ('__inner',)

    def __init__(self, json: dict):
        self.__inner = json

    def __repr__(self) -> str:
        return f'<NearestArea name={self.name!r} country={self.country!r} region={self.region!r}>'
    
        
        