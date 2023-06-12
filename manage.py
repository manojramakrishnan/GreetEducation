#!/user/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',"greets.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("couldn't import jango") from exc
    execute_from_command_line()



if __name__=='__main__':
    main()