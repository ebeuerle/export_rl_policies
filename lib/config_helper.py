import os
import yaml


class ConfigHelper(object):
    def __init__(self):
        config = self.read_yml('configs')
        self.rl_user = config["redlock"]["username"]
        self.rl_pass = config["redlock"]["password"]
        self.rl_cust = config["redlock"]["customer_name"]


    @classmethod
    def read_yml(self, f):
        yml_path = os.path.join(os.path.dirname(__file__), "../config/%s.yml" % f)
        return yaml.load(file(yml_path, 'r'))
