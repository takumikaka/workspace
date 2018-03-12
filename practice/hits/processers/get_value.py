# -*- coding: utf-8 -*-

from processers.get_html import getHtml
import config

########################################################################

class getValue(object):
    def __init__(self):
        self.get_html = getHtml()
        self.eid = config.EID

    def get_value(self, data):
        hits_data = data.get('hits', []).get('hits')
        for i in hits_data:
            for key, value in i.items():
                if key == '_source' and value.get('default', {}).get('eid') == self.eid:
                    value_k = value

        return value_k

    def run(self):
        data = self.get_html.run()
        value = self.get_value(data)
        value = value.get('default', {})
        return value


########################################################################
def main():
    action = getValue()
    action.run()

if __name__=='__main__':
    main()
