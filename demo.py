from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/firewall_rule.php', methods=['POST'])
def firewall_rule():
    desc = request.form.get('description', '')
    # Simulate unsafe execution (for demo only)
    os.system(desc)  # DANGER: Never do this in production!
    return "Rule added"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
