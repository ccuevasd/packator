import pandas as pd
import numpy as np
import seaborn as sns

df1 = pd.read_csv('data/01.01.2017 - 30.06.2017.csv')
df2 = pd.read_csv('data/01.07.2017 - 31.12.2017.csv')
df3 = pd.read_csv('data/01.01.2018 - 30.06.2018.csv')
df4 = pd.read_csv('data/01.07.2018 - 31.12.2018.csv')
df5 = pd.read_csv('data/01.01.2019 - 30.06.2019.csv')
df6 = pd.read_csv('data/01.07.2019 - 31.12.2019.csv')
df7 = pd.read_csv('data/01.01.2020 - 28.07.2020.csv')
dfb = pd.read_csv('data/Bundesland-PLZ.csv')
df = pd.concat([df1, df2, df3, df4, df5, df6, df7])

df.drop(['pickupCompleteBefore', 'pickupNotes', 'shippingAddress2', 'closingReason',
         'closingDetails', 'loadingTimePickupMin', 'waitingTimePickupMin', 'loadingTimeShippingMin',
         'waitingTimeShippingMin', 'externalReference', 'netPriceWaitingTimePickup',
         'netPriceWaitingTimeShipping', 'netPriceLoadingTimePickup', 'netPriceLoadingTimeShipping',
         'netPriceDelivery', 'netPriceLoadingHelpPickup', 'netPriceLoadingHelpShipping',
         'netPriceProofDelivery', 'costCenter1', 'costCenter2', 'netPayoutWaitingTimePickup',
         'netPayoutWaitingTimeShipping', 'netPayoutLoadingTimePickup', 'netPayoutLoadingTimeShipping',
         'netPayoutLoadingHelpPickup', 'netPayoutLoadingHelpShipping'], axis=1, inplace=True)

df['datetime'] = pd.to_datetime(df['shippingCompleteBefore'], dayfirst=True)
dt = pd.DatetimeIndex(df['datetime'])

df['date'] = dt.date
df['day'] = dt.day
df['month'] = dt.month
df['year'] = dt.year
df['hour'] = dt.hour
df['min'] = dt.minute
df['doy'] = dt.dayofyear
df['woy'] = dt.weekofyear

index_names = df[df['productSize'] == '*'].index
df.drop(index_names, inplace=True)
df['productSize'] = df['productSize'].str.upper()

dfb['shippingPostalCode'] = dfb['PLZ']
dfb['shippingPostalCode'] = dfb['shippingPostalCode'].astype(str)

dft = df.merge(dfb, how='inner', on='shippingPostalCode')
dft.set_index(dft['datetime'], inplace=True)


dft.to_csv('data/2017 - 2020.csv')
