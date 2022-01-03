from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

from datetime import datetime 
from ipaddress import * 
from wmi import * 

import subprocess, socket 
import smtplib, sys, os 
import platform, psutil 
import getpass, time 

import json, csv
import yaml, xml 

def ConvertIPv4ToIPv6(ipv4):
    return IPv6Address('2002::' + ipv4)

