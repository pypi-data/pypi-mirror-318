import os
import click
import subprocess

LOG_DIR = "/tmp/sallmon_logs"  # Directory to store logs
PID_FILE = "/tmp/sallmon_pids.txt"  # File to store PIDs

@click.group()
def cli():
    """Sallmond CLI for managing Sallmon services."""
    pass

@cli.command()
def start():
    """Start Flask and FastAPI services in the background."""
    click.echo("Starting Flask and FastAPI services...")

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
        ["uvicorn", "sallmon.sallmon_core.server:app", "--host", "0.0.0.0", "--port", "1337"],
        stdout=open(fastapi_log, "w"),
        stderr=subprocess.STDOUT,
    )
    click.echo(f"FastAPI service started with PID: {fastapi_process.pid}")

    # Save PIDs to a file
    with open(PID_FILE, "w") as pid_file:
        pid_file.write(f"{flask_process.pid}\n")
        pid_file.write(f"{fastapi_process.pid}\n")


@cli.command()
def stop():
    """Stop Flask and FastAPI services using PIDs."""
    click.echo("Stopping Flask and FastAPI services...")
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
    """Check the status of Flask and FastAPI services."""
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
@click.argument("service", type=click.Choice(["flask", "fastapi"], case_sensitive=False))
def logs(service):
    """View logs for Flask or FastAPI services."""
    log_file = os.path.join(LOG_DIR, f"{service}.log")
    if os.path.exists(log_file):
        click.echo(f"Displaying logs for {service} service:\n")
        with open(log_file, "r") as f:
            click.echo(f.read())
    else:
        click.echo(f"No logs found for {service} service.")


if __name__ == "__main__":
    cli()
