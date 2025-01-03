import prismstudio as ps
import datetime

ps.login(username='khg311@shinhan.com', password='YmcPTeWaxFYbwlO')

starttime = datetime.datetime.now()
univ='Global/APACEU_ex_KRJPUK_primary_exFinancial_mcap30_vol40_anal2_from2000'
sd = '2022-01-01'

#Commonly used dataitems
mc = ps.market.market_cap(currency='trade')
close = ps.market.close(adjustment=True, currency='trade').resample('D', 21)

cash = (
    ps.financial.balance_sheet(dataitemid=100004, periodtype='Q', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .fillna(0)
         .resample('D', 365)
)

debt = (
    ps.financial.balance_sheet(dataitemid=100151, periodtype='Q', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .fillna(0)
         .resample('D', 365)
)

ev = mc + debt - cash


# -------------------------------------------------------------------------------------------------------------------- #
#                                                     Value Factors                                                    #
# -------------------------------------------------------------------------------------------------------------------- #

# ----------------------------------------------- Sales Related Factor ----------------------------------------------- #
sales = (
    ps.financial.income_statement(dataitemid=100580, periodtype='LTM', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .resample('D', 365)
)
sales_fwd = (
    ps.estimate.consensus(dataitemid=200256, periodtype='Q-SA', periodout=0, currency='trade')
         .resample('D', 365)
)

#101. Sales to Price
s2p = sales / mc

#102. 5 year Average Sales to Price
s2p_5yr = s2p.n_periods_mean(5*365) #daily
#s2p_5yr = s2p.resample('M', 31).n_periods_mean(5*12) #monthly

#103. Forward Sales to Price
s2p_fwd = sales_fwd / mc

#104. Sales to Enterprise Value(EV)
s2ev = sales / ev

#105. 5 year average Sales to Enterprise Value
s2ev_5yr = (sales / ev).resample('B', 10).n_periods_pct_mean(5*260)
#s2ev_5yr = s2ev.resample('M', 31).n_period_pct_mean(5*12) #monthly

#106. Forward Sales to EV
s2ev_fwd = sales_fwd / ev


# --------------------------------------------- Book Value Related Factor -------------------------------------------- #
book = (
    ps.financial.balance_sheet(dataitemid=100075, periodtype='Q', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .resample('D', 365)
)

goodwill = (
    ps.financial.balance_sheet(dataitemid=100023, periodtype='Q', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .fillna(0)
         .resample('D', 365)
)

intangible = (
    ps.financial.balance_sheet(dataitemid=100024, periodtype='Q', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .fillna(0)
         .resample('D', 365)   
)

book_tangible = book - goodwill - intangible

#107. Book to Price
b2p = book / mc

#108. Tangible Book to Price
b2p_tangible = book_tangible / mc

#129. 12M Book to Price Z-Score
b2p_z = b2p.n_periods_z_score(365)

# ------------------------------------------------ Debt Related Factor ----------------------------------------------- #
#109. Net Debt to EV
d2ev = (debt - cash) / ev

# ---------------------------------------------- Earnings Related Factor --------------------------------------------- #
earnings = (
    ps.financial.income_statement(dataitemid=100647, periodtype='LTM', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .resample('D', 365)
)

earnings_fwd = (
    ps.estimate.consensus(dataitemid=200219, periodtype='NTM', periodout=0, currency='trade')
         .resample('D', 365)
)

ebidta = (
    ps.financial.income_statement(dataitemid=100723, periodtype='LTM', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .resample('D', 365)
)

ebidta_fwd = (
    ps.estimate.consensus(dataitemid=200099, periodtype='NTM', periodout=0, currency='trade')
         .resample('D', 365)
)

gp = (
    ps.financial.income_statement(dataitemid=100595, periodtype='LTM', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .resample('D', 365)
)

#110. Earnings to Price
e2p = earnings / mc

#111. 5 year Average Earnings to Price
e2p_5yr = e2p.n_periods_mean(5*365) #daily
#e2p_5yr = e2p.resample('M', 31).n_periods_mean(5*12) #monthly

#112. Forward Earnings to Price
e2p_fwd = earnings_fwd / mc

#113. EBITDA to EV
ebidta2ev = ebidta / ev

#114. Forward BITDA to EV
ebitda2ev_fwd = ebidta_fwd / ev

#115. Gross Profit to Price
gp2p = gp / mc

#130. 12M Earnings to Price Z-Score
e2p_z = e2p.n_periods_z_score(365)

#131. 4w Forward Earnings to Price Change
e2pchg_fwd_4w = (earnings_fwd / mc).n_periods_pct_change(30)

#132. 8w Forward Earnings to Price Change
e2pchg_fwd_8w = (earnings_fwd / mc).n_periods_pct_change(60)

# --------------------------------------------- Cash Flow Related Factor --------------------------------------------- #
cash_op = (
    ps.financial.cash_flow(dataitemid=100412, periodtype='LTM', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .resample('D', 365)
)

cash_op_fwd = (
    ps.estimate.consensus(dataitemid=200063, periodtype='NTM', periodout=0, currency='trade')
         .resample('D', 365)
)

cash_free = (
    ps.financial.cash_flow(dataitemid=100513, periodtype='LTM', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=4)
         .resample('D', 365)
)

cash_free_fwd = (
    ps.estimate.consensus(dataitemid=200153, periodtype='NTM', periodout=0, currency='trade')
         .resample('D', 365)
)

#117. Operating Cash Flow to Price
ocf2p = cash_op / mc

#118. Foward Operating Cash Flow to Price
ocf2p_fwd = cash_op_fwd / mc

#119. Free Cash Flow to Price
fcf2p = cash_free / mc

#120. Forward Free Cash Flow to Price
fcf2p_fwd = cash_free_fwd / mc

#121. Operating Cash Flow to EV
ocf2ev = cash_op / ev

#122. Forward Operating Cash Flow to EV
ocf2ev_fwd = cash_op_fwd / ev

#123. Operating Cash Flow to EV
fcf2ev = cash_free / ev

#124. Forward Operating Cash Flow to EV
fcf2ev_fwd = cash_free_fwd / ev

# ----------------------------------------------- Yield Related Factor ----------------------------------------------- #
dps = (
    ps.financial.dps(dataitemid=100549, periodtype='LTM', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=2)
         .fillna(0)
         .resample('D', 365)
)

dps_daily = (
    ps.market.dividend()
         .resample('D', lookback=0, beyond='enddate')

)

dps_fwd = (
    ps.estimate.consensus(dataitemid=200069, periodtype='NTM', periodout=0, currency='trade')
         .fillna(0)
         .resample('D', 365)
)

buyback_comm = (
    ps.financial.cash_flow(dataitemid=100431, periodtype='LTM', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=2).fillna(0) * -1
)

buyback_pref = (
    ps.financial.cash_flow(dataitemid=100433, periodtype='LTM', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=2).fillna(0) * -1
)

div = (
    ps.financial.cash_flow(dataitemid=100438, periodtype='LTM', preliminary='keep', currency='trade')
         .fillna(method='ffill', n=2).fillna(0) * -1
)


#125. Dividend Yield
dy = dps / close

#126. Forward Dividend Yield
dy_fwd = dps_fwd / close

#127. Buyback Yield
bby = (buyback_comm + buyback_pref ).resample('D', 365) / mc

#127. Total Yield
ty = (buyback_comm + buyback_pref + div).resample('D', 365) / mc
