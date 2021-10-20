import akshare as ak
import pandas as pd
from workalendar.asia import China
from datetime import date, timedelta, datetime

fund_em_open_fund_rank_df = ak.fund_em_open_fund_rank()
#fund_em_exchange_rank_df = ak.fund_em_exchange_rank()

fund_em_open_fund_rank_df['单位净值'] = pd.to_numeric(fund_em_open_fund_rank_df['单位净值'])
fund_em_open_fund_rank_df['累计净值'] = pd.to_numeric(fund_em_open_fund_rank_df['累计净值'])
fund_em_open_fund_rank_df['日增长率'] = pd.to_numeric(fund_em_open_fund_rank_df['日增长率'])
fund_em_open_fund_rank_df['近1周'] = pd.to_numeric(fund_em_open_fund_rank_df['近1周'])
fund_em_open_fund_rank_df['近1月'] = pd.to_numeric(fund_em_open_fund_rank_df['近1月'])
fund_em_open_fund_rank_df['近3月'] = pd.to_numeric(fund_em_open_fund_rank_df['近3月'])
fund_em_open_fund_rank_df['近6月'] = pd.to_numeric(fund_em_open_fund_rank_df['近6月'])
fund_em_open_fund_rank_df['近1年'] = pd.to_numeric(fund_em_open_fund_rank_df['近1年'])
fund_em_open_fund_rank_df['近2年'] = pd.to_numeric(fund_em_open_fund_rank_df['近2年'])
fund_em_open_fund_rank_df['近3年'] = pd.to_numeric(fund_em_open_fund_rank_df['近3年'])
fund_em_open_fund_rank_df['今年来'] = pd.to_numeric(fund_em_open_fund_rank_df['今年来'])
fund_em_open_fund_rank_df['成立来'] = pd.to_numeric(fund_em_open_fund_rank_df['成立来'])

fund_em_open_fund_rank_df['rank日增长率'] = fund_em_open_fund_rank_df['日增长率'].rank(ascending=False,method='max')
fund_em_open_fund_rank_df['rank近1周'] = fund_em_open_fund_rank_df['近1周'].rank(ascending=False,method='max')
fund_em_open_fund_rank_df['rank近1月'] = fund_em_open_fund_rank_df['近1月'].rank(ascending=False,method='max')
fund_em_open_fund_rank_df['rank近3月'] = fund_em_open_fund_rank_df['近3月'].rank(ascending=False,method='max')
fund_em_open_fund_rank_df['rank近6月'] = fund_em_open_fund_rank_df['近6月'].rank(ascending=False,method='max')
fund_em_open_fund_rank_df['rank近1年'] = fund_em_open_fund_rank_df['近1年'].rank(ascending=False,method='max')

fund_size = pd.read_excel('/home/size.xlsx')
fund_size['code']=pd.to_numeric(fund_size['code'])
fund_em_open_fund_rank_df.rename(columns={'基金代码':'code'},inplace = True)
fund_em_open_fund_rank_df['code']=pd.to_numeric(fund_em_open_fund_rank_df['code'])
fund_em_open_fund_rank_df = fund_em_open_fund_rank_df.set_index('code').join(fund_size.set_index('code'))
fund_em_open_fund_rank_df_size = fund_em_open_fund_rank_df['size']
fund_em_open_fund_rank_df = fund_em_open_fund_rank_df.drop('size',axis=1)
fund_em_open_fund_rank_df.insert(2,'size',fund_em_open_fund_rank_df_size)
fund_em_open_fund_rank_df = fund_em_open_fund_rank_df.sort_values(by='日增长率',ascending=False)
cal = China()
aday = datetime.now()
while (not cal.is_working_day(aday)):
    aday = aday + timedelta(days=-1)
datestr = aday.strftime('%Y%m%d')
with pd.ExcelWriter('/home/'+datestr+'.xlsx') as writer:  
    fund_em_open_fund_rank_df.to_excel(writer, sheet_name='open')
    
#import akshare as ak
#macro_china_market_margin_sz_df = ak.macro_china_market_margin_sz()
#macro_china_market_margin_sz_df.to_excel('/home/rongzi.xlsx')
#print(macro_china_market_margin_sz_df[-20:])
