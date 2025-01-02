import os
from pathlib import Path

from django.apps import AppConfig
from django.core.checks import register
from django.db.backends.signals import connection_created
from django.db.models.signals import class_prepared
from django.dispatch import receiver
from django.utils.autoreload import BaseReloader, autoreload_started, file_changed
from django.utils.termcolors import make_style

red = make_style(fg="red")
blue = make_style(fg="blue")
cyan = make_style(fg="cyan")
yellow = make_style(fg="yellow")
magenta = make_style(fg="magenta")
bold_yellow = make_style(opts=("bold",), fg="yellow")


class DebugConfig(AppConfig):
    name = "django_debug_signals"
    is_ready = False

    def ready(self):
        if os.environ.get("RUN_MAIN"):
            print(bold_yellow("App ready from main thread"))
        if self.is_ready is False:
            print(bold_yellow("ready"), __class__, os.getpid())
            self.is_ready = True
        else:
            raise Exception("ready called twice")


@register
def test_checks(*args, **kwargs):
    print(red("test_checks"), args, kwargs)
    return []


@receiver(connection_created, dispatch_uid="print_connection_created")
def print_connection_created(*args, **kwargs):
    print(red("connection_created"), args, kwargs)


@receiver(autoreload_started, dispatch_uid="print_autoreload_started")
def print_autoreload_started(sender: BaseReloader, **kwargs):
    print(magenta("autoreload_started"), sender, kwargs)


@receiver(file_changed, dispatch_uid="print_file_changed")
def print_file_changed(sender: BaseReloader, file_path: Path, **kwargs):
    print(magenta("file_changed"), sender, file_path, kwargs)


@receiver(class_prepared, dispatch_uid="print_class_prepared")
def print_class_prepared(sender, **kwargs):
    print(cyan("print_class_prepared"), sender, kwargs)
