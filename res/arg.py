from argparse import ArgumentParser

parser = ArgumentParser(
    description="File Sharing Web Application", usage="%(prog)s [options]"
)
parser.add_argument(
    "-p", "--port",
    type=int,
    dest="port",
    nargs="?",
    help="Define Network Port"
)
parser.add_argument(
    "-path", "--set-path",
    type=str,
    dest="path",
    nargs="?",
    default="MiShared/",
    help="Set File Path"
)
parser.add_argument(
    "-v", "--version",
    action="store_true",
    help="Print Version",
)
args = parser.parse_args()
