"""
Usage:
    Dojo create_room <room_type> <room_name>...
    Dojo add_person <name> <person_type> [acco]
    Dojo (-i | --interactive)
    Dojo -h | --help
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    
"""
import sys
import cmd

from docopt import docopt, DocoptExit
from class_implementation import Implementation


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):

    prompt = '(Dojo) '
    file = None

    @docopt_cmd
    def do_create_room(self,args):

        """Usage: create_room <room_type> <room_name>..."""
        names=[name for name in args['<room_name>']]
        if len(args['<room_type>'])-1>1:
            for name in args['<room_name>']:
                ob=Implementation()
                value=ob.create_room(name,args['<room_type>'])
        else:
            ob=Implementation()
            value=ob.create_room(args['<room_name>'][0],args['<room_type>'])

        print(args['<room_type>'])
        print(args['<room_name>'])

    @docopt_cmd
    def do_add_person(self,args):
        """if person is Fellow s/he can allocated both an office and livingspace"""
        #person.add_person(name,person_type)
        """Usage: add_person <name> <person_type> [acco]"""

        ob=Implementation()
        ob.add_person(args['<name>'],args['<person_type>'],args['acco'])




    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])
arguments = docopt(__doc__)
#print(arguments)

if opt['--interactive']:
    MyInteractive().cmdloop()
elif opt['-h'] or opt['--help']:
    pass
print(opt)