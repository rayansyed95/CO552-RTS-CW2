from control_area import ControlArea


def main():
    control_area = ControlArea()

    # Example conditions
    # check for True / False to see the difference
    control_area.smoke_detected = False
    control_area.power_failure = False  # check for True / False to see the difference
    # check for True / False to see the difference
    control_area.power_regained = False

    if control_area.power_failure:
        control_area.handle_power_failure()
    else:
        control_area.handle_fire_alarm("yes", "yes")


if __name__ == "__main__":
    main()
