import os

def check_website_status(hostname):
    """
    Pings a host to see if it's online.
    This function is VULNERABLE to Command Injection.
    """
    # Vulnerable: The hostname is passed directly to a shell command.
    command = f"ping -c 1 {hostname}"
    print(f"Running command: {command}")
    os.system(command)

# --- Exploitation Example ---
# A normal hostname might be 'google.com'
# check_website_status('google.com')

# An attacker can use ';' (or '&&') to chain commands.
# This will ping google.com AND then list the contents of the current directory.
malicious_hostname = "google.com; ls -la"
check_website_status(malicious_hostname)
