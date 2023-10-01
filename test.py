import subprocess
import time
import os
import getpass  # Add this import

# Specify a location for the log files (e.g., the user's home directory)
log_dir = os.path.expanduser("~")
logging = False
log_file = None

def get_user_level():
    return "root" if os.geteuid() == 0 else "user"

def start_logging():
    global logging, log_file
    if not logging:
        logging = True
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")  # Add seconds to the timestamp
        log_file = os.path.join(log_dir, f"command_log_{timestamp}.html")
        print(f"Logging started. Log file: {log_file}")
        with open(log_file, 'w') as log:
            log.write("<html>\n")
            log.write("<head><title>Command Log</title></head>\n")
            log.write("<body>\n")
            log.write(f"<h1>Logging started at {time.strftime('%Y.%m.%d %H:%M')}</h1>\n")
    else:
        print("Logging is already active")

def stop_logging():
    global logging, log_file
    if logging:
        logging = False
        print("Logging stopped")
        with open(log_file, 'a') as log:
            log.write(f"<h1>Logging stopped at {time.strftime('%Y.%m.%d %H:%M')}</h1>\n")
            log.write("</body>\n")
            log.write("</html>\n")
    else:
        print("Logging is not active")

def change_directory(user_input):
    global log_dir
    new_directory = user_input[3:]
    try:
        os.chdir(new_directory)
        print(f"Changed directory to {os.getcwd()}")
        log_dir = os.getcwd()
    except FileNotFoundError:
        print(f"Directory not found: {new_directory}")

def execute_command(user_input):
    global logging, log_file
    user_level = get_user_level()
    username = getpass.getuser()  # Get the current user's name
    try:
        completed_process = subprocess.run(user_input, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        current_directory = os.getcwd()

        if logging:
            with open(log_file, 'a') as log:
                log.write(f"<p><strong>Command:</strong> <span style=\"color:red;\">{user_input}</span> | <strong>Date:</strong> {time.strftime('%Y-%m-%d')} | <strong>Time:</strong> {time.strftime('%H:%M:%S')} | <strong>Issued by:</strong> {username} at {current_directory} | <strong>User level:</strong> {user_level}</p>\n")
                log.write(f"<pre><code>{completed_process.stdout}</code></pre>\n")
                log.write(f"<pre><code>{completed_process.stderr}</code></pre>\n")

        print(completed_process.stdout)
        print(completed_process.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# Display initial documentation
print("Commands:")
print("logger -start -> Start logging")
print("logger -stop  -> Stop logging")
print("logger -cd <directory> -> Change the working directory")
print("logger -help -> Show this documentation")

# Main loop
while True:
    cwd = os.getcwd()
    user_input = input(f"{cwd} $ ")

    if user_input == "logger -start":
        start_logging()

    elif user_input == "logger -stop":
        stop_logging()

    elif user_input.startswith("logger -cd "):
        change_directory(user_input)

    elif user_input == "logger -help":
        print("Commands:")
        print("logger -start -> Start logging")
        print("logger -stop  -> Stop logging")
        print("logger -cd <directory> -> Change the working directory")
        print("logger -help -> Show this documentation")
        
    elif user_input == "exit":
        break

    else:
        execute_command(user_input)
