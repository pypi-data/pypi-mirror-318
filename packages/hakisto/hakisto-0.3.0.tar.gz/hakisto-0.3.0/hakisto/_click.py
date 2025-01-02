import os
import sys
import typing as t

import click
from click.decorators import _param_memo

from hakisto import logger
from .severity import severity_names


if t.TYPE_CHECKING:
    import typing_extensions as te

    P = te.ParamSpec("P")

R = t.TypeVar("R")
T = t.TypeVar("T")
_AnyCallable = t.Callable[..., t.Any]
FC = t.TypeVar("FC", bound=t.Union[_AnyCallable, click.Command])


def hakisto_severity(
        *param_decls: str,
        default: str = None,
        choices: t.Sequence[str] = None,
        case_sensitive: bool = False,
        show_default: bool = True,
        cls: t.Optional[t.Type[click.Option]] = None,
        **attrs: t.Any) -> t.Callable[[FC], FC]:
    """Attaches HAKISTO SEVERITY option to the command.

    This is always a ``click.Choice`` option, with the default taken from HAKISTO_SEVERITY or ``INFO``.

    The default options are the Hakisto Severities (not case-sensitive).

    All positional arguments are  passed as parameter declarations to :class:`Option`,
    if none are provided, defaults to ``--log, --log-severity``.

    Keyword arguments not described below are passed as keyword arguments to :func:`click.Option`,
    arguments are forwarded unchanged (except ``cls``).

    :param default: default Hakisto Severity.
    :param choices: Lost of permitted Hakisto Severities.
    :param case_sensitive:
    :param show_default:
    :param cls: the option class to instantiate.  This defaults to :class:`Option`.
    :param param_decls: Passed as positional arguments to the constructor of ``cls``.
    :param attrs: Passed as keyword arguments to the constructor of ``cls``.
    """
    if cls is None:
        cls = click.Option
    if not param_decls:
        param_decls = ('--log', '--log-severity', 'log_severity')

    if not default:
        default = os.getenv("HAKISTO_SEVERITY", "INFO")
    attrs['default'] = default.upper()
    attrs['show_default'] = show_default
    if not choices:
        choices = severity_names.keys()
    choices = [i.upper() for i in choices]
    attrs['type'] = click.Choice(choices, case_sensitive=case_sensitive)
    if 'help' not in attrs:
        attrs['help'] = "Minimum Logging Severity"

    def decorator(f: FC) -> FC:
        _param_memo(f, cls(param_decls, **attrs))
        return f

    return decorator


def hakisto_file(
        *param_decls: str,
        default: bool = True,
        show_default: bool = True,
        cls: t.Optional[t.Type[click]] = None,
        **attrs: t.Any) -> t.Callable[[FC], FC]:
    """Attaches option enable or disable logging to a file to the command.

    All positional arguments are  passed as parameter declarations to :class:`Option`,
    if none are provided, defaults to ``--log-file/--no-log-file``.

    Keyword arguments not described below are passed as keyword arguments to :func:`click.Option`,
    arguments are forwarded unchanged (except ``cls``).

    :param default:
    :param show_default:
    :param cls: the option class to instantiate.  This defaults to :class:`Option`.
    :param param_decls: Passed as positional arguments to the constructor of ``cls``.
    :param attrs: Passed as keyword arguments to the constructor of ``cls``.
    """
    if cls is None:
        cls = click.Option

    if not param_decls:
        param_decls = ('--log-file/--no-log-file',)
    attrs['default'] = default
    attrs['show_default'] = show_default
    if 'help' not in attrs:
        attrs['help'] = "Log to file?"

    def decorator(f: FC) -> FC:
        _param_memo(f, cls(param_decls, **attrs))
        return f

    return decorator


def hakisto_process_severity(log_severity: str) -> None:
    """Process the Hakisto Severity option.

    :param log_severity:
    :type log_severity: str
    """
    logger.set_severity(severity_names.get(log_severity, 0))


def hakisto_process_file(log_file: bool) -> None:
    """Process the Hakisto File option.

    :param log_file:
    :type log_file: bool
    """
    if not log_file:
        logger.file_handler.severity = sys.maxsize
