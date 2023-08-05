# Fine tuning of cap dimensions
It is possible that different printers give different tolerance. A fine adjusting of the diametere might be required. This folder includes a range of diameters that should fit any rotor.

## Script to generate range of diameters

In fusion 360, go to tools > add-in > script and add-ins. Create new python script with content of Param_stl_generator.py. Edit the parameters in the fil:
- paramNAme: variable being varied
- folder: folder where to save the stl
- file: File name
- start: start dimension (diameter in my files), in mm
- end: end dimension (diameter in my files) in mm
-step: step in mm

Then run script.
