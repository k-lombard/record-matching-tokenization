import csv
import json
def solution(csvfile, jsonfile):
    with open(csvfile, 'r') as f:
        data = list(csv.reader(f))

    with open(jsonfile) as f:
        data2 = json.load(f)

    recordMatch = {}

    for entry in data2:
        recordMatch[(entry['employer'] + entry['firstName'] + entry['lastName']).lower()] = entry

    output = {}
    for num in range(1,len(data)):
        payment = data[num]
        mask = payment[2].replace('*', '')
        token = (payment[0] + payment[3] + payment[4]).lower()
        paid = float(payment[1])
        if token in recordMatch:
            if (mask != "" and str(recordMatch[token]['mask']) == mask) or mask == "":
                if token not in output:
                    outDict = {}
                    outDict["username"] = recordMatch[token]['username']
                    outDict["applied"] = paid
                    outDict["owe"] = float(recordMatch[token]['amountExpected']) - paid
                    output[token] = outDict
                else:
                    output[token]["applied"] = float(output[token]["applied"]) + paid
                    output[token]["owe"] = float(output[token]["owe"]) - paid
    jsonOut = list(output.values())
    with open('application.json', 'w') as outfile:
        json.dump(jsonOut, outfile)
csvfile = 'payments.csv'
jsonfile = 'db.json'
test1 = 'testpayments.csv'
test2 = 'testdb.json'
solution(csvfile, jsonfile)