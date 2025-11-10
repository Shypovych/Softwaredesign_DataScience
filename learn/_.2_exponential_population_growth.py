# =============================================================
#   EXPONENTIAL POPULATION GROWTH — LOG-LINEAR REGRESSION
# =============================================================
# This script uses real global population data from
# Our World in Data (OWID) and fits exponential growth
# models for different historical periods.
#
# It demonstrates that population grows approximately
# exponentially, i.e., linear in logarithmic scale.
# -------------------------------------------------------------
# Requirements:
#   pip install owid-catalog plotly numpy scipy
# -------------------------------------------------------------

from owid.catalog import charts
import numpy as np
import scipy.optimize
import plotly.graph_objects as go

# =============================================================
#   LOAD DATA FROM OUR WORLD IN DATA
# =============================================================
# Dataset: World population by year
df = charts.get_data("https://ourworldindata.org/grapher/population?country=~OWID_WRL")

# Filter for world-level data
data = df[df["entities"] == "World"]

# Extract year and population arrays
x = data["years"].to_numpy()
y = data["population"].to_numpy()

# Log-transform population (so exponential growth becomes linear)
ylog = np.log(y)

# =============================================================
#   DEFINE LOSS FUNCTION (L₂ NORM)
# =============================================================
def fit_L2(x0, t):
    """Least-squares loss for linear fit in log-space."""
    x, y = t
    return np.sum((x0[0] * x + x0[1] - y) ** 2)

# =============================================================
#   FIT MULTIPLE TIME INTERVALS
# =============================================================
# Different starting points for sub-period fitting
start_years = [-np.inf, 0, 1700, 1900, 1980]
fits = []  # store fitted exponential curves

# For each start year, fit a linear model to log(y)
for start in start_years:
    mask = x >= start
    t = (x[mask], ylog[mask])
    x0 = np.array([1.0, 1.0])  # initial guess [slope, intercept]

    # Optimize using Nelder–Mead
    coeffs = scipy.optimize.fmin(fit_L2, x0, args=(t,), disp=False)

    # Reconstruct exponential model: y = e^(b0*x + b1)
    fits.append(np.exp(coeffs[1]) * np.exp(coeffs[0] * x))

# =============================================================
#   VISUALIZATION WITH PLOTLY
# =============================================================
# Create two figures:
#   fig1 — linear y-axis
#   fig2 — logarithmic y-axis
fig_linear = go.Figure()
fig_log = go.Figure()

# Scatter of actual data
fig_linear.add_trace(go.Scatter(
    mode="markers", x=x, y=y, name="Observed data", marker=dict(color="red")
))
fig_log.add_trace(go.Scatter(
    mode="markers", x=x, y=y, name="Observed data", marker=dict(color="red")
))

# Add fitted exponential curves for each start year
for i, yfit in enumerate(fits):
    label = f"Fit from {start_years[i]}"
    fig_linear.add_trace(go.Scatter(x=x, y=yfit, name=label))
    fig_log.add_trace(go.Scatter(x=x, y=yfit, name=label))

# -------------------------------------------------------------
# LINEAR SCALE
fig_linear.update_layout(
    title="Exponential Fit of World Population (Linear Scale)",
    xaxis_title="Year",
    yaxis_title="Population",
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
)
fig_linear.update_xaxes(range=[1700, 2023])
fig_linear.update_yaxes(range=[0, 9e9])
fig_linear.show()

# -------------------------------------------------------------
# LOG SCALE
fig_log.update_layout(
    title="Exponential Fit of World Population (Logarithmic Scale)",
    xaxis_title="Year",
    yaxis_title="Population (log scale)",
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
)
fig_log.update_xaxes(range=[1700, 2023])
fig_log.update_yaxes(type="log", range=[8.5, 10])
fig_log.show()