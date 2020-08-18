from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#ignore warning for copying into the same slice
import warnings
warnings.filterwarnings(action='ignore')
#creating a function for atomatic data transforming

class transform_for_regression():
    def fit_transform(self, df=None):
        if df is None:
            pass
        LE = LabelEncoder()
        df['Flight'] = LE.fit_transform(df['Origin'] + df['Dest'])
        df = df[(df['DepTime'] >= 0) & (df['DepTime'] < 2400)]
        if 'dep_delayed_15min' in df.columns:
            df.drop(labels='dep_delayed_15min', axis=1, inplace=True)
        df.drop(labels=['Origin', 'Dest'], axis=1, inplace=True)
        df_categorical = df[['Month', 'DayofMonth', 'DayOfWeek', 'UniqueCarrier']]
        df['Month'] = LE.fit_transform(df['Month']) + 1
        df['DayofMonth'] = LE.fit_transform(df['DayofMonth']) + 1
        df['DayOfWeek'] = LE.fit_transform(df['DayOfWeek']) + 1
        df['UniqueCarrier'] = LE.fit_transform(df['UniqueCarrier']) + 1
        OHE = OneHotEncoder()
        df_OHE = OHE.fit_transform(df_categorical)
        df_OHE_df = pd.DataFrame(df_OHE.toarray(),
                columns=[i for i in range (1, df_OHE.toarray().shape[1] + 1)],
                                 index=df_categorical.index)
        df_OHE_df['DepTime'] = df['DepTime']
        df_OHE_df['Distance'] = df['Distance']
        df_OHE_df['Flight'] = df['Flight']
        df_OHE_df_scaled = s_scale.fit_transform(df_OHE_df)
        return df_OHE_df_scaled
    
class transform_for_boosting():
    def fit_transform(self, df):
        if df is None:
            pass
        LE = LabelEncoder()
        df['Flight'] = LE.fit_transform(df['Origin'] + df['Dest'])
        df = df[(df['DepTime'] >= 0) & (df['DepTime'] < 2400)]
        if 'dep_delayed_15min' in df.columns:
            df.drop(labels='dep_delayed_15min', axis=1, inplace=True)
        df.drop(labels=['Origin', 'Dest'], axis=1, inplace=True)
        df_categorical = df[['Month', 'DayofMonth', 'DayOfWeek', 'UniqueCarrier']]
        df['Month'] = LE.fit_transform(df['Month']) + 1
        df['DayofMonth'] = LE.fit_transform(df['DayofMonth']) + 1
        df['DayOfWeek'] = LE.fit_transform(df['DayOfWeek']) + 1
        df['UniqueCarrier'] = LE.fit_transform(df['UniqueCarrier']) + 1
        return df