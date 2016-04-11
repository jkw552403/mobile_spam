"""
This is a script to scrap all articles posted from 2(default) days ago.
"""
import argparse

from bs4 import BeautifulSoup
import pandas as pd
import requests


def parse_table(html_body):
    pass


def parse_article(html_body):
    pass


def main(board_name, sql, time):
    # TODO check if sql exixts or not
    # TODO exist => load last article we scrap
    last_article = pd.read_sql('SELECT FROM ')
    # TODO doesn't exist => last_article = None
    # and scrap all the articles!!!

    # from first table page, get all month and day to decide scrap them or not
    # if too new, find next page to check month and day

    # if we find the page from 2 days ago and we haven't downloaded yet
    # then starting from this page, to download every articles newer than the last article
    

    html_body = requests.get(url, cookies={'over18': '1'},
                             verify=False, allow_redirects=True).text

    while

    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('board_name', help='Board name which you want to scrap')
    parser.add_argument('sql', help='The SQLite file you want to save')
    parser.add_argument('-d', '--day', type=int, default=2, help='Waiting time between two requests')
    parser.add_argument('-t', '--time', type=int, default=2, help='Waiting time between two requests')

    args = parser.parse_args()

    main(args.board_name, args.output, args.day, args.time)
