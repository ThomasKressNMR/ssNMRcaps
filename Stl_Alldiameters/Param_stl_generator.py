# Generate STL files by modifying a parameter

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
	ui = None
	try:
		paramName = 'var'
		folder = '/Users/user/3dprints/Fusion360'
		
	  file = '4mm_'
		start = 2.8
	  end = 3.2
		step = 0.025
	

		app = adsk.core.Application.get()
		ui  = app.userInterface
		design = app.activeProduct
		param = design.userParameters.itemByName(paramName)

		reset_value = param.expression
        
		value = start
		while (value <= end):
			valueStr = "{:.3f}".format(value)
			param.expression = valueStr

			exportMgr = design.exportManager
            
            # Export STL file.
			stlOptions = exportMgr.createSTLExportOptions(design.rootComponent, folder + '/' + file + valueStr + '.stl')
			exportMgr.execute(stlOptions)
			
			value += step

		param.expression = reset_value
	except:
		if ui:
			ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
