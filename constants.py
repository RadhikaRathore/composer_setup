#Project Configurations
project_name='urbn-edw-dev'
#database_host='35.237.28.94'
database_host='35.227.80.115'
database_username='postgres'
database_password='India@1234'
database_name='EDW'
database_port='5432'
#for testing purpose
jobname_postfix = "test"

#Clone Database Config.
database_host_clone='35.227.80.115'
database_username_clone='postgres'
database_password_clone='India@1234'
database_name_clone='EDW'
database_port_clone='5432'

#template_bucket
template_bucket = 'urbn-template-test'

#Axper Dags Constants
axper_job_name='real-time-traffic-etl'
axper_bucket='axper-test'
axper_template='RealTimeTrafficETL'
axper_client_secret='8f091390bbe94ab7af9b95c3075f2c73'
axper_username='CRMAlerts@urbanout.com'
axper_password='TomBrady4Lyfe!'
axper_anthropologie_client_secret='a9e03c798f3641b1922f129684cedd74'
axper_freepeople_client_secret='a066794e95ad458699870b3bde362d75'
AXPER_temp_location = "gs://{bucket}/dataflow/RealTimeTrafficETL/template/tmp".format(bucket=template_bucket)
AXPER_GCSPATH = "gs://{bucket}/dataflow/RealTimeTrafficETL/template/{template}".format(bucket=template_bucket, template=axper_template)

#Darksky Dags Constants
darksky_bucket_name='darksky-test'
darksky_job_name='real-time-weather-etl'
darksky_bucket='darksky-test'
darksky_template='RealTimeWeatherTemplate'
darksky_storage='raw/stores/'
darksky_temp_location = "gs://{bucket}/dataflow/realtimeweather/template/tmp".format(bucket=template_bucket)
DARKSKY_GCSPATH= "gs://{bucket}/dataflow/realtimeweather/template/{template}".format(bucket=template_bucket, template=darksky_template)

#Darksky API KEY
darksky_api_key_old='2d54f6973dae1aca940dbb371cac7eb7'
darksky_api_key_new='308dd01a25402df3300fe7ac6b21bf7f'

#Darksky-LY Dags Constants
darksky_LY_bucket_name='darksky-test'
darksky_LY_job_name='ly-weather-etl'
darksky_LY_bucket='darksky-test'
darksky_LY_template='LYWeatherETL'
darksky_LY_storage = 'raw/stores-LY/'

#Darksky-LY GCSPATH and BODY:
DARKSKY_LY_GCSPATH="gs://{bucket}/dataflow/LYWeatherETL/template/{template}".format(bucket=template_bucket, template=darksky_LY_template)
DARKSKY_LY_BODY = {
        "jobName": "{jobname}".format(jobname=darksky_LY_job_name)+jobname_postfix,
        "environment": {
            "tempLocation": "gs://{bucket}/dataflow/LYWeatherETL/template/tmp".format(bucket=template_bucket),
            "zone": "us-east1-b"
        }
    }

#constants for body
zone = "us-east1-b"
input_param_name = "inputData"



#DailyHitLookUpTable
UPDATE_CLASS_LOOKUP_QUERY='select UPDATECLASSLOOKUP()'
UPDATE_DIVISION_LOOKUP_QUERY='select UPDATEDIVISIONLOOKUP()'
UPDATE_PLAN_BRAND_LOOKUP_QUERY='select UPDATEPLANBRANDLOOKUP()'
UPDATE_STYLE_LOOKUP_QUERY='select UPDATESTYLELOOKUP()'
UPDATE_STORE_LOOKUP_QUERY='select UPDATESTORELOOKUP()'

#OnceHitLookUpTable
UPDATE_DATE_LOOKUP_QUERY='select UPDATEDATELOOKUP()'
UPDATE_HOUR_LOOKUP_QUERY='select UPDATEHOURLOOKUP()'

