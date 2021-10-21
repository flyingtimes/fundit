def market_emotion(adf,period):
    max_name = str(period)+'max'
    min_name = str(period)+'min'
    rate_name = str(period)+'rate'
    adf[max_name] = adf['融资买入额'].rolling(period).max()
    adf[min_name] = adf['融资买入额'].rolling(period).min()
    adf[rate_name] = adf['融资买入额']/adf[max_name]
def market_emotion_multi(adf,periods,beforetime):
    periodstr=[]
    for period in periods:
        market_emotion(adf,period)
        periodstr.append(str(period)+'rate')
    adf.truncate(before=beforetime).plot(y=periodstr,figsize=(20,10),legend=True)
macro_china_market_margin_sz_df = ak.macro_china_market_margin_sz()
market_emotion_multi(macro_china_market_margin_sz_df,[240,90,60],'1/1/2021')
