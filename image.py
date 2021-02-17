import argparse
import os
from PIL import Image


class IMG:
	def __init__(self, source_path, dest_dir):
		self.img = Image.open(source_path)
		self.width, self.height = self.img.size
		self.dest_dir = dest_dir
		self.filename = os.path.basename(source_path)

	def crop(self):
		dest_height = self.width / 3 * 4
		margin_y = (self.height - dest_height) / 2

		region = self.img.crop((0, margin_y, self.width, dest_height + margin_y))
		region.save(os.path.join(self.dest_dir, self.filename))

	def split(self):
		dest_width = self.width / 2

		img_l = self.img.crop((0, 0, dest_width, self.height))
		img_r = self.img.crop((dest_width, 0, self.width, self.height))

		img_l.save(os.path.join(self.dest_dir, self.filename + '_2.png'))
		img_r.save(os.path.join(self.dest_dir, self.filename + '_1.png'))


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