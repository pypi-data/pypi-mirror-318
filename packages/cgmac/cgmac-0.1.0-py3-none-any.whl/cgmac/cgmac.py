import pandas as pd
import statsmodels.api as sm

def cgmac(data=None,lag=None):
    """
    Calculate CGM derived measures.
    
    This function calculates various statistics including mean, standard deviation and autocorrelation properties for multiple CGM data in each individual.
    
    Parameters
    ----------
    data : pandas.DataFrame
        Input DataFrame where:
        - First column contains individual IDs
        - Second column onwards contains time series data
        - Each row represents a different group/series
    lag : int
        Number of lags to compute in the autocorrelation function )(AC_Mean and AC_Var)
    
    Returns
    -------
    pandas.DataFrame
        A DataFrame with the following columns
        - ID: Group identifier from the input data
        - Mean: Mean of the time series
        - Std: Standard deviation of the time series
        - AC_Mean: Mean of the autocorrelation values (without lag 0)
        - AC_Var: Variance of the autocorrelation values (without lag 0)
    """
    df =data
    lag=int(lag)
    AC= pd.DataFrame()
    for i in range (0,len(df.iloc[:,0])):
        X = df.iloc[i,1:]
        dff=pd.DataFrame(sm.tsa.stattools.acf(X,nlags=lag,fft=False))
        AC=pd.concat([AC, pd.DataFrame([df.iloc[i,0],X.mean(),X.std(),dff.iloc[1:].mean()[0],dff.iloc[1:].var()[0]]).T])
    AC=AC.rename(columns={0: 'ID'}).rename(columns={1: 'Mean'}).rename(columns={2: 'Std'}).rename(columns={3: 'AC_Mean'}).rename(columns={4: 'AC_Var'})
    return AC
  
