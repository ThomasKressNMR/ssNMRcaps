# Fine tuning of cap dimensions

In fusion 360, go to tools > add-in > script and add-ins. Create new python script with content of Param_stl_generator.py. Edit the parameters in the fil:
- paramNAme: variable being varied
- folder: folder where to save the stl
- file: File name
- start: start dimension (diameter in my files), in mm
- end: end dimension (diameter in my files) in mm
-step: step in mm

Then run script.
