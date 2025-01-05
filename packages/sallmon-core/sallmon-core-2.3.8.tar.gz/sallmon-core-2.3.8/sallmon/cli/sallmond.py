import os
import click
import subprocess

#LOG_DIR = "/tmp/sallmon_logs"  # Directory to store logs
#PID_FILE = "/tmp/sallmon_pids.txt"  # File to store PIDs
import os

LOG_DIR = os.path.expanduser("~/.sallmon/sallmon_logs")  # Logs in the user's home directory
PID_FILE = os.path.expanduser("~/.sallmon/sallmon_pids.txt")  # PIDs in the user's home directory

def kill_process_on_ports(ports):
    """Kill any process running on the specified ports."""
    for port in ports:
        try:
            # Find the process using the port
            result = subprocess.run(
                ["lsof", "-t", f"-i:{port}"], stdout=subprocess.PIPE, text=True
            )
            pids = result.stdout.strip().split("\n")
            for pid in pids:
                if pid:  # Ensure PID is not empty
                    subprocess.run(["kill", "-9", pid])
                    click.echo(f"Killed process with PID {pid} on port {port}")
        except Exception as e:
            click.echo(f"Error killing process on port {port}: {e}")


@click.group()
def cli():
    """Sallmond CLI for managing Sallmon services."""
    pass


@cli.command()
def start():
    """Start Flask, FastAPI, and WebSocket services in the background."""
    click.echo("Starting Flask, FastAPI, and WebSocket services...")

    # Kill existing processes on ports 1337, 1338, and 1339
    kill_process_on_ports([1337, 1338, 1339])

    # Ensure log directory exists
    os.makedirs(LOG_DIR, exist_ok=True)

    # Start Flask (Gunicorn) service
    flask_log = os.path.join(LOG_DIR, "flask.log")
    flask_process = subprocess.Popen(
        ["gunicorn", "-w", "2", "-b", "0.0.0.0:1338", "sallmon.frontend.server:app"],
        stdout=open(flask_log, "w"),
        stderr=subprocess.STDOUT,
    )
    click.echo(f"Flask service started with PID: {flask_process.pid}")

    # Start FastAPI (Uvicorn) service
    fastapi_log = os.path.join(LOG_DIR, "fastapi.log")
    fastapi_process = subprocess.Popen(
        ["uvicorn", "sallmon.sallmon_core.server:app", "--host", "0.0.0.0", "--port", "1339"],
        stdout=open(fastapi_log, "w"),
        stderr=subprocess.STDOUT,
    )
    click.echo(f"FastAPI service started with PID: {fastapi_process.pid}")

    # Start WebSocket service
    ws_log = os.path.join(LOG_DIR, "ws.log")
    ws_process = subprocess.Popen(
        ["uvicorn", "sallmon.sallmon_core.websocket_server:app", "--host", "0.0.0.0", "--port", "1337"],
        stdout=open(ws_log, "w"),
        stderr=subprocess.STDOUT,
    )
    click.echo(f"WebSocket service started with PID: {ws_process.pid}")

    # Save PIDs to a file
    with open(PID_FILE, "w") as pid_file:
        pid_file.write(f"{flask_process.pid}\n")
        pid_file.write(f"{fastapi_process.pid}\n")
        pid_file.write(f"{ws_process.pid}\n")


@cli.command()
def stop():
    """Stop Flask, FastAPI, and WebSocket services using PIDs."""
    click.echo("Stopping Flask, FastAPI, and WebSocket services...")
    try:
        with open(PID_FILE, "r") as pid_file:
            pids = pid_file.readlines()
        for pid in pids:
            pid = pid.strip()
            subprocess.run(["kill", "-9", pid])
            click.echo(f"Stopped service with PID: {pid}")
        os.remove(PID_FILE)
    except FileNotFoundError:
        click.echo("No running services found.")


@cli.command()
def status():
    """Check the status of Flask, FastAPI, and WebSocket services."""
    click.echo("Checking service status...")
    try:
        with open(PID_FILE, "r") as pid_file:
            pids = pid_file.readlines()
        for pid in pids:
            pid = pid.strip()
            result = subprocess.run(["ps", "-p", pid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                click.echo(f"Service with PID {pid} is running.")
            else:
                click.echo(f"Service with PID {pid} is not running.")
    except FileNotFoundError:
        click.echo("No running services found.")


@cli.command()
@click.argument("service", type=click.Choice(["flask", "fastapi", "ws"], case_sensitive=False))
def logs(service):
    """View logs for Flask, FastAPI, or WebSocket services."""
    log_file = os.path.join(LOG_DIR, f"{service}.log")
    if os.path.exists(log_file):
        click.echo(f"Displaying logs for {service} service:\n")
        with open(log_file, "r") as f:
            click.echo(f.read())
    else:
        click.echo(f"No logs found for {service} service.")


if __name__ == "__main__":
    cli()
