from doscon_tb_api.doscon_tb_api import tb_connector
import json
import os
import datetime
base_path = os.path.dirname(__file__)


credentials = {}
#with open("credentials.json") as infile:
#    credentials = json.load(infile)
test_device_id = os.environ["tb_api_test_device"]          
test_asset_id = os.environ["tb_api_test_asset_id"]
credentials["username"] = os.environ["dosmon_user"] 
credentials["password"] = os.environ["dosmon_pw"]
credentials["url"] = os.environ["dosmon_url"]


def test_connect_incorrect_credentials():
    connector = tb_connector(credentials["url"],credentials["username"],"wrongpassword")
    assert connector.connect() == False

def test_connect_correct_credentials():
    connector = tb_connector(credentials["url"],credentials["username"],credentials["password"])
    assert connector.connect() == True

def test_getUserDevices():
    connector = tb_connector(credentials["url"],credentials["username"],credentials["password"])
    connector.connect()
    result = connector.getUserDevices()
    assert result.status_code == 200

def test_getTimeSeriesKeys():
    connector = tb_connector(credentials["url"],credentials["username"],credentials["password"])
    connector.connect()
    result = connector.getTimeSeriesKeys(test_device_id)
    assert result.status_code == 200

def test_readCsv():
    connector = tb_connector(credentials["url"],credentials["username"],credentials["password"])
    filePath = os.path.join(base_path,"testfiles","standard_csv_us_latin1.csv")
    dataFrame = connector.readCsv(filePath,datetimeColumn="Timeline",encoding="latin-1")
    assert "æøå" in dataFrame.columns

def test_getAssetInfoById():
    connector = tb_connector(credentials["url"],credentials["username"],credentials["password"])
    connector.connect()
    result = connector.getAssetInfoById(test_asset_id)
    assert result.status_code == 200

def test_getAssetsByIds():
    connector = tb_connector(credentials["url"],credentials["username"],credentials["password"])
    connector.connect()
    result = connector.getAssetsByIds(f"{test_asset_id},{test_asset_id}")
    assert result.status_code == 200

def test_getAllAssetInfos():
    connector = tb_connector(credentials["url"],credentials["username"],credentials["password"])
    connector.connect()
    result = connector.getAllAssetInfos(6,2, "ASC", "name")
    assert result.status_code == 200

def test_getAssetProfiles():
    connector = tb_connector(credentials["url"],credentials["username"],credentials["password"])
    connector.connect()
    result = connector.getAssetProfiles(6,2, "ASC", "name")
    assert result.status_code == 200

def test_getTimeSeriesData():
    connector = tb_connector(credentials["url"],credentials["username"],credentials["password"])
    connector.connect()
    sPointTs = datetime.datetime(2024,6,11,14,50,00)
    ePointTs = datetime.datetime(2024,6,9,14,50,00)
    result = connector.getTimeSeriesData(test_device_id, ["sensor"], sPointTs, ePointTs)
    assert result.status_code == 200