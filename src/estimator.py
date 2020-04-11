import math
from pprint import pprint

class Impact:
    def __init__(self, reportedCases, days, totalHospitalBeds, avgDailyIncomeInUSD, avgDailyIncomeInPopulation):
        self.reportedCases = reportedCases
        self.days = days
        self.totalHospitalBeds = totalHospitalBeds
        self.avgDailyIncomeInUSD = avgDailyIncomeInUSD
        self.avgDailyIncomeInPopulation = avgDailyIncomeInPopulation

    def currentlyInfected(self):
        infected = self.reportedCases * 10
        return infected

    def infectionsByRequestedTime(self):
        currentlyInfected = self.currentlyInfected()
        factors = daysToFactor(self.days)
        infections = currentlyInfected * 2 ** factors
        return infections

    def severeCasesByRequestedTime(self):
        infectionsByRequestedTime = self.infectionsByRequestedTime()
        severeCases = math.trunc((0.15 * infectionsByRequestedTime))
        return severeCases

    def hospitalBedsByRequestedTime(self):
        totalHospitalBeds = self.totalHospitalBeds
        severeCasesByRequestedTime = self.severeCasesByRequestedTime()
        hospitalBeds = totalHospitalBeds - (0.35 * severeCasesByRequestedTime)
        hospitalBeds = math.trunc(hospitalBeds)
        return hospitalBeds

    def casesForICUByRequestedTime(self):
        infectionsByRequestedTime = self.infectionsByRequestedTime()
        casesForICU = 0.05 * infectionsByRequestedTime
        casesForICU = math.trunc(casesForICU)
        return casesForICU

    def casesForVentilatorsByRequestedTime(self):
        infectionsByRequestedTime = self.infectionsByRequestedTime()
        casesForVentilators = 0.02 * infectionsByRequestedTime
        casesForVentilators = math.trunc(casesForVentilators)
        return casesForVentilators

    def dollarsInFlight(self):
        infectionsByRequestedTime = self.infectionsByRequestedTime()
        avgDailyIncomeInPopulation = self.avgDailyIncomeInPopulation
        avgDailyIncomeInUSD = self.avgDailyIncomeInUSD
        days = self.days
        dollars = round(infectionsByRequestedTime * avgDailyIncomeInPopulation * avgDailyIncomeInUSD * days, 2)
        return dollars


class SevereImpact:
    def __init__(self, reportedCases, days, totalHospitalBeds, avgDailyIncomeInUSD, avgDailyIncomeInPopulation):
        self.reportedCases = reportedCases
        self.days = days
        self.totalHospitalBeds = totalHospitalBeds
        self.avgDailyIncomeInUSD = avgDailyIncomeInUSD
        self.avgDailyIncomeInPopulation = avgDailyIncomeInPopulation

    def currentlyInfected(self):
        infected = self.reportedCases * 50
        return infected

    def infectionsByRequestedTime(self):
        currentlyInfected = self.currentlyInfected()
        factors = daysToFactor(self.days)
        infections = currentlyInfected * 2 ** factors
        return infections

    def severeCasesByRequestedTime(self):
        infectionsByRequestedTime = self.infectionsByRequestedTime()
        severeCases = math.trunc((0.15 * infectionsByRequestedTime))
        return severeCases

    def hospitalBedsByRequestedTime(self):
        totalHospitalBeds = self.totalHospitalBeds
        severeCasesByRequestedTime = self.severeCasesByRequestedTime()
        hospitalBeds = totalHospitalBeds - (0.35 * severeCasesByRequestedTime)
        hospitalBeds = math.trunc(hospitalBeds)
        return hospitalBeds

    def casesForICUByRequestedTime(self):
        infectionsByRequestedTime = self.infectionsByRequestedTime()
        casesForICU = 0.05 * infectionsByRequestedTime
        casesForICU = math.trunc(casesForICU)
        return casesForICU

    def casesForVentilatorsByRequestedTime(self):
        infectionsByRequestedTime = self.infectionsByRequestedTime()
        casesForVentilators = 0.02 * infectionsByRequestedTime
        casesForVentilators = math.trunc(casesForVentilators)
        return casesForVentilators

    def dollarsInFlight(self):
        infectionsByRequestedTime = self.infectionsByRequestedTime()
        avgDailyIncomeInPopulation = self.avgDailyIncomeInPopulation
        avgDailyIncomeInUSD = self.avgDailyIncomeInUSD
        days = self.days
        dollars = round(infectionsByRequestedTime * avgDailyIncomeInPopulation * avgDailyIncomeInUSD * days, 2)
        return dollars


def daysToFactor(days):
    factors = days / 3
    factors = math.trunc(factors)
    return factors


def dayFromPeriodType(periodType, timeToElapse):
    if periodType == "days":
        return timeToElapse
    if periodType == "weeks":
        return timeToElapse * 7
    if periodType == "months":
        return timeToElapse * 30


def estimator(data):
    inputData = data
    reportedCases = data["reportedCases"]
    timeToElapse = data["timeToElapse"]
    periodType = data["periodType"]
    totalHospitalBeds = data["totalHospitalBeds"]
    avgDailyIncomeInUSD = data["region"]["avgDailyIncomeInUSD"]
    avgDailyIncomeInPopulation = data["region"]["avgDailyIncomeInPopulation"]

    days = dayFromPeriodType(periodType, timeToElapse)
    impact = Impact(reportedCases, days, totalHospitalBeds, avgDailyIncomeInUSD, avgDailyIncomeInPopulation)
    severeImpact = SevereImpact(reportedCases, days, totalHospitalBeds, avgDailyIncomeInUSD, avgDailyIncomeInPopulation)

    impactData = \
        {
            "currentlyInfected": impact.currentlyInfected(),
            "infectionsByRequestedTime": impact.infectionsByRequestedTime(),
            "severeCasesByRequestedTime": impact.severeCasesByRequestedTime(),
            "hospitalBedsByRequestedTime": impact.hospitalBedsByRequestedTime(),
            "casesForICUByRequestedTime": impact.casesForICUByRequestedTime(),
            "casesForVentilatorsByRequestedTime": impact.casesForVentilatorsByRequestedTime(),
            "dollarsInFlight": impact.dollarsInFlight()
        }
    severeImpactData = \
        {
            "currentlyInfected": severeImpact.currentlyInfected(),
            "infectionsByRequestedTime": severeImpact.infectionsByRequestedTime(),
            "severeCasesByRequestedTime": severeImpact.severeCasesByRequestedTime(),
            "hospitalBedsByRequestedTime": severeImpact.hospitalBedsByRequestedTime(),
            "casesForICUByRequestedTime": severeImpact.casesForICUByRequestedTime(),
            "casesForVentilatorsByRequestedTime": severeImpact.casesForVentilatorsByRequestedTime(),
            "dollarsInFlight": severeImpact.dollarsInFlight()
        }

    data = \
        {
            "data":inputData,
			"estimate":{
				"impact": impactData,
				"severeImpact": severeImpactData
			}
        }
    return data
 