#DailyTriggerDataflowTemplate
DWCCYETL_JOBNAME='dw-ccy-composer'
DWCCYETL_TEMPLATE='DW_CCY_Template'
DWCCYETL_INPUT_DATA={"sourceTable":"urbn.DW_CCY", "sinkTable":"urbn_netezza.DW_CCY","uniqueConstraint":"PK_DW_CCY","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWCCYETL_BUCKET='urbn-template-test'
DWCCYETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_CCY_Template'
DWCCYETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWCCYSYMBOLETL_JOBNAME='dw-ccy-symbol-etl'
DWCCYSYMBOLETL_TEMPLATE='DW_CCY_SYMBOL_Template'
DWCCYSYMBOLETL_INPUT_DATA={"sourceTable":"urbn.DW_CCY_SYMBOL", "sinkTable":"urbn_netezza.DW_CCY_SYMBOL","uniqueConstraint":"PK_DW_CCY_SYMBOL","isSync":"true","columns":"*"}
DWCCYSYMBOLETL_BUCKET='urbn-template-test'
DWCCYSYMBOLETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_CCY_SYMBOL_Template'
DWCCYSYMBOLETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWLOCSTRETL_JOBNAME='dw-loc-str-etl'
DWLOCSTRETL_TEMPLATE='DW_LOC_STR_Template'
DWLOCSTRETL_INPUT_DATA={"sourceTable":"urbn.DW_LOC_STR", "sinkTable":"urbn_netezza.DW_LOC_STR","uniqueConstraint":"PK_DW_LOC_STR","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWLOCSTRETL_BUCKET='urbn-template-test'
DWLOCSTRETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_LOC_STR_Template'
DWLOCSTRETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWLOCSTRINFOETL_JOBNAME='dw-loc-str-info-etl'
DWLOCSTRINFOETL_TEMPLATE='DW_LOC_STR_INFO_Template'
DWLOCSTRINFOETL_INPUT_DATA={"sourceTable":"urbn.DW_LOC_STR_INFO", "sinkTable":"urbn_netezza.DW_LOC_STR_INFO","uniqueConstraint":"PK_DW_LOC_STR_INFO","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWLOCSTRINFOETL_BUCKET='urbn-template-test'
DWLOCSTRINFOETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_LOC_STR_INFO_Template'
DWLOCSTRINFOETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWPRDCLSETL_JOBNAME='dw-prd-cls-etl'
DWPRDCLSETL_TEMPLATE='DW_PRD_CLS_Template'
DWPRDCLSETL_INPUT_DATA={"sourceTable":"urbn.DW_PRD_CLS", "sinkTable":"urbn_netezza.DW_PRD_CLS","uniqueConstraint":"PK_DW_PRD_CLS","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWPRDCLSETL_BUCKET='urbn-template-test'
DWPRDCLSETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_PRD_CLS_Template'
DWPRDCLSETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWPRDDMMETL_JOBNAME='dw-prd-dmm-etl'
DWPRDDMMETL_TEMPLATE='DW_PRD_DMM_Template'
DWPRDDMMETL_INPUT_DATA={"sourceTable":"urbn.DW_PRD_DMM", "sinkTable":"urbn_netezza.DW_PRD_DMM","uniqueConstraint":"PK_DW_PRD_DMM","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWPRDDMMETL_BUCKET='urbn-template-test'
DWPRDDMMETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_PRD_DMM_Template'
DWPRDDMMETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWCCYXRTETL_JOBNAME='dw-ccy-xrt-etl'
DWCCYXRTETL_TEMPLATE='DW_CCY_XRT_Template'
DWCCYXRTETL_INPUT_DATA={"sourceTable":"urbn.DW_CCY_XRT", "sinkTable":"urbn_netezza.DW_CCY_XRT","uniqueConstraint":"PK_DW_CCY_XRT","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWCCYXRTETL_BUCKET='urbn-template-test'
DWCCYXRTETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_CCY_XRT_Template'
DWCCYXRTETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWPRDSKUETL_JOBNAME='dw-prd-sku-etl'
DWPRDSKUETL_TEMPLATE='DW_PRD_SKU_Template'
DWPRDSKUETL_INPUT_DATA={"sourceTable":"urbn.DW_PRD_SKU", "sinkTable":"urbn_netezza.DW_PRD_SKU","uniqueConstraint":"PK_DW_PRD_SKU","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWPRDSKUETL_BUCKET='urbn-template-test'
DWPRDSKUETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_PRD_SKU_Template'
DWPRDSKUETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWPRDSTYETL_JOBNAME='dw-prd-sty-etl'
DWPRDSTYETL_TEMPLATE='DW_PRD_STY_Template'
DWPRDSTYETL_INPUT_DATA={"sourceTable":"urbn.DW_PRD_STY", "sinkTable":"urbn_netezza.DW_PRD_STY","uniqueConstraint":"PK_DW_PRD_STY","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWPRDSTYETL_BUCKET='urbn-template-test'
DWPRDSTYETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_PRD_STY_Template'
DWPRDSTYETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWTIMEZONETBLETL_JOBNAME='dw-timezone-tbl-etl'
DWTIMEZONETBLETL_TEMPLATE='DW_TIMEZONE_TBL_Template'
DWTIMEZONETBLETL_INPUT_DATA={"sourceTable":"urbn.DW_TIMEZONE_TBL", "sinkTable":"urbn_netezza.DW_TIMEZONE_TBL","uniqueConstraint":"PK_DW_TIMEZONE_TBL","isSync":"true","syncDbColumnName":"DATETIME_TIME_START","columns":"*"}
DWTIMEZONETBLETL_BUCKET='urbn-template-test'
DWTIMEZONETBLETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_TIMEZONE_TBL_Template'
DWTIMEZONETBLETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWSLSTRANSACTIONTYPEETL_JOBNAME='dw-sls-transactiontype-etl'
DWSLSTRANSACTIONTYPEETL_TEMPLATE='DW_SLS_TRANSACTIONTYPE_Template'
DWSLSTRANSACTIONTYPEETL_INPUT_DATA={"sourceTable":"urbn.DW_SLS_TRANSACTIONTYPE", "sinkTable":"urbn_netezza.DW_SLS_TRANSACTIONTYPE","uniqueConstraint":"PK_DW_SLS_TRANSACTIONTYPE","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWSLSTRANSACTIONTYPEETL_BUCKET='urbn-template-test'
DWSLSTRANSACTIONTYPEETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_SLS_TRANSACTIONTYPE_Template'
DWSLSTRANSACTIONTYPEETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

#WeeklyTriggerDataflowTemplate
DWD2CTXNDTLTEMPLATE_JOBNAME='dw-d2c-txn-dtl-db-migration'
DWD2CTXNDTLTEMPLATE_TEMPLATE='DW_D2C_TXN_DTL_Template'
#DWD2CTXNDTLTEMPLATE_INPUT_DATA={"sourceTable":"urbn.DW_D2C_TXN_DTL", "sinkTable":"urbn_netezza.DW_D2C_TXN_DTL","uniqueConstraint":"PK_DW_D2C_TXN_DTL","isRangeQuery":"true","rangeColumnName":"Q_DT_ID","startRange":str(startDate),"endRange":str(endDate),"isSync":"false","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWD2CTXNDTLTEMPLATE_BUCKET='urbn-template-test'
DWD2CTXNDTLTEMPLATE_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_D2C_TXN_DTL_Template'
DWD2CTXNDTLTEMPLATE_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWSLSSKUSTRDTEMPLATE_JOBNAME='dw-sls-sku-str-d-db-migration-etl'
DWSLSSKUSTRDTEMPLATE_TEMPLATE='DW_SLS_SKU_STR_D_Template'
#DWSLSSKUSTRDTEMPLATE_INPUT_DATA={"sourceTable":"urbn.DW_SLS_SKU_STR_D", "sinkTable":"urbn_netezza.DW_SLS_SKU_STR_D","uniqueConstraint":"PK_DW_SLS_SKU_STR_D","isRangeQuery":"true","rangeColumnName":"Q_DT_ID","startRange":str(startDate),"endRange":str(endDate),"isSync":"false","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWSLSSKUSTRDTEMPLATE_BUCKET='urbn-template-test'
DWSLSSKUSTRDTEMPLATE_GCSPATH='gs://{bucket}/dataflow/realtimeweather/template/{template}'
DWSLSSKUSTRDTEMPLATE_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWSLSTXNDTLTEMPLATE_JOBNAME='dw-sls-txn-dtl-db-migration-etl'
DWSLSTXNDTLTEMPLATE_TEMPLATE='DW_SLS_TXN_DTL_Template'
#DWSLSTXNDTLTEMPLATE_INPUT_DATA={"sourceTable":"urbn.DW_SLS_TXN_DTL", "sinkTable":"urbn_netezza.DW_SLS_TXN_DTL","uniqueConstraint":"PK_DW_SLS_TXN_DTL","isRangeQuery":"true","rangeColumnName":"Q_DT_ID","startRange":str(startDate),"endRange":str(endDate),"isSync":"false","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWSLSTXNDTLTEMPLATE_BUCKET='urbn-template-test'
DWSLSTXNDTLTEMPLATE_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_SLS_TXN_DTL_Template'
DWSLSTXNDTLTEMPLATE_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWSLSTXNHDRTEMPLATE_JOBNAME='dq-sls-txn-hdr-db-migration-etl'
DWSLSTXNHDRTEMPLATE_TEMPLATE='DW_SLS_TXN_HDR_Template'
#DWSLSTXNHDRTEMPLATE_INPUT_DATA={"sourceTable":"urbn.DW_SLS_TXN_HDR", "sinkTable":"urbn_netezza.DW_SLS_TXN_HDR","uniqueConstraint":"PK_DW_SLS_TXN_HDR","isRangeQuery":"true","rangeColumnName":"Q_DT_ID","startRange":str(startDate),"endRange":str(endDate),"isSync":"false","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWSLSTXNHDRTEMPLATE_BUCKET='urbn-template-test'
DWSLSTXNHDRTEMPLATE_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_SLS_TXN_HDR_Template'
DWSLSTXNHDRTEMPLATE_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWTRFTEMPLATE_JOBNAME='dw-trf-db-migration-etl'
DWTRFTEMPLATE_TEMPLATE='DW_TRF_Template'
#DWTRFTEMPLATE_INPUT_DATA={"sourceTable":"urbn.DW_TRF", "sinkTable":"urbn_netezza.DW_TRF","uniqueConstraint":"PK_DW_TRF","isRangeQuery":"true","rangeColumnName":"Q_DT_ID","startRange":str(startDate),"endRange":str(endDate),"isSync":"false","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWTRFTEMPLATE_BUCKET='urbn-template-test'
DWTRFTEMPLATE_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_TRF_Template'
DWTRFTEMPLATE_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

#OnceTriggerDataflowTemplate
DWCALDTETL_JOBNAME='dw-cal-dt-etl'
DWCALDTETL_TEMPLATE='DW_CAL_DT_Template'
DWCALDTETL_INPUT_DATA={"sourceTable":"urbn.DW_CAL_DT", "sinkTable":"urbn_netezza.DW_CAL_DT","uniqueConstraint":"PK_DW_CAL_DT","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWCALDTETL_BUCKET='urbn-template-test'
DWCALDTETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_CAL_DT_Template'
DWCALDTETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWCALTIMEETL_JOBNAME='dw-cal-time-etl'
DWCALTIMEETL_TEMPLATE='DW_CAL_TIME_Template'
DWCALTIMEETL_INPUT_DATA={"sourceTable":"urbn.DW_CAL_TIME", "sinkTable":"urbn_netezza.DW_CAL_TIME","uniqueConstraint":"PK_DW_CAL_TIME","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWCALTIMEETL_BUCKET='urbn-template-test'
DWCALTIMEETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_CAL_TIME_Template'
DWCALTIMEETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

DWCALTIME1HETL_JOBNAME='dw-cal-time-1h-etl'
DWCALTIME1HETL_TEMPLATE='DW_CAL_TIME_1H_Template'
DWCALTIME1HETL_INPUT_DATA={"sourceTable":"urbn.DW_CAL_TIME_1H", "sinkTable":"urbn_netezza.DW_CAL_TIME_1H","uniqueConstraint":"PK_DW_CAL_TIME_1H","isSync":"true","syncDbColumnName":"LOAD_DATE","columns":"*"}
DWCALTIME1HETL_BUCKET='urbn-template-test'
DWCALTIME1HETL_GCSPATH='gs://urbn-template-test/dataflow/Template/DW_CAL_TIME_1H_Template'
DWCALTIME1HETL_TEMP_LOCATION='gs://urbn-template-test/dataflow/Template/tmp'

#Trigger SQL Scripts
PLAN_BRAND_USD_FUNCTION_TABLENAME='URBN_POSTGRESQL.PLAN_BRAND_USD_FUNCTION'
PLAN_BRAND_STORE_CURRENCY_FUNCTION_TABLENAME='URBN_POSTGRESQL.PLAN_BRAND_STORE_CURRENCY_FUNCTION'
DIVISION_USD_FUNCTION_TABLENAME='URBN_POSTGRESQL.DIVISION_USD_FUNCTION'
DIVISION_STORE_CURRENCY_FUNCTION_TABLENAME='URBN_POSTGRESQL.DIVISION_STORE_CURRENCY_FUNCTION'
CLASS_USD_FUNCTION_TABLENAME='URBN_POSTGRESQL.CLASS_USD_FUNCTION'
CLASS_STORE_CURRENCY_FUNCTION_TABLENAME='URBN_POSTGRESQL.CLASS_STORE_CURRENCY_FUNCTION'
HOUR_SALES_USD_TABLENAME='URBN_POSTGRESQL.HOUR_SALES_USD'
HOUR_SHIPPED_USD_TABLENAME='URBN_POSTGRESQL.HOUR_SHIPPED_USD'
HOUR_DEMAND_USD_TABLENAME='URBN_POSTGRESQL.HOUR_DEMAND_USD'
HOUR_SALES_STORE_CURRENCY_TABLENAME='URBN_POSTGRESQL.HOUR_SALES_STORE_CURRENCY'
HOUR_SHIPPED_STORE_CURRENCY_TABLENAME='URBN_POSTGRESQL.HOUR_SHIPPED_STORE_CURRENCY'
HOUR_DEMAND_STORE_CURRENCY_TABLENAME='URBN_POSTGRESQL.HOUR_DEMAND_STORE_CURRENCY'
HOUR_TRAFFIC_FUNCTION_TABLENAME='URBN_POSTGRESQL.HOUR_TRAFFIC_FUNCTION'
WEATHER_DAY_FUNCTION_TABLENAME='URBN_POSTGRESQL.WEATHER_DAY_FUNCTION'
UPDATE_CONVERSION_TABLENAME='URBN_POSTGRESQL.UPDATE_CONVERSION'
DATA_DELETE_FUNCTION_TABLENAME='URBN_POSTGRESQL.DATA_DELETE_FUNCTION'
