import json

import click
import dataset_sh
from datafact.proj import locate_draft_file
from dataset_sh.constants import DEFAULT_COLLECTION_NAME


@click.group('preview')
def preview_cli():
    pass


@preview_cli.command('show')
@click.option('--name', '-n', type=str, default='draft', help='draft dataset.sh file name.')
@click.option('--collection', '-c', type=str, default=DEFAULT_COLLECTION_NAME, help='which collection to preview.')
def preview_collection(name, collection):
    """
    initialize a dataset factory project.
    """
    fp = locate_draft_file(name)

    def print_collection(fp):
        with dataset_sh.open_dataset_file(fp) as f:
            for item in f.collection(collection):
                yield json.dumps(item, indent=2) + '\n'

    click.echo_via_pager(print_collection(fp))


@preview_cli.command('collections')
@click.option('--name', '-n', type=str, default='draft', help='draft dataset.sh file name.')
def list_collections(name):
    """
    initialize a dataset factory project.
    """
    fp = locate_draft_file(name)

    with dataset_sh.open_dataset_file(fp) as f:
        cs = f.collections()
        click.secho(f'Find {len(cs)} collections:', fg='yellow')
        for idx, c in enumerate(cs):
            click.secho(f'  {idx + 1:02}: {c}')
