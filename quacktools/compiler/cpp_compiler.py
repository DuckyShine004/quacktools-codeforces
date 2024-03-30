"""This module defines the c++ compiler. Allows the user to compile c++ code."""

from __future__ import annotations

import subprocess

from typing import TYPE_CHECKING

from quacktools.compiler.compiler import Compiler

if TYPE_CHECKING:
    from quacktools.app.app import App


class CPPCompiler(Compiler):
    """The CPPCompiler instance allows the user to compile c++ code.

    Attributes:
        executable_file (str): Executable filename.
    """

    def __init__(self, app: App) -> None:
        """Initializes the c++ compiler.

        Args:
            app (App): The application instance.
        """

        super().__init__(app)

        self.executable_file = ""

    def compile(self) -> None:
        """Compiles the user's code."""

        self.executable_file = self.filename + ".exe"
        command = f"g++ {self.file} -o {self.executable_file}"
        subprocess.run(command, check=True, shell=True)

        # Display compilation errors to user

    def get_program_output(self) -> None:
        """Get the user's program's code output."""

        user_outputs = []

        for sample_input in self.samples["input"]:
            sample_input = "".join(sample_input).strip()
            command = f"./{self.executable_file}"

            with open("output.txt", "w", encoding="utf-8") as output_file:
                subprocess.run(
                    command,
                    check=True,
                    stdout=output_file,
                    input=sample_input.encode(),
                    stderr=subprocess.PIPE,
                )

            with open("output.txt", "r", encoding="utf-8") as output_file:
                user_outputs.append(output_file.read())

        self.user_outputs = user_outputs
