import ipywidgets as widgets
from IPython.display import display, Markdown, Code, HTML

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
            "AttributeName": "price", 
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
response = forecast.create_predictor(
    PredictorName = predictor_name,
    AlgorithmArn = algorithm_arn,
    ForecastHorizon = forecast_horizon,
    PerformAutoML = False,
    PerformHPO = False,
    InputDataConfig = {'DatasetGroupArn': dataset_group_arn},
    FeaturizationConfig = {'ForecastFrequency': timeseries_frequency}
)
""",
'5':
"""
forecast_name = f'{project}_prophet'
response = forecast.create_forecast(
    ForecastName=forecast_name,
    PredictorArn=predictor_arn_prophet
)
""",
'6':
"""
response = forecast_query.query_forecast(
    ForecastArn=forecast_arn_prophet,
    Filters={"item_id":item_id}
)
""",
'7':
"""
response = forecast.create_forecast_export_job(
    ForecastExportJobName=name,
    ForecastArn=forecast_arn_prophet,
    Destination={
        "S3Config" : {
            "Path": s3_path,
             "RoleArn": role_arn
        }
    }
)
"""
}