import numpy as np

"""
Probability of each infection serverity by age

Source: Imperial College Covid-19 research team
"""

age_hospitalization_probs = [0.001, 0.003, 0.012, 0.032, 0.049, 0.102, 0.166, 0.243, 0.273]
age_severe_probs = [0.05, 0.05, 0.05, 0.05, 0.063, 0.122, 0.274, 0.432, 0.709]
age_death_probs = [0.00002, 0.00006, 0.0003, 0.0008, 0.0015, 0.006, 0.022, 0.051, 0.093]

## Citar fontes

"""
Wealth distribution - Lorenz Curve

By quintile, source: https://www.worldbank.org/en/topic/poverty/lac-equity-lab1/income-inequality/composition-by-quintile
"""

lorenz_curve = [.04, .08, .13, .2, .56]
share = np.min(lorenz_curve)
basic_income = np.array(lorenz_curve) / share

"""
Discrete Normal Distributions: Time for Infection State Transition 
    (i.e.: average time that the agent will REMAIN in the state)
"""
# TODO: Change values accordingly!
min_asymptomatic_days = 1

mean_asymptomatic_spreading = 2.5  # https://www.bmj.com/content/bmj/369/bmj.m1435.full.pdf
sd_asymptomatic_spreading = 0.5
min_asymptomatic_spreading_days = 1

mean_total_incubation = 6.4  # https://www.worldometers.info/coronavirus/coronavirus-incubation-period/
sd_total_incubation = 1.8  # ranges roughly from 2 to 11


def discrete_normal(mean, sd):
    return np.int(np.random.normal(mean, sd))


def generate_infection_evolution_timestamps(minimum_asymptomatic_days,
                                            mean_asymptomatic_spreading_dist,
                                            sd_asymptomatic_spreading_dist,
                                            minimum_asymptomatic_spreading_days,
                                            mean_total_incubation_dist,
                                            sd_total_incubation_dist):
    # Number of days in asymptomatic spreading state: truncated discrete normal distribution
    asymptomatic_spreading_days = max(discrete_normal(mean_asymptomatic_spreading_dist,
                                                      sd_asymptomatic_spreading_dist),
                                      minimum_asymptomatic_spreading_days)

    # Total number of days from infection to symptomatic
    total_incubation_days = max(discrete_normal(mean_total_incubation_dist, sd_total_incubation_dist),
                                (minimum_asymptomatic_days + asymptomatic_spreading_days))

    asymptomatic_spreading_timestamp = total_incubation_days - asymptomatic_spreading_days

    return asymptomatic_spreading_timestamp, total_incubation_days
