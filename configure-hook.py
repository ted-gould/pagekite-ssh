#!/usr/bin/env python3

import subprocess
import sys


def main():
	user = subprocess.check_output(['snapctl', 'get', 'pagekite-user']).decode('utf8').strip()
	secret = subprocess.check_output(['snapctl', 'get', 'pagekite-secret']).decode('utf8').strip()

	if not user:
		print "User not set"
		sys.exit(1)
	if not secret:
		print "Secret not set"
		sys.exit(1)

	configline = "service_on=raw/22:%s.pagekite.me:localhost:22:%s" % (user, secret)

	with open(sys.getenv("SNAP_DATA") + "/pagekite.rc", "w") as config_file:
		config_file.write(configline)
		config_file.write("\n")

	print("I'm the configure hook!")

if __name__ == '__main__':
	main()
