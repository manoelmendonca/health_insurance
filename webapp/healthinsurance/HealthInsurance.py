#-------------------------------------------------------------------------------
#                    HEALTH INSURANCE CROSS-SELLING PROJECT
# File: HealthInsurance.py
#
# Goal: this class is used in 'handler.py' file, being...
#       ...called by the MachineLearning-API.
#       The class encapsulates the commands to perform a ML forecasting
#       It performs all the data clearing, encodings & transformation needed.
#
#                                                        First date.: 2024.05.21
# manoelmendonca@hotmail.com                             Last update: 2024.09.07
#-------------------------------------------------------------------------------

import pickle
import pandas as pd
import numpy as np
#import inflection
#import math
#import datetime


class HealthInsurance:
    def __init__(self) -> None:
        self.home_path = '../webapp/models/'
        #self.home_path = 'C:/MeusEstudos/CURSOS TI/Em 2023 - ComunidadeDS/Projetos do Aluno/PA.04 health_insurance_priv/webapp/models/'
        # variáveis utilizadas na versão "atual": ver método "DataTransforming"
        self.age_scaler                       = pickle.load( open( self.home_path + 'age_scaler.pkl', 'rb' ) )
        self.age_rbf_24_scaler                = pickle.load( open( self.home_path + 'age_rbf_24_scaler.pkl', 'rb' ) )
        self.age_rbf_44_scaler                = pickle.load( open( self.home_path + 'age_rbf_44_scaler.pkl', 'rb' ) )
        self.annual_premium_scaler            = pickle.load( open( self.home_path + 'annual_premium_scaler.pkl', 'rb' ) )
        self.annual_premium_scaler_f1         = pickle.load( open( self.home_path + 'annual_premium_scaler_f1.pkl', 'rb' ) )
        self.annual_premium_scaler_f2         = pickle.load( open( self.home_path + 'annual_premium_scaler_f2.pkl', 'rb' ) )
        self.ohe_gender                       = pickle.load( open( self.home_path + 'ohe_gender_scaler.pkl', 'rb' ) )
        self.fe_policy_sales_channel_scaler   = pickle.load( open( self.home_path + 'fe_policy_sales_channel_scaler.pkl', 'rb' ) )
        self.policy_sales_chn_importance_dict = pickle.load( open( self.home_path + 'fe_policy_sales_channel_dict.pkl', 'rb' ) )
        self.looe_region_code_scaler          = pickle.load( open( self.home_path + 'looe_region_code_scaler.pkl', 'rb' ) )
        self.ohe_vehicle_age                  = pickle.load( open( self.home_path + 'ohe_vehicle_age_scaler.pkl', 'rb' ) )
        self.vintage_scaler                   = pickle.load( open( self.home_path + 'vintage_scaler.pkl', 'rb' ) )

        # variáveis constantes na versão "original" e descontinuados
        #self.annual_premium_scaler_f3         = pickle.load( open( self.home_path + 'annual_premium_scaler_f3.pkl', 'rb' ) )

    def data_cleaning( self, df1 ):
        # 1.0. Rename Columns to LowerCase
        df1.columns = df1.columns.str.lower()
        return df1

    def feature_engineering( self, df3 ):
        # 3.2. Create Features

        # Simple conversion of "vehicle_damage", "vehicle_age" and "annual_premium"

        # vehicle damage number
        df3['vehicle_damage'] = df3['vehicle_damage'].apply( lambda x: 1 if x == 'Yes' else 0 )

        # vehicle age
        df3['vehicle_age'] = df3['vehicle_age'].apply( lambda x: 'over_2_years' if x == '> 2 Years' else 
                                                            'between_1_2_years' if x == '1-2 Year'  else 
                                                            'bellow_1_year' )

        # From 'annual_premium', derive 3 features
        #    - feature.1: points with values between 2630-2675, others =ZERO
        #    - feature.2: values from 2675 to 74301 (or 83260), others =ZERO
        #    - feature.3: values above previous limits, others =ZERO
        df3['annual_premium_f1'] = df3['annual_premium'].apply( lambda x: 0.0 if x>2675.0 else x )
        df3['annual_premium_f2'] = df3['annual_premium'].apply( lambda x: x if x>2675.0 and x<74301.0 else 0.0 )
        df3['annual_premium_f3'] = df3['annual_premium'].apply( lambda x: 0.0 if x<74301.0 else x )

        return df3

    def DataTransforming(self, in_df):

        # The code here is (almost) a mirror of Section 6.1: DataFitAndTransform.DataTransforming

        out_df = in_df.copy()

        # gender: encoding
        ohe_gender = self.ohe_gender.transform(out_df[['gender']])
        out_df = pd.concat([out_df, ohe_gender], axis=1).drop(columns=['gender'])

        # region_code: encoding
        out_df = self.looe_region_code_scaler.transform(out_df)

        # annual_premium: standardization
        out_df['annual_premium'] = self.annual_premium_scaler.transform(out_df[['annual_premium']].values)
        out_df['annual_premium_f1'] = self.annual_premium_scaler_f1.transform(out_df[['annual_premium_f1']].values)
        out_df['annual_premium_f2'] = self.annual_premium_scaler_f2.transform(out_df[['annual_premium_f2']].values)
