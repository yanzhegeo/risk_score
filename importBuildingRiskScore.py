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
        count = 0
        for row in reader:
            count += 1
            if count%10000==0:
                print (count)
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
    if (len(row) < 27):
        return
    if (row[25] == "NA"):
        row[25] = 0.0
    else:
        row[25] = float(row[23])
    data = {
        "location_name": row[0],
        "top_category": row[1],
        "latitude": float(row[2]),
        "longitude": float(row[3]),
        "street_address": row[4],
        "postal_code": row[5],
        "city": row[6],
        "community": row[7],
        "weekday": row[8],
        "open_hours": row[9],
        "area_square_feet": row[10],
        "infection_rate": row[11],
        "avg_visits": row[12],
        "avg_median_dwell": row[13],
        "cv": row[14],
        "peak": row[15],
        "interval": row[16],
        "encounter": row[17],
        "prob": row[18],
        "area_per_capita": row[19],
        "area_per_capita_perc_rank": row[20],
        "prob_perc_rank": row[21],
        "cv_perc_rank": row[22],
        "peak_perc_rank": row[23],
        "time_density_perc_rank": row[24],
        "risk_score": row[25],
        "risk_level": row[26]
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
    
    
    
