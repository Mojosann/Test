from imp import reload
import os, sys, time
from functools import partial
from pprint import pprint

import third_party_test_core
reload(third_party_test_core)

import third_party_test_ui
reload(third_party_test_ui)

class ThirdPartyTestTool(object):
	def __init__(self):

		self.ffmpeg = "Z:/dev/bin/ffmpeg_5.0/ffmpeg.exe"
		# ffmpeg = "Z:/dev/bin/ffmpeg_ess/ffmpeg.exe"
		self.ffprobe = "Z:/dev/bin/ffmpeg_ess/ffprobe.exe"

		mov_path = "Z:/dev/tools/standalone/third_party_test/sq1401_sh0110.mov"
		jpg_path = "Z:/dev/tools/standalone/third_party_test/sequence_output/jpg_output/sq1401_sh0110_%04d.jpg"
		png_path = "Z:/dev/tools/standalone/third_party_test/sequence_output/png_output/sq1401_sh0110_%04d.png"
		exr_path = "Z:/dev/tools/standalone/third_party_test/exr_source/test_%04d.exr"

		##### output_path should exist first
		output_jpg_path = "Z:/dev/tools/standalone/third_party_test/sequence_output/png_to_jpg_quality_2/sq1401_sh0110_%04d.jpg"
		output_mov_path = "Z:/dev/tools/standalone/third_party_test/sequence_output/mov_output/all_form_jpg.mov"
		output_png_path = "Z:/dev/tools/standalone/third_party_test/sequence_output/png_output/sq1401_sh0110_%04d.png"

		self.ui   = third_party_test_ui.BatchFileConverterUI()
		self.core = third_party_test_core.ThirdPartyTestCore()

		# self.ui.export_button_signal.connect(partial(self.export_file_command))
		# self.ui.export_button_signal.connect(partial(self.export_batch_file_command))


	def export_file_command(self, data_dict={}):

		pprint(data_dict)

		##### get data
		input_dict = {}
		input_dict['set_frame_range'] = data_dict.get('set_frame_range')
		input_dict['start_frame'] = data_dict.get('start_frame')
		input_dict['source_file'] = data_dict.get('source_file')
		input_dict['target_file'] = data_dict.get('target_file')
		input_dict['target_ext']  = data_dict.get('target_ext')

		
		format_type = self.core.get_source_file_metadata(self.ffprobe, input_dict['source_file'])
		
		fps = None
		start_frame = None
		##### mov to jpg
		if 'MOV' in format_type:
			fps = self.core.get_mov_fps()

		if input_dict['target_ext'] == '.jpg' or '.png':
			if input_dict['set_frame_range']:
				start_frame = input_dict['start_frame']	

			self.core.convert_to_image_file(self.ffmpeg, input_dict['source_file'], input_dict['target_file'], fps, start_frame)
		# # converter.convert_to_image_file(ffmpeg, output_png_path, output_jpg_path) ##### qscale=1, 1000 KB | qscale=2, 500 KB
		
		##### to mov
		if input_dict['target_ext'] == '.mov':
			self.core.convert_to_mov_file(self.ffmpeg, input_dict['source_file'], input_dict['target_file'])

		# sys.exit()
	
	def export_batch_file_command(self, data_dict={}):

		# pprint(data_dict)
		##### get data
		input_dict = {}
		for convert_info in data_dict.values():

			source_file = convert_info.get('source_file')
			target_file = convert_info.get('target_file')
			progressbar	= convert_info.get('progress')
			
			set_frame   = convert_info.get('set_frame_range')
			if set_frame:
				start_frame = convert_info.get('start_frame')
			
			format_type = self.core.get_source_file_metadata(self.ffprobe, source_file)
			
			fps = None
			##### mov to jpg
			if 'MOV' in format_type:
				fps = self.core.get_mov_fps()

			if os.path.splitext(target_file)[1] == '.jpg' or '.png':
				self.core.convert_to_image_file(self.ffmpeg, source_file, target_file, fps, start_frame)
				# for i in range(100):
				# 	time.sleep(0.01)
				# 	progressbar.setValue(i+1)

def main():

	tool = ThirdPartyTestTool()
	return tool.ui