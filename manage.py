#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
        ) from exc
    execute_from_command_line(sys.argv)
