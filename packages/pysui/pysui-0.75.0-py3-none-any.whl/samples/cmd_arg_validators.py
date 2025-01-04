#    Copyright Frank V. Castellucci
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#        http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# -*- coding: utf-8 -*-

"""Argparse validators for sample script reuse."""

import sys
import argparse
import base64
import binascii
from pathlib import Path
from typing import Any, Sequence
from pysui.sui.sui_constants import SUI_MAX_ALIAS_LEN, SUI_MIN_ALIAS_LEN
from pysui.sui.sui_types.address import valid_sui_address


class ValidateAlias(argparse.Action):
    """Alias string validator."""

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = ...,
    ) -> None:
        """Validate."""
        vlen: int = len(values)
        if SUI_MIN_ALIAS_LEN <= vlen <= SUI_MAX_ALIAS_LEN:
            setattr(namespace, self.dest, values)
        else:
            parser.error(
                f"Invalid alias string length, must be betwee {SUI_MIN_ALIAS_LEN} and {SUI_MAX_ALIAS_LEN} characters."
            )
            sys.exit(-1)


class ValidateAddress(argparse.Action):
    """Address validator."""

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = ...,
    ) -> None:
        """Validate."""
        if isinstance(values, list):
            for va in values:
                if not valid_sui_address(va):
                    parser.error(f"'{values}' contains invlaid Sui address.")
                    sys.exit(-1)
        else:
            if not valid_sui_address(values):
                parser.error(f"'{values}' is not a valid Sui address.")
                sys.exit(-1)
        setattr(namespace, self.dest, values)


class ValidateObjectID(argparse.Action):
    """ObjectID validator."""

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = ...,
    ) -> None:
        """Validate."""
        if isinstance(values, list):
            for va in values:
                if not valid_sui_address(va):
                    parser.error(f"'{values}' contains invlaid Sui address.")
                    sys.exit(-1)
        else:
            if not valid_sui_address(values):
                parser.error(f"'{values}' is not a valid Sui address.")
                sys.exit(-1)
        setattr(namespace, self.dest, values)


class ValidatePackageDir(argparse.Action):
    """Validate package directory."""

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = ...,
    ) -> None:
        """Validate."""
        ppath = Path(values)
        if not ppath.exists:
            parser.error(f"{str(ppath)} does not exist.")
        setattr(namespace, self.dest, ppath)


class ValidateB64(argparse.Action):
    """Validate base64 string."""

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = ...,
    ) -> None:
        """Validate."""
        try:
            if isinstance(values, list):
                res = [base64.b64decode(x, validate=True) for x in values]
            else:
                res = base64.b64decode(values, validate=True)
            setattr(namespace, self.dest, values)
        except binascii.Error as bae:
            parser.error(f"{values} invalide base64 string")
