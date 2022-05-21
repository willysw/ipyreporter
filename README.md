# ipyreporter

***Pretty variable reporting in Jupyter Notebook.***

## Motivation

Create a reporter initialized with a section header:

```python
    R = Reporter("Subsection Header")
```

Add some variables to report:

```python
    # by item
    R['x_y'] = 3.142, 'm/s', 'average speed'

    # by calling
    R(k_0=(2.707, 'bar', 'pressure'), alpha=(34.0, 'deg'))

    # vectors
    R['v'] = [1, 2, 3, 4], 'km', 'a vector'
```

Display in IPython:

```python
    display(R)
```

displays (in order of insertion):

| Subsection Header | | |
| --- | --- | --- |
| average speed | $x_y$ | 3.142 m/s |
| pressure | $k_0$ | 2.707 bar |
| | $\alpha$ | 34.0 deg |
| a vector | $v$ | [1.0, 2.0, 3.0, 4.0] km |

Access variables:

```python
    >>> R['x_y']
    3.142

    >>> R.x_y
    3.142

    >>> R.v
    array([1.0, 2.0, 3.0, 4.0], dtype=float)
```

> ==Inject into local namespace?==

Save to file:

```yaml
    Subsection Header:
        x_y:
            value: 3.142
            unit: m/s
            desc: average speed
        ...
        v:
            value:
                - 1.0
                - 2.0
                - 3.0
                - 4.0
            unit: km
            desc: a vector
        ...
```

## Alternates

### Alternate Display in LaTeX

```python
    display(R)
```

**Subsection Header**
$$\begin{aligned}
    \textsf{average speed:}\quad x_y &= 3.142\,m/s \\
    \textsf{pressure:}\quad k_0 &= 2.707\,bar \\
    \alpha &= 34.0\,deg \\
    \textsf{a vector:}\quad v &= \left[
        1.0,\,2.0,\,3.0,\,4.0
    \right]\, km
\end{aligned}$$
