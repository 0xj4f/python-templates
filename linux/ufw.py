import subprocess

class FirewallManager:
    def __init__(self):
        self.ufw_path = "/usr/sbin/ufw"

    def run_command(self, cmd):
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr.strip()}")
        else:
            print(result.stdout.strip())

    def enable_firewall(self):
        self.run_command(f"{self.ufw_path} enable")

    def allow_port(self, port, proto="tcp"):
        self.run_command(f"{self.ufw_path} allow {port}/{proto}")

    def deny_port(self, port, proto="tcp"):
        self.run_command(f"{self.ufw_path} deny {port}/{proto}")

    def status(self):
        self.run_command(f"{self.ufw_path} status verbose")

if __name__ == "__main__":
    fw = FirewallManager()
    # Example: allow only ssh, http, https, block everything else by default
    fw.enable_firewall()
    fw.allow_port(22)    # ssh
    fw.allow_port(80)    # http
    fw.allow_port(443)   # https
    fw.status()
