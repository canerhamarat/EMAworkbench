'''
Created on 27 Jul. 2011

This file illustrated the use the EMA classes for a model in Excel.

It used the excel file provided by 
`A. Sharov <http://home.comcast.net/~sharov/PopEcol/lec10/fullmod.html>`_

This excel file implements a simple predator prey model.

.. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
'''
import matplotlib.pyplot as plt

from expWorkbench import ModelEnsemble, ParameterUncertainty,\
                         Outcome, ema_logging
from expWorkbench.excel import ExcelModelStructureInterface
from analysis.plotting import lines

class ExcelModel(ExcelModelStructureInterface):
    
    uncertainties = [ParameterUncertainty((0.01, 0.2),
                                          "K2"), #we can refer to a cell in the normal way
                     ParameterUncertainty((450,550),
                                          "KKK"), # we can also use named cells
                     ParameterUncertainty((0.05,0.15),
                                          "rP"),
                     ParameterUncertainty((0.00001,0.25),
                                          "aaa"),
                     ParameterUncertainty((0.45,0.55),
                                          "tH"),
                     ParameterUncertainty((0.1,0.3),
                                          "kk")]
    
    #specification of the outcomes
    outcomes = [Outcome("B4:B1076", time=True),  #we can refer to a range in the normal way
                Outcome("P_t", time=True)] # we can also use named range
    
    #name of the sheet
    sheet = "Sheet1"
    
    #relative path to the Excel file
    workbook = r'\excel example.xlsx'
    

if __name__ == "__main__":    
    logger = ema_logging.log_to_stderr(level=ema_logging.INFO)
    
    model = ExcelModel(r"..\..\models\excelModel", "predatorPrey")
    
    ensemble = ModelEnsemble()
    ensemble.set_model_structure(model) 

    ensemble.parallel = True #turn on parallel computing
    ensemble.processes = 2 #using only 2 cores 
    
    #generate 100 cases
    results = ensemble.perform_experiments(10) 
    
    lines(results)
    plt.show()
    
    #save results
#    save_results(results, r'..\..\excel runs.cPickle')