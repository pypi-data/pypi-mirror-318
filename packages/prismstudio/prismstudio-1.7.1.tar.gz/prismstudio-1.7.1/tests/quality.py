import prismstudio as ps

ps.login(username='superuser', password='L:3v[5a:mv8,z3Cf')
ps.dataitem_search()

income_net = ps.financial.income_statement(dataitemid=100639, periodtype='LTM')
income_op = ps.financial.income_statement(dataitemid=100610, periodtype='LTM')
revenue = ps.financial.income_statement(dataitemid=100589, periodtype='LTM')
cogs = ps.financial.income_statement(dataitemid=100591, periodtype='LTM')
current_asset = ps.financial.balance_sheet(dataitemid=100018, periodtype='Q')
current_liability = ps.financial.balance_sheet(dataitemid=100047, periodtype='Q')
cash_stinv = ps.financial.balance_sheet(dataitemid=100004, periodtype='Q')
acc_receivable = ps.financial.balance_sheet(dataitemid=100006, periodtype='Q')
asset = ps.financial.balance_sheet(dataitemid=100033, periodtype='Q')
liability = ps.financial.balance_sheet(dataitemid=100057, periodtype='Q')
ltdebt = ps.financial.balance_sheet(dataitemid=100048, periodtype='Q')
interestexp = ps.financial.income_statement(dataitemid=100611, periodtype='LTM')
ebitda = ps.financial.income_statement(dataitemid=100723, periodtype='LTM')
cashflow_op = ps.financial.cash_flow(dataitemid=100412, periodtype='LTM')
equity_common = ps.financial.balance_sheet(dataitemid=100075, periodtype='Q')

# Gross Margin
GM = (revenue - cogs) / revenue

# Operating Margin
OM = income_op / revenue

# Net Margin
NM = income_net / revenue

#2001 Current Ratio
CURRENT = current_asset / current_liability

#2002 Quick Ratio
QUICK = (cash_stinv + acc_receivable) / current_liability

#2003 Cash Ratio
CASH = cash_stinv / current_liability

#2004 Debt Ratio
DEBT = liability / asset

#2005 Debt to Equity
DEBT2EQUITY = liability / equity_common

#2005 Long Term Debt to Equity
LTDEBT2EQUITY = ltdebt / equity_common

#2007 Debt to EBITDA
DEBT2EBITDA = liability / ebitda

#2008
cashflow_op