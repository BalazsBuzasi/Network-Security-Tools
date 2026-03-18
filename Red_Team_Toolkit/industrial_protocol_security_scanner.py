from pymodbus.client.sync import ModbusTcpClient
import logging

# Basic logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def modbus_security_scan(target_ip, port=502):
    print(f"--- Starting Modbus Security Scan: {target_ip} ---")

    # Establish connection to the PLC or Simulator
    client = ModbusTcpClient(target_ip, port=port)

    if client.connect():
        print(f"[+] SUCCESS: Connection established on {target_ip}:{port}")
        print(f"[!] SECURITY RISK: Device is responding via cleartext protocol (Insecure).")

        try:
            # Attempt to read 10 holding registers (e.g., sensor data)
            # Standard Modbus lacks authentication—this highlights the vulnerability!
            result = client.read_holding_registers(address=0, count=10, slave=1)

            if not result.isError():
                print(f"[+] DATA RETRIEVED: {result.registers}")
                print(f"[!!!] CRITICAL VULNERABILITY: Unauthenticated Access Detected. Values can be modified by any network actor.")
            else:
                print("[-] Could not read registers, but the port is open and exposed.")

        except Exception as e:
            print(f"[-] Error during query: {e}")
        finally:
            client.close()
            print("--- Scan Completed ---")
    else:
        print(f"[-] FAILURE: Could not connect to {target_ip}. Device is offline or protected by a firewall.")

if __name__ == "__main__":
    target = input("Enter Target IP (e.g., 127.0.0.1 for local testing): ")
    modbus_security_scan(target)

