#!/usr/bin/env python
# coding:utf-8
from SalesforceConnector.RestClient import SfaConnection

def main():
    print("Login to Salesforce using JWT...")

    sfa_c = SfaConnection()
    # sfa_c.jwt_login()
    print("Login successful!")
    limits = sfa_c.GetLimitsInfo()
    print("Current API usage limits:", limits)

if __name__ == "__main__":
    main()