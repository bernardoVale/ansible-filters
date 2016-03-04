from ansible import errors
import re

def oratab(oratab_content):
    sid_list = []
    try:
        for line in oratab_content.strip().split('\n'):
            if not str(line).startswith('#'):
                parse_oratab = re.match(r"(\w*):(\/\S*):([Y|N])", line)

                if parse_oratab:
                    sid = parse_oratab.group(1)
                    #oracle_home = parse_oratab.group(2)
                    sid_list.append(sid)
                    #sid_list.append(oracle_home)
    except Exception, e:
        raise errors.AnsibleFilterError('oratab plugin error: %s' % str(e))

    return sid_list

class FilterModule(object):
    ''' A filter to split a string into a list. '''
    def filters(self):
        return {
            'oratab' : oratab,
        }