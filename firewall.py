import subprocess

def run_command(command):
    """
    Run a system command and return the output.
    """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout

def add_rule(rule_name, direction, action, protocol, local_port, remote_ip):
    """
    Add a rule to the Windows Firewall.
    """
    command = (
        f"netsh advfirewall firewall add rule name={rule_name} "
        f"dir={direction} action={action} protocol={protocol} "
        f"localport={local_port} remoteip={remote_ip}"
    )
    print(f"Adding rule: {command}")
    return run_command(command)

def delete_rule(rule_name):
    """
    Delete a rule from the Windows Firewall.
    """
    command = f"netsh advfirewall firewall delete rule name={rule_name}"
    print(f"Deleting rule: {command}")
    return run_command(command)

def list_rules():
    """
    List all Windows Firewall rules.
    """
    command = "netsh advfirewall firewall show rule name=all"
    return run_command(command)

# Example usage
if __name__ == "__main__":
    # Add a rule to block all incoming traffic from a specific IP
    rule_name = "BlockIncomingTrafficFromIP"
    direction = "in"
    action = "block"
    protocol = "TCP"
    local_port = "any"
    remote_ip = "192.168.1.100"
    add_rule(rule_name, direction, action, protocol, local_port, remote_ip)

    # List current rules
    print("Current Windows Firewall rules:")
    print(list_rules())

    # Remove the rule
    delete_rule(rule_name)

    # List rules after deletion
    print("Windows Firewall rules after deletion:")
    print(list_rules())
