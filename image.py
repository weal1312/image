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

		img_l = self.img.crop(0, 0, dest_width, self.dest_height)
		img_r = self.img.crop(dest_width, 0, self.width, self.dest_height)

		img_l.save(os.path.join(self.dest_dir, self.filename + '_2.png'))
		img_r.save(os.path.join(self.dest_dir, self.filename + '_1.png'))