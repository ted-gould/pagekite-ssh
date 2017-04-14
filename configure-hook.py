#!/usr/bin/env python3

import subprocess
import sys


def main():
	user = subprocess.check_output(['snapctl', 'get', 'pagekite-user']).decode('utf8').strip()
	secret = subprocess.check_output(['snapctl', 'get', 'pagekite-secret']).decode('utf8').strip()

	print("I'm the configure hook!")

if __name__ == '__main__':
	main()
