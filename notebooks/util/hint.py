import ipywidgets as widgets
from IPython.display import display, Markdown, Code, HTML, JSON

def hint(section):
    if section in SECTION:
        _hint(SECTION[section])
        
def _hint(code):
    code_blocks = [] 
    for block in code.split('\n'):
        block = block.rstrip()
        if len(block) != 0:
            code_blocks.append(block)

    button = widgets.Button(description="Hint")
    button.count = 0
    output = widgets.Output()
    display(button, output)

    def on_button_clicked(b):
        with output:
            if button.count < len(code_blocks):
                display(Code(data=code_blocks[button.count], language='python'))
                button.count+=1
            else:
                button.disabled = True
            
    button.on_click(on_button_clicked)

SECTION = {
'2c':
"""
schema = {
    "Attributes": [
        {
            "AttributeName": "item_id", 
            "AttributeType": "string"
        },
        {
            "AttributeName": "timestamp", 
            "AttributeType": "timestamp"
        },
        {
            "AttributeName": "workingday", 
            "AttributeType": "float"
        }
    ]
}

response = forecast.create_dataset(Domain="RETAIL",
                               DatasetType='RELATED_TIME_SERIES',
                               DatasetName=name,
                               DataFrequency=timeseries_frequency,
                               Schema=schema
)
""",
'2f':
"""
response = forecast.create_dataset_import_job(
    DatasetImportJobName=dataset_group,
    DatasetArn=related_dataset_arn,
    DataSource= {
        "S3Config" : {
            "Path": s3_path,
            "RoleArn": role_arn
        } 
    },
    TimestampFormat= timestamp_format
)
""",
'3b':
"""
algorithm_arn = f'{base_algorithm_arn}Deep_AR_Plus'
predictor_name = f'{project}_Deep_AR_Pls'

response = forecast.create_predictor(
    PredictorName = predictor_name,
    AlgorithmArn = algorithm_arn,
    ForecastHorizon = forecast_horizon,
    PerformAutoML = False,
    PerformHPO = False,
    InputDataConfig = {'DatasetGroupArn': dataset_group_arn},
    FeaturizationConfig = {'ForecastFrequency': timeseries_frequency}
)

predictor_arn_deep_ar = response['PredictorArn']
""",
'5':
"""
forecast_name = f'{project}_deep_ar'
response = forecast.create_forecast(
    ForecastName=forecast_name,
    PredictorArn=predictor_arn_deep_ar
)
forecast_arn_deep_ar = response['ForecastArn']
""",
'6':
"""
response = forecast_query.query_forecast(
    ForecastArn=forecast_arn_deep_ar,
    Filters={"item_id":item_id}
)
plot_forecasts(response, actual)
plt.title("DeepAR Forecast");
""",
'7':
"""
name = f'{project}_forecast_export_deep_ar_plus'
s3_path = f"{s3_data_path}/{name}"
response = forecast.create_forecast_export_job(
    ForecastExportJobName=name,
    ForecastArn=forecast_arn_deep_ar,
    Destination={
        "S3Config" : {
            "Path": s3_path,
             "RoleArn": role_arn
        }
    }
)

forecast_export_arn_deep_ar = response['ForecastExportJobArn']
"""
}