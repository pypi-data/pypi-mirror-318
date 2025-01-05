# CGMac (CGM Metrics Calculator)
## Overview
This code calculates key metrics from Continuous Glucose Monitoring (CGM) data for multiple individuals. It processes time series glucose data and calculates various statistical measures including mean glucose levels, standard deviation and temporal autocorrelation properties.

## Function description

The main function `cgmac` processes CGM data and returns the following measures for each individual
- Mean glucose level
- Standard deviation of the glucose levels
- Mean of autocorrelation values
- Variance of autocorrelation values

These measures are particularly useful for
- Predicting glucose control abilities including insulin sensitivity, insulin secretion, and insulin clearance
- Prediction of diabetic complications

## Lag Parameter Selection

### Default Recommendations
For a typical CGM analysis, we recommend the following lag settings based on sampling interval:
- 5-minute sampling interval: lag = 30 (covers 150 minutes)
- 15-minute sampling interval: lag = 10 (covers 150 minutes)

These recommendations are based on capturing temporal correlations over a 150-minute window, which often provides meaningful insights into glucose dynamics.
The lag parameter is fully customisable as optimal lag values may vary depending on your research objectives.

Examples of use with different sampling intervals:
```python
import cgmac
# For 5-minute interval data
results_5min = cgmac.cgmac(data=cgm_data_5min, lag=30)

# For 15-minute interval data
results_15min = cgmac.cgmac(data=cgm_data_15min, lag=10)

# Custom lag for specific research needs
results_custom = cgmac.cgmac(data=cgm_data, lag=your_custom_lag)
```

## Prerequisites

Required Python libraries:
- pandas
- statsmodels
- numpy

## Input data format

The input DataFrame should be structured as follows
- First column: Individuals IDs
- Second column onwards: Glucose readings (time series data)
- Each row represents a different individual's CGM readings.

Example input data structure:
```python
  ID  Reading1 Reading2 Reading3 ...
0 1  120 125 118 ...
1 2  115 118 121 ...
```

