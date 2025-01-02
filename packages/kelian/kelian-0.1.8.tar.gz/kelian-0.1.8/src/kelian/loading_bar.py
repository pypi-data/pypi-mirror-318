from types import NoneType
from average_time import AverageTime
from typing import Any

class ProgressBar():
    def __init__(self, total_or_data:int|Any, current:int=0, length:int=50, enabled_average_time:bool=True, hide_average_time_when_is_over:bool=True, enabled_display_in_iterator:bool=True) -> None:
        if isinstance(total_or_data, int):
            self.total:int = total_or_data
            self.data_iterator:Any = None
        else:
            self.total:int = len(total_or_data)+1
            self.data_iterator:Any = iter(total_or_data)
        self.current:int = current
        self.length:int = length
        self.pattern:tuple[str, str, str, str, bool, str, bool] = ("[", "=", ".", "]", True, " | ", True)
        self.enabled_average_time = enabled_average_time
        if enabled_average_time:
            self.average_time = AverageTime()
        self.hide_average_time_when_is_over:bool = hide_average_time_when_is_over
        self.enabled_display_in_iterator:bool = enabled_display_in_iterator

    def __iter__(self):
        return self

    def __next__(self):
        try:
            print(self.__str__(), end="\r")
            return next(self.data_iterator)
        except StopIteration:
            raise StopIteration

    def format(self, start_side:str=None, full:str=None, empty:str=None, end_side:str=None, percent:bool=None, separator:str=None, average_time:bool=None) -> None:
        assert isinstance(start_side, (str, NoneType)), "'start_side' is not of type string"
        assert isinstance(full, (str, NoneType)), "'full' is not of type string"
        assert isinstance(empty, (str, NoneType)), "'empty' is not of type string"
        assert isinstance(end_side, (str, NoneType)), "'end_side' is not of type string"
        assert isinstance(percent, (bool, NoneType)), "'percent' is not of type boolean"
        assert isinstance(separator, (str, NoneType)), "'separator' is not of type string"
        assert isinstance(average_time, (bool, NoneType)), "'average_time' is not of type boolean"

        self.pattern = (
            start_side if start_side is not None else self.pattern[0], 
            full if full is not None else self.pattern[1], 
            empty if empty is not None else self.pattern[2], 
            end_side if end_side is not None else self.pattern[3], 
            percent if percent is not None else self.pattern[4], 
            separator if separator is not None else self.pattern[5], 
            average_time if average_time is not None else self.pattern[6]
        )

    def update(self) -> None:
        self.current += 1
        if self.enabled_average_time:
            self.average_time.loop(self.average_time.DEFAULT_ID)

    def display(self, update:bool=False) -> str:
        if update:
            self.update()

        full_bar_value = (self.length*self.current) // self.total

        result = "\x1b[2K" # clear the current line
        result += self.pattern[0]
        result += self.pattern[1] * full_bar_value
        result += self.pattern[2] * (self.length - full_bar_value)
        result += self.pattern[3]

        if self.pattern[4]: # if percent
            percent_value = round((100*self.current)/self.total, 1)
            result += " " + " "*(5-len(str(percent_value))) + str(percent_value) + "%"

        if self.enabled_average_time and self.pattern[6]: # if average_time
            if self.current == self.total:
                if not self.hide_average_time_when_is_over:
                    result += self.pattern[5]
                    result += "0:00:00.0"
            else:
                result += self.pattern[5]
                avg = self.average_time.get_average(self.average_time.DEFAULT_ID)
                result += "" if str(avg).startswith("E: ") else str((self.total - self.current)*avg)

        return result

    def __str__(self) -> str:
        return self.display(True)

    def __repr__(self) -> str:
        return self.__str__()
