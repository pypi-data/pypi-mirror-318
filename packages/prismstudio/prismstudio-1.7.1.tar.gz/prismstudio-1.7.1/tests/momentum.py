import prismstudio as ps

ps.login(username='superuser', password='L:3v[5a:mv8,z3Cf')

#Commonly used dataitems
close_divadj = ps.market.close(currency='trade')
close = ps.market.close(currency='trade', adjustment=True)
open_ = ps.market.open(currency='trade', adjustment=True)
high = ps.market.high(currency='trade', adjustment=True)
low = ps.market.low(currency='trade', adjustment=True)
volume = ps.market.volume(adjustment=True)

# ---------------------------------------------- Price Related Factors ---------------------------------------------- #
#1001 12M - 1M Price Momentum
PM_12M1M = (close.sample_shift(21) / close.sample_shift(252)) - 1

#1002 9M Price Momentum
PM_9M = close.sample_pct_change(189)

#1003 6M Price Momentum
PM_6M = close.sample_pct_change(126)

#1003 1M Price Momentum
PM_1M = close.sample_pct_change(21)

#1004 1W Price Momentum
PM_1W = close.sample_pct_change(5)

#1006 1W Mean Daily Price Return
RM_1W = close.sample_pct_change(1).sample_mean(5)

#1007 1W Exponentially Weighted Mean Daily Price Return
RM_EWM1W = close.sample_pct_change(1).sample_ewma(5)

#1008 1M Mean Daily Price Return
RM_1M = close.sample_pct_change(1).sample_mean(21)

#1009 1M Exponentially Weighted Mean Daily Price Return
RM_EWM1M = close.sample_pct_change(1).sample_ewma(21)

#1010 MACD RATIO
MACDR = close.sample_ewma(12) / close.sample_ewma(26)

#1011 9D Exponentially Weighted MEAN MACD RATIO
MACDR_10D = MACDR.sample_ewma(9)

#1012 50D/200D Moving Average Ratio 
MAR_50D200D = close.sample_mean(50) / close.sample_mean(200)

#1013 10D/50D Moving Average Ratio
MAR_10D50D = close.sample_mean(10) / close.sample_mean(50)

#1014 20D AB-Ratio
a = (high - open_).sample_sum(20) / (open_ - low).sample_mean(20)
b = (high - close.sample_shift(1)).sample_sum(20) / (close.sample_shift(1) - low).sample_sum(20)
ABR_20D = a/b

#1017 10D RSI
diff = close.sample_diff(1)
up_total = ((diff > 0).map({True: diff, False: 0})).sample_sum(10)
up_count = ((diff > 0).map({True: 1, False: 0})).sample_sum(10)
up_avg = up_total / up_count
down_total = ((diff < 0).map({True: (-1)*diff, False: 0})).sample_sum(10)
down_count = ((diff < 0).map({True: 1, False: 0})).sample_sum(10)
down_avg = down_total / down_count
rs = up_avg/down_avg
RSI_10D = 100 - 100 / (1 + rs)

#1018 60D Price Z Score
PZ_60D = close.sample_z_score(60)

#1019 120D Price Z Score
PZ_120D = close.sample_z_score(120)

#1020 20D High Low Ratio
HL_20D = (close.sample_max(20) - close) / (close - close.sample_min(20))

#1021 Percent off from 252D high
H_252D = close / close.sample_max(252)

#1022 Percent off from 252D low
L_252D = close / close.sample_min(252)

#1023 21D Win Ratio
win = close.sample_diff(1)
win = (win > 0).map({True: 1, False: 0})
WIN_21D = win.sample_sum(21) / 21

#1024 28D Vertical Horizontal Filter
VHF_28D = (close.sample_max(28) - close.sample_min(28)) / close.sample_diff(1).abs().sample_sum(28)

#1025 20D Commodity Channel Index
tprc = (high + low + close) / 3
deviation = tprc - tprc.sample_mean(20)
mad = (deviation.abs()).sample_mean(20)
CCI_20D = deviation / (0.015*mad)

#1026 Know Sure Thing
roc10D = close.sample_pct_change(10)
roc15D = close.sample_pct_change(15)
roc20D = close.sample_pct_change(20)
roc30D = close.sample_pct_change(30)

roc10D_sma_10D = roc10D.sample_mean(10)
roc15D_sma_10D = roc15D.sample_mean(10)
roc20D_sma_10D = roc20D.sample_mean(10)
roc30D_sma_15D = roc30D.sample_mean(15)

kst = roc10D_sma_10D + (2*roc15D_sma_10D) + (3*roc20D_sma_10D) + (4*roc20D_sma_10D)
kst_9D = kst.sample_mean(9)

KST = kst / kst_9D


# ---------------------------------------------- Volume Related Factors --------------------------------------------- #

# 1025 5D Volume to 252D Volume
VOLUME_5D = volume.sample_mean(5) / volume.sample_mean(252)

# 1026 42D Volume to 252D Volume
VOLUME_42D = volume.sample_mean(42) / volume.sample_mean(252)


#1027 10D Accumulation Distribution Ratio
high_10D = high.sample_max(10)
low_10D = low.sample_min(10)
mfv = ((2*close - low_10D - high_10D) / (high_10D - low_10D))*volume
ACCUMDIST_10D = mfv.sample_sum(10) / volume.sample_sum(10)

#1028 10D On Balance Volume Ratio
coef = close.sample_diff(1)
coef = (coef > 0).map({True: 1, False: coef})
coef = (coef < 0).map({True: -1, False: coef})
obv_n = coef * volume
OBV_10D = obv_n.sample_sum(10) / volume.sample_sum(10)

#1029 10D Money Flow Ratio
MF_10D = (coef * close * volume).sample_sum(10) / (close * volume).sample_sum(10)


# ------------------------------------------------- Breadth Factors ------------------------------------------------- #
#1015 21D Advance Decline Ratio
advance = (close.sample_pct_change(21) > 0).cross_sectional_sum()
decline = (close.sample_pct_change(21) < 0).cross_sectional_sum()
advancedecline = advance / decline

rm_1w = close.sample_pct_change(1).sample_mean(21)


#100 close / 252 day high
prc2high = close / close.sample_max(252)

#1004 close / 252 day low
prc2low = close / close.sample_min(252)

#1005 1M P

