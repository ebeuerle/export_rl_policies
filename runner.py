import lib
import json

class PolicyExport():
    def __init__(self):
        self.config = lib.ConfigHelper()
        self.csv_writer = lib.CsvWriter()
        self.rl_sess = lib.RLSession(self.config.rl_user,self.config.rl_pass,self.config.rl_cust)
        self.output = [["PolicyName", "Description", "CloudType", "RQL"]]

    def build(self):
        self.url = "https://api.redlock.io/policy"
        self.rl_sess.authenticate_client()
        response = self.rl_sess.client.get(self.url)
        #write out the top of csv to file
        self.csv_writer.write(self.output)
        json_response = response.json()
        for policydata in json_response:
            #filter out anomoly policies(3) and built-in ones(2) since they don't contain RQL
            if policydata["policyId"] in (
                                          "e12e1edc-3018-11e7-93ae-92361f002671", 
                                          "e12e210c-3018-11e7-93ae-92361f002671", 
                                          "e12e1b44-3018-11e7-93ae-92361f002671",
                                          "49f4760d-c951-40e4-bfe1-08acaa17672a",
                                          "05befc8b-c78a-45e9-98dc-c7fbaef580e7"):
               continue
            self.rql_url = "https://api.redlock.io/search/history/%s" % policydata["rule"]["criteria"]
            rql_resp = self.rl_sess.client.get(self.rql_url)
            json_rql_resp = rql_resp.json()
            data = [policydata["name"],policydata["description"],policydata["cloudType"],json_rql_resp["query"]]
	    encoded_data = [x.encode('utf-8') for x in data]
            self.csv_writer.append([encoded_data])

    def run(self):
        self.build()

def main():
    rl_policyexport = PolicyExport()
    rl_policyexport.run()


if __name__ == "__main__":
    main()
