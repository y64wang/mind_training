#!/usr/bin/env python3
""" This script build l1sw-env docker image.
    version: docker version to be built
    path: path to Dockerfile
    -s: to add sudo before docker build

    The host http_proxy/https_proxy/no_proxy env variables are automatically inherited

Usage: python3 build.py version path [-s]
"""

import argparse
import os
import shutil
import subprocess
import sys

ARTIFACTORY_REPO='l1sw-docker-local.artifactory-espoo2.int.net.nokia.com/l1sw-env:'

def build_docker_command(version, path, sudo=False):
    cmd = ['docker', 'build']

    if not os.path.isfile(os.path.join(path, 'Dockerfile')):
        print('Error: Dockerfile does not exist in ', path)
        sys.exit(2)
    if sudo:
        cmd = ['sudo'] + cmd

    if r'http_proxy':
        cmd += ['--build-arg http_proxy=$http_proxy']
    if r'https_proxy':
        cmd += ['--build-arg https_proxy=$https_proxy']
    if r'no_proxy':
        cmd += ['--build-arg no_proxy=$no_proxy']

    cmd += ['-t', ARTIFACTORY_REPO+version, path]

    return cmd

def parse_arg():
    arg_parser = argparse.ArgumentParser(
                        description='This script build l1sw-env docker image.',
                        epilog='''The host proxy environment variables (http_proxy/https_proxy/no_proxy)
                                are automatically inherited into docker building.''',
                        add_help=True)
    arg_parser.add_argument('version', nargs=1, help='docker version to be built')
    arg_parser.add_argument('path', nargs=1, help='path to Dockerfile')
    arg_parser.add_argument('-s', '--sudo', action='store_true', default=False, help='sudo enabled for docker build')

    args = arg_parser.parse_args()

    version = str(args.version[0])
    path = str(args.path[0])

    sudo = False;
    if args.sudo:
        sudo=args.sudo

    return version, path, sudo

def main():
    version = ''
    path = '.'
    sudo = False

    version, path, sudo = parse_arg()
    command = build_docker_command(version, path, sudo)
    return subprocess.check_call(' '.join(command), shell=True, executable=shutil.which('bash'))

if __name__ == "__main__":
    sys.exit(main())
