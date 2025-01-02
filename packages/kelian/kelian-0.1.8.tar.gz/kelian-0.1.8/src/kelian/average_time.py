from datetime import datetime, timezone

class AverageTime:
    DEFAULT_ID = "default"

    def __init__(self) -> None:
        self.data:dict[str, dict[str, list[datetime]]] = {}

    def __add_time__(self, start_time:datetime=None, end_time:datetime=None, id_time:str=DEFAULT_ID) -> None:
        if id_time not in list(self.data.keys()):
            self.data[id_time] = { "st": [], "ed": [] }

        if start_time is not None:
            self.data[id_time]["st"].append(start_time)

        if end_time is not None:
            self.data[id_time]["ed"].append(end_time)

    def __get_average_by_id__(self, id_time:str) -> None | str:
        assert id_time in list(self.data.keys()), "ID not found"
        if len(self.data[id_time]["st"]) == 0:
            return "E: Start time not found for id: " + id_time
        if len(self.data[id_time]["ed"]) == 0:
            return "E: Not enough value recorded for id: " + id_time
        if len(self.data[id_time]["st"])-1 > len(self.data[id_time]["ed"]):
            return "E: Too many stopwatches started"
        average_list:list[float] = []
        for index in range(len(self.data[id_time]["ed"])):
            stts:float = self.data[id_time]["st"][index].timestamp()
            edts:float = self.data[id_time]["ed"][index].timestamp()
            average_list.append(edts - stts)
        average:float = sum(average_list) / len(average_list)
        average:datetime = datetime.fromtimestamp(average)
        average -= datetime(year=1970, month=1, day=1, hour=1)
        return average

    def start(self, id:str=DEFAULT_ID) -> None:
        self.__add_time__(start_time=datetime.now(timezone.utc), 
                          id_time=id)

    def loop(self, id:str=DEFAULT_ID) -> None:
        t = datetime.now(timezone.utc)
        if id not in list(self.data.keys()):
            self.__add_time__(start_time=t, id_time=id)
        else:
            self.__add_time__(start_time=t, end_time=t, id_time=id)

    def stop(self, id:str=DEFAULT_ID) -> None:
        self.__add_time__(end_time=datetime.now(timezone.utc), 
                          id_time=id)

    def get_average(self, id:str=None) -> datetime | dict[str, datetime] | str:
        if id is None and [self.DEFAULT_ID] == list(self.data.keys()):
            return self.__get_average_by_id__(self.DEFAULT_ID)
        elif id is None:
            d = {key_id:self.__get_average_by_id__(key_id) for key_id in list(self.data.keys())}
            if len(list(d.keys())) > 1:
                return d
            else:
                return list(d.values())[0]
        else:
            return self.__get_average_by_id__(id)

    def __str__(self) -> str:
        avg = self.get_average()
        if isinstance(avg, dict):
            max_key_length = max([len(k) for k in list(avg.keys())])
            timelist = [k+(" "*(max_key_length-len(k)))+": "+str(v) for k, v in avg.items()]
            return "\n".join(timelist)
        else:
            return str(avg)

    def __repr__(self) -> str:
        return self.__str__()
