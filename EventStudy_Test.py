import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from collections import defaultdict
from collections import OrderedDict


# READ EXCEL FILE WITH STOCK RETURN DATA AND S&P 500 INDEX
return_Data = pd.read_excel(r'C:\Users\rjoosten\PycharmProjects\EventStudy\Stock Price Data.xlsx', index=False)

# CREATE DATETIME OF DATE COLUMN
return_Data['Date'] = pd.to_datetime(return_Data['Date'])

# CREATE LIST OF STOCKS
symbols_list = ['HII US Equity', 'HON', '^GSPC']

# CREATE AN EVENTS DATA FRAME WHERE COLUMN ARE THE NAMES OF ALL THE STOCKS AND ROWS ARE THE DAILY DATES
events_col = symbols_list[:]
events_col.remove('^GSPC')  # We dont't need to create events for the S&P500

# COPY THE DATE INDEX FROM DATA_RET TO THE EVENTS DATA FRAME
events_index = return_Data['Date']  # Copy the date index from data_ret to the events data frame
data_events = pd.DataFrame(index=events_index, columns=events_col)

# DEFINE ESTIMATION PERIOD L1:
L1 = 30

# DEFINE WINDOW FOR FORWARD AND BACKWARD LOOKING PERIOD:
window = 3

# DEFINE EVENT DATE
ED = ['2012-06-11']

# CREATE A DICTINOARY FOR THE EVENTS TO STORE THE ABNORMAL RETURNS (AR) VALUES OF EACH WINDOW DAY AND
# A DICTIONARY FOR EACH STOCK TO STORE THE AR VALUES.
pos_dict = defaultdict(dict)
pos_dict_s = defaultdict(dict)


# FOR EACH STOCK, LOCATE EACH EVENT AND CALCULATE ABNORMAL RETURN FOR PREVIOUS WINDOW AND FUTURE WINDOW DAYS
for s in events_col:
    pos_event_dates = ED

    for pos_event in pos_event_dates:
        date_loc = return_Data.loc[return_Data['Date']==pos_event].index[0]


        date_loc = date_loc - window

        if date_loc > L1 and date_loc <= len(return_Data) - (2 * window + 1):
            index_range = (2 * window) + 1

                # Create dictionairy to store the AR values for each day of this event
            pos_dict_s_event = OrderedDict()
            for d in range(index_range):
                date_loc2 = date_loc + d

                    # Parameters to estimate market model
                u_i = return_Data[s][date_loc2 - L1: date_loc2 - 1].mean()
                u_m = return_Data['^GSPC'][date_loc2 - L1: date_loc2 - 1].mean()
                R_i = return_Data.ix[date_loc2, s]
                R_m = return_Data.ix[date_loc2, '^GSPC']
                beta_i = ((R_i - u_i) * (R_m - u_m)) / (R_m - u_m) ** 2
                alpha_i = u_i - (beta_i * u_m)
                var_err = (1 / (L1 - 2)) * (R_i - alpha_i - (beta_i * R_m)) ** 2
                AR_i = R_i - alpha_i - (beta_i * R_m)
                print(AR_i)
                pos_dict_s_event[date_loc2] = AR_i

            pos_dict_s[pos_event] = pos_dict_s_event

    pos_dict[s] = pos_dict_s
print(pos_dict_s)
# CREATE EMPTY RETURNS DATAFRAME
abret_col = symbols_list[:]  # Use [:] to deep copy the list
abret_col.remove('^GSPC')  # We dont't need to calculate abnormal returns for the S&P500
abret_index = range(-window, window + 1)
pos_data_abret = pd.DataFrame(index=abret_index, columns=abret_col)
print(pos_data_abret)
for h in abret_col:
    if h in pos_dict.keys():
        for z in abret_index:
            pos_data_abret[h][z] = np.mean([x.values()[z + window] for x in pos_dict[h].values()])

print(pos_data_abret)
# CREATE CAR TABLE
pos_CAR = pos_data_abret.cumsum()
print(pos_CAR)

# PLOT CAR
plt.clf()
plt.plot(pos_CAR)
plt.legend(pos_CAR)
plt.ylabel('CAR')
plt.xlabel('Window')
matplotlib.rcParams.update({'font.size': 8})
plt.savefig('PositiveCAR_All.png', format='png')

# SUM CAR AND PLOT THE AGGREGATE

pos_CAR['SUM'] = pos_CAR.sum(axis=1)


plt.clf()
plt.plot(pos_CAR['SUM'])
plt.legend(pos_CAR['SUM'])
plt.ylabel('CAR')
plt.xlabel('Window')
matplotlib.rcParams.update({'font.size': 8})
plt.savefig('PositiveCAR_SUM.png', format='png')
