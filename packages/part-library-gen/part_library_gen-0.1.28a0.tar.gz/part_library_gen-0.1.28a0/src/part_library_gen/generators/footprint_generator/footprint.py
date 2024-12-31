

class Footprint:
    def __init__(self, name):
        self.name = name
        self.width = 0
        self.height = 0
        self.pads = []
        self.top_overlay = []
        self.bottom_overlay = []
        self.assembly_top = []

    def add_pad(self, pad):
        if isinstance(pad, list):
            self.pads += pad
        else:
            self.pads.append(pad)

    def add_overlay(self, overlay):
        if isinstance(overlay, list):
            self.top_overlay += overlay
        else:
            self.top_overlay.append(overlay)

    def to_dict(self):
        return {
            'name': self.name,
            'width': self.width,
            'height': self.height,
            'pads': [x.to_dict() for x in self.pads],
            'top_overlay': [x.to_dict() for x in self.top_overlay],
            'bottom_overlay': [x.to_dict() for x in self.bottom_overlay],
            'assembly_top': [x.to_dict() for x in self.assembly_top]
        }

    def form_dict(self, data):
        self.name = data['part_number']
        self.width = data['width']
        self.height = data['height']
        self.pads = data['pads']
        self.top_overlay = data['top_overlay']
        self.bottom_overlay = data['bottom_overlay']
        self.assembly_top = data['assembly_top']
