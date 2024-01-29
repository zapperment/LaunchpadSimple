import logging
from ableton.v3.control_surface import ControlSurface 

logger = logging.getLogger(__name__)

def extract_rgb(color_value):
	red = (color_value >> 16) & 0xFF  
	green = (color_value >> 8) & 0xFF 
	blue = color_value & 0xFF  

	return (red, green, blue)

def log(message):
	logger.info("LS_LOG " + message)

class LaunchpadSimple(ControlSurface):

	def __init__(self, *a, **k):
		(super().__init__)(*a, **k)
		song = self.song
		log("Number of tracks: " + str(len(song.tracks)))
		for track_index, track in enumerate(song.tracks):
			log("* Track " + str(track_index + 1) + " name: " + track.name)
			log("  Number of clip slots: " + str(len(track.clip_slots)))
			for clip_slot_index, clip_slot in enumerate(track.clip_slots):
				log("  * Clip slot " + str(clip_slot_index + 1) + " has clip? " + str(clip_slot.has_clip))
				if clip_slot.has_clip:
					clip = clip_slot.clip
					log("    Clip name: " + clip.name)
					log("    Color: " + str(clip.color))
					log("    Color index: " + str(clip.color_index))
					log("    Color RGB: " + str(extract_rgb(clip.color)))



