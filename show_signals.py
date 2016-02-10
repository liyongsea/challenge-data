# -*- coding: utf-8 -*-
"""
Cardiologs Technologies
All rights reserved
Created on Thu Nov 19 18:01:48 2015
"""

from matplotlib import pyplot as plt
import matplotlib.ticker as plticker
import numpy as np


def plot_data(data):
    # make sure it is an np.array of dimension 1
    data = np.array(data)
    np.testing.assert_equal(data.ndim, 1, "Please input only vectors. Use 'flatten' on your np.array if need be.")

    def _make_lead_data(data):
        "Cut the data into lead signals"
        leadnames = ['MLI', 'MLII', 'MLIII', 'AVL', 'AVR', 'AVF',
                     'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
        length = 750
        start = 0
        for name in leadnames:
            yield (name, data[start: start + length])
            start += length

    def _plot_data(lead_data):
        "Plot the data from lead signals"
        # time
        time = np.linspace(0, 3, 750)
        # ticks location
        loc_x = plticker.MultipleLocator(base=1.0)
        for k, (name, signal) in enumerate(lead_data):
            # get index in standard order and get subplot
            output = np.unravel_index(k, (3, 4), order='F')
            index = np.ravel_multi_index(output, (3, 4), mode='raise', order='C')
            axis = plt.subplot(3, 4, index + 1)
            # ticks location and decorum
            axis.spines["top"].set_visible(False)
            axis.spines["right"].set_visible(False)
            axis.tick_params(axis='x', direction='out')
            axis.tick_params(axis='y', direction='out')
            axis.get_xaxis().tick_bottom()
            axis.get_yaxis().tick_left()
            axis.xaxis.set_minor_locator(loc_x)
            # plots
            plt.plot(time, 0 * time, "--", color="black", lw=2)
            plt.plot(time, signal, color="blue")
            # lead name
            plt.title(name)
    # convert to lead signals
    lead_data = _make_lead_data(data)
    # plot data
    _plot_data(lead_data)

