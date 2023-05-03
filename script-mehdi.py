import pandas as pd
import openpyxl
from openpyxl.styles import (PatternFill, colors)
from openpyxl import Workbook
import os
import os.path
import win32com.client
from datetime import datetime
from time import sleep
import time
#import logging

i = 0
outlook = win32com.client.Dispatch("Outlook.Application")
mapi = outlook.Session
folder= mapi.Folders['Besma.Rakrouki2@dxc.com'].Folders['test']
items = folder.Items
types  = "wfm_report"
caseID = ""                                                    

def sendMail(agentMail, receivers, subj, text) :
        try :   
                mail = outlook.CreateItem(0)                
                mail.Subject = subj
                mail.To = agentMail
                mail.Body = text     
                mail.CC = receivers            
                time.sleep(1)
                mail.send()    
                print("Mail was Sent")     
        except :
                print("Issue to send mail!")
                   
                             

                                                                                                     

def again() :      
                empty = False 
                i = 0
                while i < 1 :
                        datenow = datetime.now()
                        datetimeNow = datenow.strftime('%Y-%m-%d %H:%M:%S')
                        businessHour = datenow.strftime('%H')
                        businessHour = str(businessHour)  
                        businessDay = datenow.strftime('%A')                        
                        time.sleep(1)
                        items.Sort("[ReceivedTime]", True) 
                        for item in list(items) :                                   
                                datenow = datetime.now()
                                datetimeNow = datenow.strftime('%Y-%m-%d %H:%M:%S')
                                businessHour = datenow.strftime('%H')
                                businessHour = str(businessHour)  
                                businessDay = datenow.strftime('%A')                                    
                                datenow = datenow.strftime('%d/%m/%Y %H:%M:%S')   
                                leng = len(folder.Items)  
                                print(item)   
                                print("len : " + str(leng))                                                   
                                if len(folder.Items) == 0 :                                 
                                        if empty == False  :    
                                                print('date Now : ' + str(datetimeNow))                             
                                                print ('Mail box is empty!!!\n')
                                                print ('**********************') 
                                                empty = True  
                                        else :  
                                                again()  
                                                
                                else :      
                                        empty = False                                                                                
                                        time.sleep(1)            
                                        attachments = item.Attachments           
                                        bodyMess = item.Body                                                   
                                        sender = item.SenderEmailAddress 
                                        senderName = str(item.Sender)                   
                                        receivedDate = item.SentOn 
                                        receivedDate = receivedDate.strftime('%d_%m_%Y_%H_%M_%S')
                                        text = '• Description : Script WFM \r\n mail.number : ' + str(leng)
                                        attachments = item.Attachments
                                        
                                        for attachment in attachments:     
                                                file = os.path.splitext(str(attachment))[0][1:]         
                                                attachment.SaveASFile("C:\\" + str(attachment) + '_' + str(receivedDate) + ".xlsx")  
                                                print(attachment)                                           
                                                time.sleep(3)
                                                print(i)
                                                i= i + 1
                                                if (i >= leng) :
                                                        sendMail("besma.rakrouki2@dxc.com", "besma.rakrouki2@dxc.com", "Script Notification", text)
                                                        print("Job End!")
                                                        time.sleep(5)
                                                        break
                                                                                       
                        
                        time.sleep(5)
again()
try:
        logging.critical("SCRIPT BEGAN  LOG") 
        print("SCRIPT BEGAN") 
        again()
except Exception as e:
        print("Error Exception occured : " + str(e)) 
        sendMail("besma.rakrouki2@dxc.com", "besma.rakrouki2@dxc.com", str(e), str(e))
        raise
