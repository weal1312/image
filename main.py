import argparse
import os
from image import IMG

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('mod', help='define the type image process(crop|split)')
	parser.add_argument('-i', '--input', help='define the input path')
	parser.add_argument('-o', '--output', help='define the output path')
	args = parser.parse_args()

	method = args.mod
	source_dir = args.input if args.input else 'E:\\Downloads\\temp'
	dest_dir = args.output if args.output  else os.path.join(source_dir, 'output')
	os.makedirs(dest_dir, exist_ok=True)

	for path in [os.path.join(source_dir, file) for file in os.listdir(source_dir) if file.endswith('png')]:
		getattr(IMG(path, dest_dir), method)()