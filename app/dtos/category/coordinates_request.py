import dataclasses


@dataclasses.dataclass
class CoordinatesRequest:
    longitude: float
    latitude: float

    def __post_init__(self) -> None:
        self.longitude = round(self.longitude, 5)
        self.latitude = round(self.latitude, 5)
