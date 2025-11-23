from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Limo", 100, 2)
    taxi.drive(18)
    fare = taxi.get_fare()
    print(f"Fare for 18km: ${fare:.2f}")
    assert round(fare, 2) == 48.80, "Fare should be $48.80"


main()
