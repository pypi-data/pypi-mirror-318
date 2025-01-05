#  hakisto - logging reimagined
#
#  Copyright (C) 2024  Bernhard Radermacher
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


# logger using PyPubSub to improve flexibility

import inspect
import os
import sys
import threading
from types import FrameType, TracebackType

from .pub_sub import send_message
from .topic import construct_topic, extract_topic
from .severity import TRACE, DEBUG, VERBOSE, INFO, SUCCESS, WARNING, ERROR, CRITICAL, severity_names
from .subject import Subject

__all__ = ["Logger"]


class Logger:
    """Main Logger class. Can be inherited from, but should be sufficient for most situations.

    .. include:: logger_name.txt

    :param name: Logger name.
    :type name: str, optional
    """

    __excluded_source_files = set()
    __lock = threading.RLock()

    def __init__(self, name: str = "", **kwargs) -> None:
        self._lock = threading.RLock()
        self._name, self._topic = construct_topic(name, self.__class__.__name__)
        hakisto_severity = os.getenv("HAKISTO_SEVERITY", "").upper()
        self.severity = severity_names.get(hakisto_severity, 0)

    def set_severity(self, severity: int) -> None:
        with self._lock:
            self.severity = severity

    @property
    def severity(self) -> int:
        return self._severity

    @severity.setter
    def severity(self, severity: int):
        with self._lock:
            self._severity = severity

    @property
    def name(self) -> str:
        return self._name

    @property
    def topic(self) -> str:
        return self._topic

    @classmethod
    def register_excluded_source_file(cls, file_name: str) -> None:
        """This must be called in the source file of any descendent to exclude the respective
        entries in the call-stack.

        Recommendation: Call on source file level (module).

        .. code:: python

           Logger.register_excluded_source_file(inspect.currentframe().f_code.co_filename)

        :param file_name: Source file name
        :type file_name: str
        """
        with cls.__lock:
            cls.__excluded_source_files.add(file_name)

    @classmethod
    def get_excluded_source_files(cls) -> set[str]:
        """Get a copy of excluded_source_files when identifying *real* caller in call-stack.

        :rtype: set[str]
        """
        return cls.__excluded_source_files.copy()

    def critical(self, *args: str, message_id: str = None, force_location: bool = False, **kwargs) -> None:
        """Log a **CRITICAL** entry.

        ``CRITICAL`` entries will include the respective source location, source section and local variables.

        :param args: The Message(s). Every message will create a separate entry.
        :type args: str
        :param message_id: Message ID.
        :type message_id: str
        :param force_location: Force output of location
        :type force_location: bool
        """
        self.log(CRITICAL, message_id=message_id, force_location=force_location, *args, **kwargs)

    def error(self, *args: str, message_id: str = None, force_location: bool = False, **kwargs) -> None:
        """Log an **ERROR** entry.

        ``ERROR`` entries will include the respective source location.

        :param args: The Message(s). Every message will create a separate entry.
        :type args: str
        :param message_id: Message ID.
        :type message_id: str
        :param force_location: Force output of location
        :type force_location: bool
        """
        self.log(ERROR, message_id=message_id, force_location=force_location, *args, **kwargs)

    def warning(self, *args: str, message_id: str = None, force_location: bool = False, **kwargs) -> None:
        """Log a **WARNING** entry.

        :param args: The Message(s). Every message will create a separate entry.
        :type args: str
        :param message_id: Message ID.
        :type message_id: str
        :param force_location: Force output of location
        :type force_location: bool
        """
        self.log(WARNING, message_id=message_id, force_location=force_location, *args, **kwargs)

    def success(self, *args: str, message_id: str = None, force_location: bool = False, **kwargs) -> None:
        """Log a **SUCCESS** entry.

        This has been added to support responses from SAP.

        :param args: The Message(s). Every message will create a separate entry.
        :type args: str
        :param message_id: Message ID.
        :type message_id: str
        :param force_location: Force output of location
        :type force_location: bool
        """
        self.log(SUCCESS, message_id=message_id, force_location=force_location, *args, **kwargs)

    def info(self, *args: str, message_id: str = None, force_location: bool = False, **kwargs) -> None:
        """Log an **INFO** entry.

        :param args: The Message(s). Every message will create a separate entry.
        :type args: str
        :param message_id: Message ID.
        :type message_id: str
        :param force_location: Force output of location
        :type force_location: bool
        """
        self.log(INFO, message_id=message_id, *args, **kwargs)

    def verbose(self, *args: str, message_id: str = None, force_location: bool = False, **kwargs) -> None:
        """Log a **VERBOSE** entry.

        :param args: The Message(s). Every message will create a separate entry.
        :type args: str
        :param message_id: Message ID.
        :type message_id: str
        :param force_location: Force output of location
        :type force_location: bool
        """
        self.log(VERBOSE, message_id=message_id, force_location=force_location, *args, **kwargs)

    def debug(self, *args: str, message_id: str = None, force_location: bool = False, **kwargs) -> None:
        """Log a **DEBUG** entry.

        :param args: The Message(s). Every message will create a separate entry.
        :type args: str
        :param message_id: Message ID.
        :type message_id: str
        :param force_location: Force output of location
        :type force_location: bool
        """
        self.log(DEBUG, message_id=message_id, force_location=force_location, *args, **kwargs)

    def trace(self, *args: str, message_id: str = None, force_location: bool = False, **kwargs) -> None:
        """Log a **TRACE** entry.

        :param args: The Message(s). Every message will create a separate entry.
        :type args: str
        :param message_id: Message ID.
        :type message_id: str
        :param force_location: Force output of location
        :type force_location: bool
        """
        self.log(TRACE, message_id=message_id, force_location=force_location, *args, **kwargs)

    def log(self, severity, *args: str, message_id: str = None, force_location: bool = False, **kwargs) -> None:
        """Log an entry.

        While this method has been made public, be advised, that using integers directly might break in the
        future, if the implementation is modified.

        :param severity: The severity level of the log entry.
        :type severity: int
        :param args: The Message(s). Every message will create a separate entry.
        :type args: str
        :param message_id: Message ID.
        :type message_id: str
        :param force_location: Force output of location
        :type force_location: bool
        """
        if severity < self.severity:
            return
        frame = self._get_caller()
        for message in args:
            self._send_log(
                Subject(
                    topic=extract_topic(self.topic),
                    severity=severity,
                    frame=frame,
                    message=str(message),
                    message_id=message_id,
                    force_location=force_location,
                    **kwargs,
                )
            )

    def set_handler_severity(self, severity: int) -> None:
        """Set the minimum severity for all Handlers listening to the logger's topic.

        :param severity: New severity.
        :type severity: int
        """
        # noinspection PyTypeChecker
        self._send_log(
            Subject(
                topic=extract_topic(self.topic),
                severity=severity,
                frame=None,
                message=None,
                message_id=None,
                __set_severity__=severity,
            )
        )

    def set_date_format(self, date_format: str) -> None:
        """Set the date format for all Handlers listening to the logger's topic.

        :param date_format: New date format.
        :type date_format: str
        """
        # noinspection PyTypeChecker
        self._send_log(
            Subject(
                topic=extract_topic(self.topic),
                severity=0,
                frame=None,
                message=None,
                message_id=None,
                __set_date_format__=date_format,
            )
        )

    def _get_caller(self) -> FrameType:
        """Return *real* caller.

        If this method is overridden, make sure that the right frames are excluded.

        :meta public:
        """
        frame = inspect.currentframe()
        while frame.f_code.co_filename in self.get_excluded_source_files():
            frame = frame.f_back
        return frame

    def _send_log(self, subject: Subject) -> None:
        send_message(self.topic, subject=subject)

    def __repr__(self):
        return f"Logger(name='{self.name}')"


Logger.register_excluded_source_file(inspect.currentframe().f_code.co_filename)


def log_exception(exception_class: type, exception: Exception, trace_back: TracebackType):
    """Hook to handle uncaught exceptions.

    The entry is sent to **all** Handlers.
    A :class:`imuthes.logging.Handler` **must** implement ``handle_exception`` when it should react to this.
    """
    send_message("-", subject=Subject(topic="-", severity=sys.maxsize, frame=trace_back, message=str(exception)))


sys.excepthook = log_exception
