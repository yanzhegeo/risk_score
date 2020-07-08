#!/usr/bin/python3
from pymongo import MongoClient
import pymongo
import csv
import urllib3
from datetime import datetime
import time

#mongo_client = MongoClient('mongodb://127.0.0.1:27017')

mongo_client = MongoClient('127.0.0.1:27017',
                            username='ruser',
                            password='flzx3qc',
                            authSource='COVID19-DB',
                            authMechanism='SCRAM-SHA-256')

db = mongo_client["COVID19-DB"]

building_riskscore = db["Building-RiskScore"]

def importBuildingRiskScore():
    with open('risk_score_updated.csv', newline='') as csvfile: 
        reader = csv.reader(csvfile, quotechar='"', delimiter=',',
                     quoting=csv.QUOTE_ALL, skipinitialspace=True)
        if reader is None:
            print("CSV File Error")
            return
        # Read the title and the date 
        titleInfo = next(reader)
        print(titleInfo)
        for row in reader:
            insertBuildingData(row)
    
    print("Import confirmed data is completed.")


"""
    location_name, 
    top_category, 
    latitude, 
    longitude, 
                        street_address,
                        weekday,
                        open_hours,
                        area_square_feet,
                        avg_visits,
                        avg_median_dwell,
                        infection_rate,
                        cv,
                        peak,
                        interval,
                        encounter,
                        prob,
                        area_per_capita,
                        area_per_capita_perc_rank,
                        prob_perc_rank,
                        cv_perc_rank,
                        peak_perc_rank,
                        time_density_perc_rank,
                        risk_score
"""

def insertBuildingData(row):
    if (len(row) < 24):
        return
    if (row[23] == "NA"):
        row[23] = 0.0
    else:
        row[23] = float(row[23])
    data = {
        "location_name": row[1],
        "top_category": row[2],
        "latitude": float(row[3]),
        "longitude": float(row[4]),
        "street_address": row[5],
        "weekday": row[6],
        "open_hours": row[7],
        "area_square_feet": row[8],
        "avg_visits": row[9],
        "avg_median_dwell": row[10],
        "infection_rate": row[11],
        "cv": row[12],
        "peak": row[13],
        "interval": row[14],
        "encounter": row[15],
        "prob": row[16],
        "area_per_capita": row[17],
        "area_per_capita_perc_rank": row[18],
        "prob_perc_rank": row[19],
        "cv_perc_rank": row[20],
        "peak_perc_rank": row[21],
        "time_density_perc_rank": row[22],
        "risk_score": row[23]
    }
    
    building_riskscore.insert_one(data)

def dropDataCollection():
    building_riskscore.drop()
    building_riskscore.create_index([('latitude', pymongo.ASCENDING)])
    building_riskscore.create_index([('longitude', pymongo.ASCENDING)])
    building_riskscore.create_index([('risk_score', pymongo.ASCENDING)])

if __name__ == '__main__':
    dropDataCollection()
    importBuildingRiskScore()
    
    
    
