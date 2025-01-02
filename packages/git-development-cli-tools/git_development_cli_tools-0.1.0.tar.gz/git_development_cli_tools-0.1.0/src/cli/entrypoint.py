#!/usr/bin/env python3

# Standard libraries
from argparse import Namespace
from enum import Enum

# Entrypoint class, pylint: disable=too-few-public-methods
class Entrypoint:

    # Enumerations
    Result = Enum('Result', [
        'SUCCESS',
        'FINALIZE',
        'ERROR',
        'CRITICAL',
    ])

    # CLI
    @staticmethod
    def cli(options: Namespace) -> Result:

        # TODO, pylint: disable=fixme
        print(options)

        # Result
        return Entrypoint.Result.SUCCESS
