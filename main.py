import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(json_bytes: bytes) -> Car:
    data = json.loads(json_bytes.decode("utf-8"))
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    else:
        raise ValueError("Invalid data")
