import time


class ControlArea:
    def __init__(self):
        self.alarms = []
        self.smoke_detected = False
        self.power_failure = False
        self.power_regained = False
        self.zone_name = "Ground Floor - (GF)"
        self.zone_alarms = ['GF-Alarm-1', 'GF-Alarm-2', 'GF-Alarm-3']

    def handle_fire_alarm(self, manual_alarm_confirmation, generate_incident_report_log):
        if self.smoke_detected:
            print("Smoke detected at", time.strftime("%Y-%m-%d %H:%M:%S"))
            if manual_alarm_confirmation.lower() == "yes":
                self.activate_system(generate_incident_report_log)
            elif manual_alarm_confirmation.lower() == "no":
                self.handle_false_alarm(generate_incident_report_log)
        else:
            print("No smoke detected.")

    def activate_system(self, generate_incident_report_log):
        print("System activated at", time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Activating alarm")
        print("Activating sprinklers")
        print("Closing doors")
        print("Activating emergency lighting")
        print("Calling emergency services")
        if generate_incident_report_log.lower() == "yes":
            print("Alarm system activated at",
                  time.strftime("%Y-%m-%d %H:%M:%S"))
            print("Alarm zone:", self.zone_name)
            print("Alarms activated:", ', '.join(self.zone_alarms))
            self.terminate_system()
        else:
            self.terminate_system()

    def handle_false_alarm(self, generate_incident_report_log):
        print("False alarm.")
        if generate_incident_report_log.lower() == "yes":
            print("False alarm triggered at ",
                  time.strftime("%Y-%m-%d %H:%M:%S"))
            print("Alarm zone:", self.zone_name)
            print("Alarms activated:", ', '.join(self.zone_alarms))
            self.reset_system()
        else:
            self.reset_system()

    def reset_system(self):
        print("System reset at", time.strftime("%Y-%m-%d %H:%M:%S"))
        self.smoke_detected = False

    def terminate_system(self):
        print("System terminated at", time.strftime("%Y-%m-%d %H:%M:%S"))

    def handle_power_failure(self):
        print("Power failure detected")
        print("Waiting 20 seconds to regain power")
        time.sleep(20)
        if not self.power_regained:
            print("Calling emergency services")
            print("Activating emergency lighting")
            self.reset_system()
        else:
            self.handle_fire_alarm("yes", "yes")
