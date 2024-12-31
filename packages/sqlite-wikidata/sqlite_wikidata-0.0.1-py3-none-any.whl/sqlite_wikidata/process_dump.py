import click

from sqlite_wikidata.build_index import build_index
from sqlite_wikidata.db import connect, init_wikidata, add_wikidata_dump_folder


@click.group()
def app():
    pass


@app.command(name='process-dump')
@click.option('--db', 'd', 'sqlite_path', help='Path to the SQLite database')
@click.option('--path', 'p', 'wikidata_path', help='Path to the wikidata dump')
def process_dump(sqlite_path, wikidata_path):
    """process dump"""
    connect(sqlite_path)
    init_wikidata()
    add_wikidata_dump_folder(wikidata_path)


@app.command(name='index-db')
@click.option('--db', 'd', 'sqlite_path', help='Path to the SQLite database')
def index_db(sqlite_path):
    """process dump"""
    build_index(sqlite_path)


if __name__ == '__main__':
    app()
