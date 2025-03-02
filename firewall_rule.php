<?php
// Original vulnerable code in a pfSense package
$rule_desc = $_POST['description']; // User input from a firewall rule form
$command = "echo 'Rule: $rule_desc' >> /var/log/rules.log";
system($command); // Logs the rule description, but vulnerable to injection
echo "Rule added: " . $rule_desc;
?>
