from collections import namedtuple

import matplotlib as mpl
import pytest

import time_series_visualizer


@pytest.fixture(scope='module')
def line_plot_ax():
    fig = time_series_visualizer.draw_line_plot()
    return fig.axes[0]


@pytest.fixture(scope='module')
def bar_plot_ax():
    fig = time_series_visualizer.draw_bar_plot()
    return fig.axes[0]


@pytest.fixture(scope='module')
def box_plot():
    BoxPlot = namedtuple("BoxPlot", 'fig ax1 ax2')
    fig = time_series_visualizer.draw_box_plot()
    box_plot = BoxPlot(fig, fig.axes[0], fig.axes[1])
    return box_plot


def test_data_cleaning():
    actual = int(time_series_visualizer.df.count(numeric_only=True))
    expected = 1238
    assert actual == expected, "Expected DataFrame count after cleaning to be 1238."


def test_line_plot_title(line_plot_ax):
    actual = line_plot_ax.get_title()
    expected = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    assert actual == expected


def test_line_plot_labels(line_plot_ax):
    xlabel = line_plot_ax.get_xlabel()
    ylabel = line_plot_ax.get_ylabel()
    assert xlabel == "Date"
    assert ylabel == "Page Views"


def test_line_plot_data_quantity(line_plot_ax):
    actual = len(line_plot_ax.lines[0].get_ydata())
    expected = 1238
    assert actual == expected


def test_bar_plot_legend_labels(bar_plot_ax):
    actual = [label.get_text() for label in bar_plot_ax.get_legend().get_texts()]
    expected = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                'November', 'December']
    assert actual == expected


def test_bar_plot_labels(bar_plot_ax):
    xlabel = bar_plot_ax.get_xlabel()
    ylabel = bar_plot_ax.get_ylabel()
    labels = [label.get_text() for label in bar_plot_ax.get_xaxis().get_majorticklabels()]

    assert xlabel == "Years"
    assert ylabel == "Average Page Views"
    assert labels == ['2016', '2017', '2018', '2019']


def test_bar_plot_number_of_bars(bar_plot_ax):
    rectangles = len([rect for rect in bar_plot_ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
    assert rectangles == 49


def test_box_plot_number(box_plot):
    assert len(box_plot.fig.get_axes()) == 2


def test_box_plot_labels(box_plot):
    ax1_xlabels = [label.get_text() for label in box_plot.ax1.get_xaxis().get_majorticklabels()]
    ax1_ylabels = [label.get_text() for label in box_plot.ax1.get_yaxis().get_majorticklabels()]
    ax2_xlabesls = [label.get_text() for label in box_plot.ax2.get_xaxis().get_majorticklabels()]

    assert box_plot.ax1.get_xlabel() == "Year"
    assert box_plot.ax1.get_ylabel() == "Page Views"
    assert box_plot.ax2.get_xlabel() == "Month"
    assert box_plot.ax2.get_ylabel() == "Page Views"
    assert ax1_xlabels == ['2016', '2017', '2018', '2019']
    assert ax2_xlabesls == ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    assert ax1_ylabels == ['0', '20000', '40000', '60000', '80000', '100000', '120000', '140000', '160000', '180000', '200000']


def test_box_plot_titles(box_plot):
    assert box_plot.ax1.get_title() == "Year-wise Box Plot (Trend)"
    assert box_plot.ax2.get_title() == "Month-wise Box Plot (Seasonality)"


def test_box_plot_number_of_boxes(box_plot):
    ax1_boxes = len(box_plot.ax1.lines) / 6
    ax2_boxes = len(box_plot.ax2.lines) / 6
    assert ax1_boxes == 4
    assert ax2_boxes == 12
