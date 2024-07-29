from pyngrok import ngrok
import subprocess

# Start ngrok tunnel
public_url = ngrok.connect(8080)
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:8080\"".format(public_url))

# Start Flask app
subprocess.run(["python", "app.py"])