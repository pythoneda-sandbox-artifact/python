# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/artifact/sandbox.py

This file declares the Sandbox class.

Copyright (C) 2023-today rydnr's pythoneda-sandbox-artifact/python

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared.artifact import (
    ArchitecturalRole,
    HexagonalLayer,
    PescioSpace,
    PythonPackage,
)
from pythoneda.shared.nix.flake import (
    FlakeUtilsNixFlake,
    License,
    NixosNixFlake,
    PythonedaSharedPythonedaBannerNixFlake,
)
from pythoneda.shared.nix.flake.licenses import Gpl3


class Sandbox(PythonPackage):
    """
    Represents the pythoneda-sandbox/python Python package.

    Class name: Domain

    Responsibilities:
        - Model the pythoneda-sandbox/python Python package and its metadata.

    Collaborators:
        - pythoneda.shared.artifact.PythonPackage
    """

    def __init__(self, version: str):
        """
        Creates a new Sandbox instance.
        :param version: The package version.
        :type version: str
        """
        flake_utils = FlakeUtilsNixFlake.default()
        nixos = NixosNixFlake.default()
        banner = PythonedaSharedPythonedaBannerNixFlake.default()
        inputs = [flake_utils, nixos, banner]
        super().__init__(
            "rydnr",
            version,
            f"https://github.com/pythoneda-sandbox-def/python/{version}",
            inputs,
            "pythoneda",
            "Artifact space of https://github.com/pythoneda-sandbox/python",
            self.__class__.url,
            License.from_id(
                Gpl3.license_type(),
                "2023",
                "rydnr",
                self.__class__.url,
            ),
            ["rydnr <github@acm-sl.org>"],
            2023,
            "rydnr",
            PescioSpace.DECISION,
            ArchitecturalRole.BOUNDED_CONTEXT,
            HexagonalLayer.DOMAIN,
        )

    @classmethod
    @property
    def url(cls) -> str:
        """
        Retrieves the url.
        :return: Such url.
        :rtype: str
        """
        return "https://github.com/pythoneda-sandbox-def/python"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
