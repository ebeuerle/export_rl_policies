import lib
import json

class PolicyExport():
    def __init__(self):
        self.config = lib.ConfigHelper()
        self.csv_writer = lib.CsvWriter()
        self.rl_sess = lib.RLSession(self.config.rl_user,self.config.rl_pass,self.config.rl_cust, self.config.rl_api_base)
        self.output = [["PolicyName", "Description", "CloudType", "RQL"]]

    def build(self):
        self.url = "https://" + self.config.rl_api_base + "/policy"
        self.rl_sess.authenticate_client()
        response = self.rl_sess.client.get(self.url)
        #write out the top of csv to file
        self.csv_writer.write(self.output)
        json_response = response.json()
        for policydata in json_response:
            if policydata.get('rule').get('criteria'):
                pass
            else:
                continue
            if policydata.get('rule').get('criteria') in ("network_anomaly", "portsweep_network_anomaly", "unusual_port_proto_network_anomaly", "uba_anomaly", "brute_force_anomaly"):
                continue
            if len(policydata.get('rule').get('criteria')) == 36:
                self.rql_url = "https://" + self.config.rl_api_base + "/search/history/%s" % policydata["rule"]["criteria"]
                rql_resp = self.rl_sess.client.get(self.rql_url)
                json_rql_resp = rql_resp.json()
                rql_query = json_rql_resp["query"]
            else:
                rql_query = policydata.get('rule').get('criteria')
#            print(policydata['policyId'])
#            print(rql_query)
            data = [policydata["name"],policydata["description"],policydata["cloudType"],rql_query]
            encoded_data = [x.encode('utf-8') for x in data]
            self.csv_writer.append([encoded_data])

    def run(self):
        self.build()

def main():
    rl_policyexport = PolicyExport()
    rl_policyexport.run()


if __name__ == "__main__":
    main()
