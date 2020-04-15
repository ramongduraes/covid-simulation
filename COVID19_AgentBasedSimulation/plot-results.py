import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import animation, rc
from IPython.display import HTML

from covid_abs.agents import *
from covid_abs.abs import *
from covid_abs.common import *
from covid_abs.experiments import *
from covid_abs.graphics import *

sim = Simulation(
    # Percentage of infected in initial population
    initial_infected_perc = 0.02,
    # Percentage of immune in initial population
    initial_immune_perc = 0.01,
    # Length of simulation environment
    length=100,
    # Height of simulation environment
    height=100,
    # Size of population
    population_size=80,
    # Minimal distance between agents for contagion
    contagion_distance=5.,
    # Maximum percentage of population which Healthcare System can handle simutaneously
    critical_limit=0.05,
    # Mobility ranges for agents, by Status
    amplitudes = {
        Status.Susceptible : 5,
        Status.Recovered_Immune : 5,
        Status.Infected : 5
        }
)

anim = execute_simulation(sim, iterations=80)
rc('animation', html='html5')
anim
save_gif(anim, 'do_nothing.gif')
