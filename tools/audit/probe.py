import subprocess


def run(cmd: str) -> int:
    return subprocess.call(cmd, shell=True)
