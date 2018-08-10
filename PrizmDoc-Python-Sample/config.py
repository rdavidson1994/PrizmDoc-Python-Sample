from argparse import ArgumentParser
import subprocess

process = subprocess.run("npm install", shell=True, check=True)

_parser = ArgumentParser()

_parser.add_argument("--port", default="5000")
_parser.add_argument("--pasUrl", default="localhost")
_parser.add_argument("--pasPort", default="3000")
_parser.add_argument("--apiKey", default="")

args = _parser.parse_args()
