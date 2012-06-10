import argparse
import sys
import inspect

# customized parser show help message when no positional arguments given
class HelpOnErrorParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def find_actions(namespace, action_prefix):
    """Find all the actions in the namespace."""
    actions = {}
    for key, value in namespace.iteritems():
        if key.startswith(action_prefix):
            actions[key[len(action_prefix):]] = analyse_action(value)
    return actions

def analyse_action(func):
    """Analyse a function."""
    description = inspect.getdoc(func) or 'undocumented action'
    arguments = []
    args, varargs, kwargs, defaults = inspect.getargspec(func)
    if varargs or kwargs:
        raise TypeError('variable length arguments for action not allowed.')
    if len(args) != len(defaults or ()):
        raise TypeError('not all arguments have proper definitions')

    for idx, (arg, definition) in enumerate(zip(args, defaults or ())):
        if arg.startswith('_'):
            raise TypeError('arguments may not start with an underscore')
        if not isinstance(definition, tuple):
            shortcut = None
            default = definition
        else:
            shortcut, default = definition
        argument_type = type(default)
        #if isinstance(default, bool) and default is True:
        #    arg = 'no-' + arg
        arguments.append((arg.replace('_', '-'), shortcut,
                          default, argument_type))
    return func, description, arguments

def run(namespace=None, action_prefix='action_', args=None):
    if namespace is None:
        namespace = sys._getframe(1).f_locals
    if args is None:
        args = sys.argv[1:]

    actions = find_actions(namespace, action_prefix)
    parser = HelpOnErrorParser(description=namespace['__doc__'])
    subparsers = parser.add_subparsers(dest='_func')   

    for name, (func, description, arguments) in actions.items():
        doc = description.splitlines()[0]
        argument_doc = {}
        for line in description.splitlines()[1:]:
            r = line.split('--', 1)
            if len(r) == 2:
                argument_doc[r[0].strip()] = r[1].strip()

        subparser =  subparsers.add_parser(name , description=doc)
        for argname, shortcut, default, argument_type in arguments:
            help_msg = argument_doc.get(argname, '')
            if shortcut:
                subparser.add_argument('-'+shortcut, '--'+argname, default=default, type=argument_type, help=help_msg)
            else:
                subparser.add_argument('--'+argname, default=default, type=argument_type, help=help_msg)

    kwargs = vars(parser.parse_args(args))
    func = kwargs.pop('_func')
    actions[func][0](**kwargs)


