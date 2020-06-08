#!/usr/bin/env python3

import sys
import argparse



class ParseArguments():

    def parse(self, args=sys.argv[1:]):
    	print("parse")
    	parser = argparse.ArgumentParser()

    	parser.add_argument("--id")
    	parser.add_argument("--registrar")
    	parser.add_argument("--realm")
    	parser.add_argument("--username")
    	parser.add_argument("--password")
    	parser.add_argument("--contact")
    	parser.add_argument("--outbound")
    	parser.add_argument("--thread-cnt")
    	parser.add_argument("--nameserver", action="append")
    	parser.add_argument("--publish", action="store_true") # arg
    	parser.add_argument("--clock-rate")
    	parser.add_argument("--add-codec")
    	parser.add_argument("--dis-codec", action="append")
		parser.add_argument("--client")
		parser.add_argument("--client2")

    	options = parser.parse_args(args)
    	return options


def main():
	print("def")
	p = ParseArguments()
	args = p.parse()

	print(args)
	print(args.nameserver)


if __name__ == '__main__':
	main()