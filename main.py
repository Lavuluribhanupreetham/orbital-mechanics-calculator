"""
Orbital Mechanics Calculator - CLI entry point.
Ties together the three functional modules:
    1. orbital_calculations  - velocity, escape velocity, period
    2. hohmann_transfer      - two-orbit transfer planning
    3. mission_log           - history persistence + reporting
Run with:  python main.py
"""
import logging
from orbital_calculations import orbital_velocity, escape_velocity, orbital_period
from hohmann_transfer import hohmann_transfer
from mission_log import MissionLog
logging.basicConfig(
    filename="orbital_calculator.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",)
logger = logging.getLogger(__name__)
MENU = """
=============================================
       ORBITAL MECHANICS CALCULATOR
=============================================
Choose an option:
1. Calculate Orbital Velocity
2. Calculate Escape Velocity
3. Calculate Orbital Period
4. Plan a Hohmann Transfer
5. View Mission Report / History
6. Exit
"""
def read_altitude(prompt: str) -> float:
    """Read and validate a single altitude value from the user."""
    value = float(input(prompt))
    if value < 0:
        raise ValueError("Altitude cannot be negative.")
    return value
def handle_single_value(choice: str, log: MissionLog) -> None:
    altitude = read_altitude("Enter altitude above Earth's surface (km): ")
    if choice == "1":
        result = orbital_velocity(altitude)
        print(f"\nOrbital velocity at {altitude:.1f} km: {result:.2f} km/s")
        log.record("Orbital Velocity", {"altitude_km": altitude}, {"velocity_km_s": round(result, 2)})
    elif choice == "2":
        result = escape_velocity(altitude)
        print(f"\nEscape velocity at {altitude:.1f} km: {result:.2f} km/s")
        log.record("Escape Velocity", {"altitude_km": altitude}, {"velocity_km_s": round(result, 2)})
    elif choice == "3":
        result = orbital_period(altitude)
        print(f"\nOrbital period at {altitude:.1f} km: {result:.2f} minutes")
        log.record("Orbital Period", {"altitude_km": altitude}, {"period_min": round(result, 2)})
def handle_hohmann(log: MissionLog) -> None:
    initial_altitude = read_altitude("Enter initial orbit altitude (km): ")
    final_altitude = read_altitude("Enter final orbit altitude (km): ")
    result = hohmann_transfer(initial_altitude, final_altitude)
    print("\n" + "=" * 45)
    print("          HOHMANN TRANSFER")
    print("=" * 45)
    print(f"Initial orbit velocity:  {result.velocity_initial:.2f} km/s")
    print(f"Final orbit velocity:    {result.velocity_final:.2f} km/s")
    print(f"Transfer velocity 1:     {result.velocity_transfer_1:.2f} km/s")
    print(f"Transfer velocity 2:     {result.velocity_transfer_2:.2f} km/s")
    print(f"\nFirst burn (dv1):        {result.delta_v_1:.2f} km/s")
    print(f"Second burn (dv2):       {result.delta_v_2:.2f} km/s")
    print(f"Total delta-v:           {result.total_delta_v:.2f} km/s")
    print(
        f"\nTransfer time:           {result.transfer_time_sec / 60:.2f} minutes "
        f"({result.transfer_time_sec / 3600:.2f} hours)")
    log.record(
        "Hohmann Transfer",
        {"initial_altitude_km": initial_altitude, "final_altitude_km": final_altitude},
        {"total_delta_v_km_s": round(result.total_delta_v, 2),
         "transfer_time_hr": round(result.transfer_time_sec / 3600, 2)},
    )
def main() -> None:
    log = MissionLog()
    logger.info("Session started.")
    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()
        try:
            if choice in {"1", "2", "3"}:
                handle_single_value(choice, log)
            elif choice == "4":
                handle_hohmann(log)
            elif choice == "5":
                log.print_report()
            elif choice == "6":
                print("\nThank you for using the calculator!")
                logger.info("Session ended normally.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
        except ValueError as exc:
            print(f"\n[Input Error] {exc}")
            logger.warning("Input error: %s", exc)
        except Exception as exc:  
            print(f"\n[Unexpected Error] {exc}")
            logger.error("Unexpected error: %s", exc)
if __name__ == "__main__":
    main()