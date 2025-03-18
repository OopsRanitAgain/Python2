class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __repr__(self):
        return f'Time (hour={self.hour}, minute={self.minute}, second={self.second})'
    
    def __str__(self):
        return ('12' if self.hour in (0,12) else str(self.hour%12)) + f':{self.minute:0>2}:{self.second:0>2}'+ (' AM' if self.hour < 12 else ' PM')
    
    @property
    def hour(self):
        return self._hour
    
    @hour.setter
    def hour(self,hour):
        if not 0 <= hour < 24:
            raise ValueError('Hour must be Between 0 and 23')
        self._hour = hour

    @property
    def minute(self):
        return self._minute
    
    @minute.setter
    def minute(self,minute):
        if not 0<= minute < 60:
            raise ValueError('Minute must be between 0 and 59')
        self._minute = minute
    
    @property
    def second(self):
        return self._second
    
    @second.setter
    def second(self,second):
        if not 0<= second < 60:
            raise ValueError('Second Must be between 0 and 59')
        self._second = second

    def set_time(self,hour = 0,minute = 0,second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second