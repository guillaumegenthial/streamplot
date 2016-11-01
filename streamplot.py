import sys
import time
import collections
import numpy as np
try:
	import pyqtgraph as pg
	from pyqtgraph.Qt import QtGui, QtCore
	pg.setConfigOption('background', 'w')
except Exception, e:
	print "Unable to import pyqtgraph"

class LivePlotter(object):
	"""
	Creates instance of QT app for plotting
	Defines usefull methods to update data and plot

	# Attributes
		frequency (float): time in second, minimum time between two updates
		downsample (integer): downsampling parameter, unused in this version
		size (tuple of integers): size of the window

	# Methods
		add(x,y): adds data to plot data
		update(): update the plot
	"""
	def __init__(self, **kwargs):

		self.name = kwargs.get("name", "live_plotter")
		self.frequency = kwargs.get("frequency", 0.1)
		self.downsample = kwargs.get("downsample", 10)
		self.point_nb = kwargs.get("point_nb", 100)
		self.size = kwargs.get("size", (600, 300))
		self.pen = kwargs.get("pen", "r")
		self.x_axis = kwargs.get("x_axis", "x")
		self.y_axis = kwargs.get("y_axis", "y")
		self.x_unit = kwargs.get("x_unit", "t")
		self.y_unit = kwargs.get("y_unit", "")

		self.last_refresh = time.time()

		self.x, self.y = [], []

		try:
			self.win = kwargs.get("win", pg.GraphicsWindow().resize(self.size[0], self.size[1]))
			self.p = self.win.addPlot(title=self.name)
			self.p.setLabel('left', self.y_axis, units=self.y_unit)
			self.p.setLabel('bottom', self.x_axis, units=self.x_unit)
			self.plot = self.p.plot(self.x, self.y, pen=self.pen)
		except Exception, e:
			print "Unable to initialize Live Plotter"


	def add(self, y, x=None):
		"""
		Adds data to the plot
		If x is None, will take time for x axis
		"""
		if x is None:
			x = time.time()
		self.x += [x]
		self.y += [y]

	def update(self):
		"""
		After having added data to the graph data, calling update updates the plot
		"""
		try:
			t = time.time()
			frequency = self.frequency
			last_refresh = self.last_refresh
			downsample = self.downsample
			point_nb = self.point_nb

			if frequency is not None:
				if t - last_refresh < frequency:
					return

			if point_nb is not None:
				x_size = len(self.x)
				downsample = x_size / point_nb
			
			# self.plot.setData(self.x, self.y, downsample=downsample)
			self.plot.setData(self.x, self.y)
			pg.QtGui.QApplication.processEvents()
			self.last_refresh = t

		except Exception, e:
			pass

	def close(self):
		"""
		Closes the window
		"""
		try:
			self.win.close()
		except Exception, e:
			pass

class PlotManager(object):
	"""
	General class to handle multiple variable plotting in the same window

	# Attributes
		title (string): title of the window
		size (tuple of integers): size of the window
		nline (integer): number of plots for each line of the window, default 3
		frequency (float): see LivePlotter
		plots (OrderedDict of LivePlotter instances): where the plots are

	# Example
		length = 10000
		costs  = np.arange(length)

		plt_mgr = PlotManager(
			title="plots", 
			nline=3)

		for i in range(length):
			cost = costs[i]
			plt_mgr.add("cost", cost)
			plt_mgr.add("time", time.time())
			plt_mgr.add("time2", time.time())
			plt_mgr.update()

		plt_mgr.close()

	"""
	def __init__(self, **kwargs):
		self.title = kwargs.get("title", "Plots")
		self.size = kwargs.get("size", (800, 400))
		self.nline = kwargs.get("nline", 3)
		self.frequency = kwargs.get("frequency", 0.1)
		self.downsample = kwargs.get("downsample", 10)
		self.point_nb = kwargs.get("point_nb", 100)
		self.nplots = -1

		try:
			self.plots = collections.OrderedDict()
			self.win = pg.GraphicsWindow(title=self.title)
			self.win.resize(self.size[0], self.size[1])
		except Exception, e:
			print "Unable to initialize Plot Manager"

	def add(self, name, y, x=None, **kwargs):
		"""
		Adds data x, y to the data of the variable with name name.
		"""
		try:
			if name not in self.plots:
				self.nplots += 1
				if self.nplots % self.nline == 0:
					self.win.nextRow()

				self.plots[name] = LivePlotter(
					name=name, 
					win=self.win, 
					frequency=self.frequency,
					downsample=self.downsample,
					point_nb=self.point_nb,
					**kwargs)

			self.plots[name].add(y, x)
		except Exception, e:
			pass

	def update(self):
		"""
		Updates all subplots
		"""
		for name, plot in self.plots.iteritems():
			plot.update()

	def close(self):
		"""
		Close window from Terminal
		"""
		try:
			wait = input("Press ENTER to close plots")
		except Exception, e:
			pass
		for name, plot in self.plots.iteritems():
			plot.close()