#       out_df['annual_premium_f3'] = self.ss3.transform(out_df[['annual_premium_f3']].values)

        # policy_sales_channel: encoding
        out_df['policy_sales_channel_importance'] = out_df['policy_sales_channel'].map(self.policy_sales_chn_importance_dict)
        out_df['policy_sales_channel'] = out_df['policy_sales_channel'].map(self.fe_policy_sales_channel_scaler)

        # age: rescaling
        out_df['age_rbf_24'] = out_df['age'].map(self.age_rbf_24_scaler)
        out_df['age_rbf_44'] = out_df['age'].map(self.age_rbf_44_scaler)
        out_df['age'] = self.age_scaler.transform(out_df[['age']].values)

        # vehicle_age: encoding
        ohe = self.ohe_vehicle_age.transform(out_df[['vehicle_age']])
        out_df = pd.concat([out_df, ohe], axis=1).drop(columns=['vehicle_age'])

        # vintage: rescaling
        out_df['vintage'] = self.vintage_scaler.transform(out_df[['vintage']].values)

        return out_df

    def data_preparation( self, df6 ):

        # 6.2. Split data
        # treat "annual_premium_f3"
#        df6 = df6[ (df6['annual_premium_f3'] == 0) ]
#        df6 = df6.drop( 'annual_premium_f3', axis=1 )
        # Apply scalers&encodings to validation set
        df6 = df6.drop(columns=['response'], errors='ignore')
        df6 = self.DataTransforming(df6)

        # 6.3. Resampling: nop

        # 7.6. Manual feature selection
        cols_selected = ['age_rbf_24',
                        # 'age', 'age_rbf_44', 'vehicle_age_over_2_years',
                         'annual_premium', 'annual_premium_f1',
                         'annual_premium_f2', 'driving_license',
                         'gender_Female', 'gender_Male', 'policy_sales_channel',
                         'policy_sales_channel_importance', 'previously_insured',
                         'region_code', 'vehicle_age_bellow_1_year',
                         'vehicle_age_between_1_2_years',
                         'vehicle_damage', 'vintage']

        return df6[ cols_selected ]

    def get_prediction( self, model, original_data, test_data ):

        # DEBUG
        #test_data.to_csv('test_data.csv', index=False)

        # model prediction
        pred = model.predict_proba( test_data )

        # From predict_proba, get only col.1: probability of True-Response
        pred1 = [ col[1] for col in pred ]

        # join prediction into original data
        original_data['score'] = pred1

        # convert to JSON & return results
        return original_data.to_json( orient='records', date_format='iso' )




