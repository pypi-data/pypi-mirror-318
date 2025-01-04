"""Main entry point for the SlimContext project.

This script extracts project structure from a Git repository and generates context for an LLM
model.

Copyright (c) 2024 Neil Schneider
"""

import sys
from pathlib import Path

import click

from slimcontext.parsers.parser import ProjectParser
from slimcontext.utils.gitrepo_tools import GitRepository
from slimcontext.utils.logger import setup_logger
from slimcontext.utils.token_counter import TokenCounter

# Initialize a global logger
logger = setup_logger(__name__)


def initialize_git_repo(repo_path: Path) -> GitRepository:
    """Initialize a Git repository object.

    Args:
        repo_path (Path): Path to the Git repository.

    Returns:
        GitRepository: Initialized Git repository object.
    """
    try:
        return GitRepository(repo_dir=repo_path)
    except ValueError:
        logger.exception('Error initializing Git repository.')
        sys.exit(1)
    except Exception:
        logger.exception('Unexpected error initializing Git repository.')
        sys.exit(1)


def generate_context(parser: ProjectParser, files: list[Path], context_level: str) -> str:
    """Generate the combined context from all files.

    Args:
        parser (ProjectParser): The ProjectParser instance.
        files (list[Path]): List of file paths to parse.
        context_level (str): The context level, either 'full' or 'slim'.

    Returns:
        str: The combined context.
    """
    logger.info("Generating '%s' context for %d files.", context_level, len(files))
    context = parser.generate_repo_context(files, context_level)
    logger.info('Context generation completed.')
    return context


def count_tokens(context: str, model: str) -> int:
    """Count the tokens in the given context.

    Args:
        context (str): Generated context.
        model (str): Model name for token counting.

    Returns:
        int: Total token count.
    """
    try:
        token_counter = TokenCounter(model=model)
        return token_counter.count_tokens(context)
    except Exception:
        logger.exception('Error during token counting.')
        sys.exit(1)


def write_output(context: str, output_path: Path | None) -> None:
    """Write the generated context to a file or stdout.

    Args:
        context (str): Generated context.
        output_path (Path | None): Path to the output file, or None for stdout.
    """
    if output_path:
        try:
            with output_path.open('w', encoding='utf-8') as f:
                f.write(context)
            logger.info('Context successfully written to %s', output_path)
        except Exception:
            logger.exception('Failed to write to output file: %s', output_path)
            sys.exit(1)
    else:
        sys.stdout.write(context + '\n')


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option(
    '--path',
    '-p',
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default='.',
    show_default=True,
    help='Path to the Git repository. Defaults to the current directory.',
)
@click.option(
    '--context-level',
    '-c',
    type=click.Choice(['full', 'slim'], case_sensitive=False),
    default='full',
    show_default=True,
    help="Level of context to generate. Choices are 'full' or 'slim'.",
)
@click.option(
    '--output',
    '--out',
    '-o',
    type=click.Path(file_okay=True, dir_okay=False, writable=True, path_type=Path),
    default=None,
    help='Output file path. If not provided, outputs to stdout.',
)
@click.option(
    '--token-model',
    '-t',
    type=click.Choice(['gpt-4', 'gpt-3.5-turbo', 'none'], case_sensitive=False),
    default='gpt-4',
    show_default=True,
    help=("Model name to use for token counting. Choose 'none' to skip token counting."),
)
@click.option(
    '-v',
    '--verbose',
    count=True,
    help='Increase verbosity level. Use -v for INFO and -vv for DEBUG.',
)
def main(
    path: Path,
    context_level: str,
    output: Path,
    token_model: str,
    verbose: int,
) -> None:
    """Main entry point of the script.

    Generate context from multiple files in a Git repository and save it to an output file.
    """
    # Configure logging based on verbosity
    if verbose == 0:
        log_level = 'WARNING'
    elif verbose == 1:
        log_level = 'INFO'
    else:
        log_level = 'DEBUG'

    # Reconfigure logger with the desired log level
    logger.setLevel(log_level)
    for handler in logger.handlers:
        handler.setLevel(log_level)

    logger.debug('Log level set to %s', log_level)

    logger.info('Initializing Git repository at: %s', path)
    git_repo = initialize_git_repo(path)

    # Gather files using GitRepository
    files = git_repo.get_abolute_file_paths()
    while output in files:
        files.remove(output)

    if not files:
        logger.warning('No files found to parse. Exiting.')
        sys.exit(0)

    logger.info('Total files to parse: %d', len(files))

    # Initialize ProjectParser or PyParser based on your requirement
    # Assuming you want to use ProjectParser as in the updated main.py
    parser = ProjectParser(root_dir=git_repo.get_git_root())

    # Generate context
    context = generate_context(parser, files, context_level.lower())

    if not context:
        logger.warning('No context was generated. Exiting.')
        sys.exit(0)

    # Token counting
    if token_model.lower() != 'none':
        token_count_value = count_tokens(context, token_model.lower())
        logger.info('Total tokens in context: %d', token_count_value)
        sys.stdout.write(f'Total tokens in context: {token_count_value}\n')

    # Write output
    write_output(context, output)


if __name__ == '__main__':
    main()
