class PriorityDetector:

    RULES = {
        "password": ("Low", "Password reset affects only one user."),
        "printer": ("Medium", "Printer issue affects one department."),
        "wifi": ("Medium", "Wi-Fi issue affecting one employee."),
        "wi-fi": ("Medium", "Wi-Fi issue affecting one employee."),
        "vpn": ("High", "VPN issue affecting remote access."),
        "server": ("Critical", "Server outage affects multiple users."),
        "network outage": ("Critical", "Company-wide network outage.")
    }

    @staticmethod
    def detect(issue):

        issue = issue.lower()

        for keyword, value in PriorityDetector.RULES.items():
            if keyword in issue:
                return value

        return (
            "Medium",
            "Default enterprise priority."
        )