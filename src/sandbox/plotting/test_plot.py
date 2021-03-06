'''
Created on 19 nov. 2012

@author: localadmin
'''
import matplotlib.pyplot as plt

from expWorkbench import load_results, ema_logging
from plotting import envelopes

ema_logging.log_to_stderr(ema_logging.DEBUG)

results = load_results(r'../../test/data/1000 flu cases no policy.cPickle')

envelopes(results, 
          group_by='policy',
          density='kde',
          log=True)

plt.show()