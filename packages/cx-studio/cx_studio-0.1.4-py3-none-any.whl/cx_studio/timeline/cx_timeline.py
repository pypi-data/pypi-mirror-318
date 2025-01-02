from .cx_track import Track
from ..core import DataPackage, Time, TimeRangeSupport


class Timeline(TimeRangeSupport):
    def __init__(self) -> None:
        super().__init__()
        # 默认包含一个空的 Track
        self._tracks: list[Track] = [Track()]
        self._data = DataPackage()

    @property
    def data(self):
        return self._data

    @property
    def tracks(self):
        return self._tracks

    @property
    def start(self):
        return Time(0)

    @property
    def duration(self):
        if not self._tracks:
            return Time(0)
        return max(t.duration for t in self._tracks)

    def __len__(self):
        return len(self._tracks)

    def __getitem__(self, index):
        return self._tracks[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Track):
            raise TypeError("Value must be a Track instance")
        self._tracks[index] = value

    def __delitem__(self, index):
        del self._tracks[index]

    def append(self, track):
        if not isinstance(track, Track):
            raise TypeError("Value must be a Track instance")
        self._tracks.append(track)

    def insert(self, index, track):
        if not isinstance(track, Track):
            raise TypeError("Value must be a Track instance")
        self._tracks.insert(index, track)

    def auto_insert_item(self, item: TimeRangeSupport):
        for track in self._tracks:
            if track.available_for(item):
                track.auto_insert(item)
                return
        new_track = Track()
        new_track.append(item)
        self.append(new_track)

    def item_count(self) -> int:
        if not self._tracks:
            return 0
        return sum(len(track) for track in self._tracks)

    def iter_items(self):
        for track in self._tracks:
            yield from track.iter_items()
