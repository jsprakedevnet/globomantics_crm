#!/usr/bin/env python

class Database:

    def __init__(self, path):
        """
    Consturctor to initialize the data attribute as
    a dictionary where the account number is the key and
    the value is another dictionary with keys "paid" and "due".
        """
        #Open the specified databse file for reading and perform loading
        """
        with open(path, "r") as handle:
            import json
            self.data = json.load(handle)
        """
        """
        with open(path, "r") as handle:
            import yaml
            self.data = yaml.safe_load(handle)
        """
        with open(path, "r") as handle:
            import xmltodict
            self.data = xmltodict.parse(handle.read())["root"]
            print(self.data)


    def balance(self, acct_id):
        acct = self.data.get(acct_id)
        if acct:
            return int(acct["due"]) - int(acct["paid"])
        return None
