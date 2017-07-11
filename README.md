# StreamPlot

Real Time Plotting in Python with pyqtgraph.
Simple to use.

<!-- MarkdownTOC -->

- Install
- Test
- Use
- Install from source

<!-- /MarkdownTOC -->


## Install

Install `pyqtgraph` following the instructions on [this webpage](http://www.pyqtgraph.org)

Use pip (install from repo, see below)
```
pip install streamplot
```

## Test

To test the install, run the `test.py` script.

```
python test.py
```

## Use

In a python code

- Import package  
```python
from streamplot import PlotManager
```
- Create instance of `PlotManager` with
```python
plt_mgr = PlotManager(title="My first plot")
```
- Send data to the plot
```python
x, y = 1, 2
plt_mgr.add(name="name_of_variable", x=x, y=y)
plt_mgr.update()
```
- If you want to plot multiple variables, do something like
```python
x1, y1 = 2, 4
plt_mgr.add(name="1", x=x1, y=y1)
plt_mgr.add(name="2", x=x2, y=y2)
plt_mgr.update()
```
- close the graphs from Terminal
```python
plt_mgr.close()
```

## Install from source

Clone repo, and run from Terminal

```
python setup.py install
```

Alternatively, if you want to modify the package and just add an egg-link to site-packages

```
python setup.py develop
```




