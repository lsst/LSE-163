#!/usr/bin/env python
"""Create a website from LSE-163 to deploy on LSST the Docs."""

import io
import os
import shutil
import datetime
from argparse import ArgumentParser

import jinja2


def main():
    args = parse_args()

    if not os.path.exists(args.build_dir):
        os.makedirs(args.build_dir)

    shutil.copyfile(args.source_pdf_path,
                    os.path.join(args.build_dir,
                                 os.path.basename(args.source_pdf_path)))

    render_template(args.template_path, args.build_dir)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        '--template',
        dest='template_path',
        required=True,
        help='Path to the jinja2 HTML template')
    parser.add_argument(
        '--pdf',
        dest='source_pdf_path',
        required=True,
        help='Path to built LSE-163 PDF file')
    parser.add_argument(
        '--build-dir',
        dest='build_dir',
        required=True,
        help='Directory to build website in')
    return parser.parse_args()


def render_template(template_path, build_dir):
    with io.open(template_path, 'r', encoding='utf-8') as f:
        t = jinja2.Template(f.read())

    template_vars = {
        'build_date': datetime.datetime.now().isoformat() + 'Z'
    }

    if os.getenv('TRAVIS_BRANCH'):
        template_vars['branch'] = os.getenv('TRAVIS_BRANCH')

    html = t.render(**template_vars)

    html_path = os.path.join(build_dir, 'index.html')
    with io.open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    main()
