'''Read in the census data and produce JSON output of the right quantities'''

import csv
import json

def fix(s):
    try:
        return int(s)
    except:
        return s

def grab(f, key='Estimate'):
    out = {}
    ff = open(f)
    for i in xrange(3): ff.next()
    for row in csv.DictReader(ff):
        out[row['Id2']] = fix(row[key])
    return out

def grab_distribution(f):
    out = {}
    ff = open(f)
    for i in xrange(5): ff.next()
    for row in csv.reader(ff):
        id2 = row[1]
        data = row[3::2]
        out[id2] = map(int,data)
    return out

def main():
    json.dump(grab('census_data/ACS_10_5YR_median_household_income.csv'), open('census_data/m_hhi.json','w'))
    json.dump(grab('census_data/ACS_10_5YR_gini.csv'), open('census_data/gini.json','w'))
    json.dump(grab('census_data/ACS_10_5YR_gini.csv', 'Geography'), open('census_data/names.json','w'))
    json.dump(grab_distribution('census_data/ACS_10_5YR_household_income.csv'), open('census_data/hhi_distribution.json','w'))

if __name__ == "__main__":
    main()
        

