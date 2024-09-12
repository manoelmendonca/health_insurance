#-------------------------------------------------------------------------------
#                    HEALTH INSURANCE CROSS-SELLING PROJECT
# File: handler.py
#
# Goal: this ML-API receives/solves a request to perform a forecast for one item
#
#                                                        First date.: 2024.05.21
# manoelmendonca@hotmail.com                             Last update: 2024.09.07
#-------------------------------------------------------------------------------

import os
import pickle
import pandas as pd
from flask             import Flask, request, Response

# from "pasta.NomeDoArquivo" import "NomeDaClasse"
from healthinsurance.HealthInsurance  import HealthInsurance

#............... Load model
model = pickle.load( open( 'models/final_model.pkl', 'rb' ) )
#model = pickle.load( open( 'C:/MeusEstudos/CURSOS TI/Em 2023 - ComunidadeDS/Projetos do Aluno/PA.04 health_insurance_priv/webapp/models/final_model.pkl', 'rb' ) )

#............... Init API
# REF: https://flask.palletsprojects.com/en/2.3.x/genindex/

app = Flask( __name__ )

#............... Create Endpoint Route
# REF: https://flask.palletsprojects.com/en/2.3.x/api/#flask.Blueprint.route
# predict function: that's the handler, activated when the API receives a request

@app.route( '/healthinsurance/predict', methods=['POST'] )
def health_insurance_predict():
    test_json = request.get_json()

    if test_json: # is there any data in the received request?
        if isinstance( test_json, dict ): # unique dt
            # Convert 1-line Json to DataFrame
            test_raw = pd.DataFrame( test_json, index=[0] )

        else: # multiple dt
            # Convert N-lines Json to DataFrame
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )

        # Instantiate HealthInsurance class
        pipeline = HealthInsurance()

        # data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        # feature engineering
        df2 = pipeline.feature_engineering( df1 )
        # data preparation
        df3 = pipeline.data_preparation( df2 )
        # prediction
        json_response = pipeline.get_prediction( model, test_raw, df3 )

        return json_response

    else:
        # No data in the received request
        return Response( 'OK, but no data... {}', status=200, mimetype='application/json' )


#............... Run Flask API
if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 )
    app.run( '0.0.0.0', port=port )
