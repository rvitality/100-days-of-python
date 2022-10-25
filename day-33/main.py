from datetime import datetime
import requests
from datetime import datetime

MY_LAT = 14.599512
MY_LONG = 120.984222


# ================================ #
# ISS POSITION
def is_iss_overhead():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json", timeout=130)
    iss_response.raise_for_status()

    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    # ================================ #

    # check if iss position is close to my positon
    return (
        iss_latitude >= MY_LAT - 5
        or iss_latitude <= MY_LAT + 5
        and iss_longitude >= MY_LONG - 5
        or iss_longitude <= MY_LONG + 5
    )


def is_night():
    api_parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get(
        "https://api.sunrise-sunset.org/json?", params=api_parameters, timeout=130
    )
    response.raise_for_status()

    data = response.json()
    results = data["results"]

    sunrise_hour = int(results["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(results["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour

    return current_hour >= sunset_hour and current_hour <= sunrise_hour


if is_iss_overhead() and is_night():
    print("Look Up! ISS is above you in the night sky! ")
