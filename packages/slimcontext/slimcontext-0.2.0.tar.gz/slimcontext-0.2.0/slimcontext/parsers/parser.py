"""MultiFileContextParser is responsible for parsing multiple file types and generating context.

Copyright (c) 2024 Neil Schneider, All rights reserved.
"""

from pathlib import Path

from slimcontext.parsers.htmlparse.htmlparser import HtmlParser
from slimcontext.parsers.pyparse.pyparser import PyParser
from slimcontext.parsers.utils import generate_context_header
from slimcontext.utils.logger import setup_logger

logger = setup_logger(__name__)


class ProjectParser:
    """A high-level parser that delegates to specialized sub-parsers for certain file extensions.

    Uses fallback "read the entire file" for unknown types.
    """

    def __init__(self, root_dir: Path | None = None) -> None:
        """Initialize the ProjectParser with an optional root directory."""
        self.root_dir = root_dir or Path.cwd()

        # Initialize extension assignments
        self.extension_assignments = {
            '.py': 'unassigned',
            '.js': 'unassigned',
            '.jsx': 'unassigned',
            '.ts': 'unassigned',
            '.tsx': 'unassigned',
            '.c': 'unassigned',
            '.cpp': 'unassigned',
            '.h': 'unassigned',
            '.hpp': 'unassigned',
            '.java': 'unassigned',
            '.go': 'unassigned',
            '.rs': 'unassigned',
            '.sh': 'unassigned',
            '.rb': 'unassigned',
            '.swift': 'unassigned',
            '.php': 'unassigned',
            '.kt': 'unassigned',
            '.kts': 'unassigned',
            '.html': 'unassigned',
            '.htm': 'unassigned',
            '.css': 'unassigned',
            '.scss': 'unassigned',
            '.sass': 'unassigned',
            '.yaml': 'unassigned',
            '.yml': 'unassigned',
            '.json': 'unassigned',
            '.toml': 'unassigned',
            '.xml': 'unassigned',
        }

        # Load language parsers
        self.languages = {
            'py_parser': PyParser(root_dir=self.root_dir),
            'html_parser': HtmlParser(root_dir=self.root_dir),
        }

        # Update extension assignments based on each parser's supported extensions
        self._update_extension_assignments()

    def _update_extension_assignments(self) -> None:
        """Internal method to update extension assignments based on available parsers.

        Raises:
            ValueError: If an extension is already assigned to a different parser.
        """
        for parser_key, parser in self.languages.items():
            for ext in parser.extensions:
                ext_lower = ext.lower()
                if ext_lower not in self.extension_assignments:
                    logger.info(
                        "Extension '%s' is not recognized and will be added to the extensions.",
                        ext_lower,
                    )
                    self.extension_assignments[ext_lower] = 'unassigned'

                if self.extension_assignments[ext_lower] == 'unassigned':
                    self.extension_assignments[ext_lower] = parser_key
                    logger.debug("Assigned extension '%s' to parser '%s'.", ext_lower, parser_key)
                elif self.extension_assignments[ext_lower] != parser_key:
                    logger.error(
                        "Extension '%s' is already assigned to parser '%s'. "
                        "Cannot assign to parser '%s'.",
                        ext_lower,
                        self.extension_assignments[ext_lower],
                        parser_key,
                    )
                    error_message = (
                        f"Extension '{ext_lower}' is already assigned to parser "
                        f"'{self.extension_assignments[ext_lower]}'."
                    )
                    raise ValueError(error_message)
                else:
                    logger.debug(
                        "Extension '%s' is already assigned to parser '%s'.",
                        ext_lower,
                        parser_key,
                    )

    def generate_file_context(self, file_path: Path, context_level: str) -> str:
        """Given a single file_path and context_level ('full' or 'slim'), generate text context.

        Returns a string with the header + the file's context.

        Args:
            file_path (Path): The path to the file to parse.
            context_level (str): The context level, either 'full' or 'slim'.

        Returns:
            str: The generated context as a string.
        """
        # Common header for all file types
        header_lines = generate_context_header(file_path, self.root_dir)

        # Decide how to parse the file
        extension = file_path.suffix.lower()
        context = ''
        try:
            parser_key = self.extension_assignments.get(extension, 'unassigned')
            if parser_key != 'unassigned':
                parser = self.languages.get(parser_key)
                if parser:
                    if context_level == 'slim' and hasattr(parser, 'generate_slim_context'):
                        context = parser.generate_slim_context(
                            file_path.read_text(encoding='utf-8', errors='replace'),
                            file_path,
                        )
                    elif context_level == 'full' and hasattr(parser, 'generate_full_context'):
                        context = parser.generate_full_context(
                            file_path.read_text(encoding='utf-8', errors='replace'),
                            file_path,
                        )
                    else:
                        # Fallback to reading the entire file
                        file_text = file_path.read_text(encoding='utf-8', errors='replace')
                        context = '\n'.join([*header_lines, file_text])
                else:
                    logger.warning(
                        "Parser '%s' not found for extension '%s'. Falling back to full read.",
                        parser_key,
                        extension,
                    )
                    file_text = file_path.read_text(encoding='utf-8', errors='replace')
                    context = '\n'.join([*header_lines, file_text])
            else:
                # Handle unassigned extensions
                logger.debug(
                    "No specific parser assigned for extension '%s'. Reading entire file.",
                    extension,
                )
                file_text = file_path.read_text(encoding='utf-8', errors='replace')
                context = '\n'.join([*header_lines, file_text])

        except (UnicodeDecodeError, FileNotFoundError, PermissionError) as e:
            logger.warning('Skipping file due to read error %s: %s', file_path, e)
            context = ''  # or return just a header plus warning message

        return context

    def generate_repo_context(self, file_paths: list[Path], context_level: str) -> str:
        """Walk multiple files, gather all contexts, and combine them.

        Returns:
            str: The combined context of all files as a single string.
        """
        all_contexts = []
        for fp in file_paths:
            context = self.generate_file_context(fp, context_level)
            if context:
                all_contexts.append(context)

        return '\n'.join(all_contexts)
