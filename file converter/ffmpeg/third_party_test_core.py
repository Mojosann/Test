import os, sys, json, subprocess, time
from pprint import pprint

class ThirdPartyTestCore(object):

	def __init__(self):
		self.metadata = {}

	def get_source_file_metadata(self, third_party, source_file):
		
		##### get metadata dict
		content_list = []
		content_list.append(third_party)
		content_list.append('-print_format')
		content_list.append('json')
		content_list.append('-show_streams')
		content_list.append('-show_format')
		content_list.append(source_file)

		##### os method
		# metadata = os.popen(' '.join(content_list))
		# self.metadata = json.loads(metadata.read())

		##### subprocess method
		metadata = subprocess.Popen(' '.join(content_list), shell=True, stdout=subprocess.PIPE)
		self.metadata = json.loads(metadata.stdout.read())	

		##### only get format type		
		format_type = self.metadata['format']['format_long_name']
		return format_type

	def get_mov_fps(self):		

		##### get fps
		fps = 0
		for item in self.metadata['streams']:
			if item.get('r_frame_rate'):
				if int(item['r_frame_rate'].split('/')[0]) > 0:
					fps = int(item['r_frame_rate'].split('/')[0])
		return fps

	def convert_to_image_file(self, third_party, source_file, output_file, fps=None, start_frame=None):
		
		##### get convert data
		convert_info_list = []
		convert_info_list.append(third_party)
		convert_info_list.append('-i')
		convert_info_list.append(source_file)

		if os.path.basename(source_file).split('.')[1] == 'mov':
			convert_info_list.append('-vf')

		if fps:
			convert_info_list.append('fps=%s' % fps)
		
		if start_frame:
			convert_info_list.append('-start_number')
			convert_info_list.append('%s' % start_frame)

		##### convert to jpg and keep quality
		if os.path.basename(output_file).split('.')[1] == 'jpg':
			# convert_info_list.append('-qscale:v 2')   ##### 500 KB
			convert_info_list.append('-qscale:v 1') ##### 1000 KB
			convert_info_list.append('-qmin 1')

		##### convert to png: 13,000 KB
		if os.path.basename(output_file).split('.')[1] == 'png':
			convert_info_list.append('-pred')
			convert_info_list.append('mixed')
			convert_info_list.append('-compression_level')
			convert_info_list.append('0') # 100

		convert_info_list.append(output_file)

		#### mov/exr convert to image
		if len(convert_info_list):
			##### os method
			# os.system(' '.join(convert_info_list))
			##### subprocess method
			subprocess.call(' '.join(convert_info_list), shell=True)

	def convert_to_mov_file(self, third_party, source_file, output_file, start_number=None, end_number=None):

		##### get convert data
		convert_info_list = []
		convert_info_list.append(third_party)
		
		if start_number:
			convert_info_list.append('-start_number')
			convert_info_list.append(str(start_number))
		
		convert_info_list.append('-i')
		convert_info_list.append(source_file)
		
		if end_number:
			convert_info_list.append('-vframes') #end_number
			convert_info_list.append(str(end_number))
		
		convert_info_list.append(output_file)

		#### jpg to mov: 2000KB
		##### os method
		# os.system(' '.join(convert_info_list)) ##### codec=h.264 cant not play in quicktime
		# set prores codec method
		# os.system('%s -f image2 -i %s -c:v prores_ks -profile:v 4 -vendor apl0 -pix_fmt yuv444p10le -s 2048x1152 -r 25 %s' % (third_party, source_file, output_file))
		##### subprocess method
		subprocess.call(' '.join(convert_info_list), shell=True)


# os.system('%s -i %s -f ffmetadata %s' % (ffmpeg, mov_path, metadata))
# os.system('%s -i %s -c copy -map_metadata 0 -map_metadata:s:v 0:s:v -f ffmetadata %s' % (ffmpeg, mov_path, metadata))
# os.system('%s -print_format json -show_format -show_streams %s > %s' % (ffprobe, mov_path, metadata))
# os.system('%s -print_format flat -select_streams 0 -show_entries stream=r_frame_rate %s' % (ffprobe, mov_path))

# content = '%s -print_format json -show_streams -show_format %s' % (third_party, source_file)
# format_type = '%s -hide_banner -loglevel fatal -show_error -show_format -print_format ini %s' % (third_party, source_file)
# fps_data = '%s -print_format flat -select_streams 0 -show_entries stream=r_frame_rate %s' % (third_party, source_file)
# os.system('%s -f image2 -i %s %s' % (third_party, source_file, output_file))