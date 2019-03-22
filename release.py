#!/usr/bin/env python

# This script is licensed on Creative Commons Zero (CC0).
# See: https://creativecommons.org/publicdomain/zero/1.0/


import os, shutil, sys

from py			import pyIsCompat
from py.cl		import args
from py.paths	import appendPath
from py.paths	import dir_release
from py.paths	import dir_svg
from py.paths	import file_license
from py.paths	import file_readme
from py.paths	import template_file
from py.theme	import copyTemplate
from py.theme	import getReleaseDefaultImages
from py.util	import compress
from py.util	import convertToPNG
from template	import init as generateTemplate


py_compat, py_ver = pyIsCompat()
if not py_compat:
	print('\nERROR:\tUsing Python version {}. Version 3 or greater required.'.format(py_ver))
	sys.exit(1)


if args.contains('clean'):
	# use condition to prevent IDE from organizing import
	if True: import clean

	sys.exit(clean.init(args.getValue('clean', True)))

live_run = not args.contains('dry_run')
if not live_run:
	print('\nDry run: Not making any changes ...\n')

if live_run:
	# create output directory
	os.makedirs(dir_release, exist_ok=True)

	if not args.contains('no-update-template') or not os.path.isfile(template_file):
		generateTemplate()

# default sizes (overridden with --sizes option)
sizes = ['24', '32', '64']
if args.contains('size'):
	sizes = args.getValue('size', True)

for S in sizes:
	# check that all sizes are numerical values
	try:
		int(S)
	except ValueError:
		print('\nERROR: "{}" is not a valid numerical value for argument "size".'.format(S))
		sys.exit(1)

print('\nCaching images to be converted for release ...')

release_images = getReleaseDefaultImages()
img_count = len(release_images)
idx = 0

print('{} images will be included in release.'.format(img_count))

for S in sizes:
	size_dir = appendPath(dir_release, '{}/emojitwo'.format(S))

	for img_name in release_images:
		idx += 1

		source = appendPath(dir_svg, '{}.svg'.format(img_name))
		target = appendPath(size_dir, '{}.png'.format(img_name))

		os.makedirs(size_dir, exist_ok=True)

		if os.path.isfile(target) and not args.contains('update_png'):
			sys.stdout.write('Not updating {}x{} PNG: {}                          \r'.format(S, S, img_name))
			continue

		if live_run:
			try:
				sys.stdout.write('Converting SVG to {}x{} PNG image ({}/{}) (Ctrl+C to cancel)       \r'.format(S, S, idx, img_count))
				convertToPNG(source, target, S, S)
				if not os.path.isfile(target):
					print('\nERROR: SVG->PNG conversion failed.')
					sys.exit(1)
			except KeyboardInterrupt:
				print('\nProcess cancelled by user')
				sys.exit(0)

	if live_run:
		copyTemplate(size_dir)
		shutil.copy(file_license, size_dir)
		shutil.copy(file_readme, size_dir)

# newline after converting files
print()

# create zip distribution archive
compress(not live_run)

print('\nDone!')
