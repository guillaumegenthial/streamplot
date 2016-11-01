# Live Plot

Real time plots

## Install

```
python setup.py install
```

Alternatively, if you want to modify the package and just add an egg-link to site-packages

```
python setup.py develop
```


## Use

In a python code

- Import package  
```python
from liveplot import PlotManager
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


