# Databricks notebook source
import datetime

   

d1 =datetime.datetime(2022,3,15)
d2 =datetime.datetime(2022,6,21)

   

d1 - d2

   

d2 - d1

   

help(datetime.timedelta)

   

d1 + datetime.timedelta(10)
#Adds 10 days to d1
   

d1 + datetime.timedelta(-45)
#Subtracts 45 days from d1
   

d1 + datetime.timedelta(hours=12)
#Adds 12 hours to d1
   

d1 + datetime.timedelta(days = 2,hours=12)
#Adds 2 days and 12 hours to d1
   

d1.timestamp()

   

dt = datetime.datetime(1970,1,1)
print(dt)

   

dt.timestamp()
#This converts the datetime into seconds since 1970-01-01 00:00:00 UTC
   

dt.fromtimestamp(1)
#Convert timestamp = 1 second into a datetime

   

