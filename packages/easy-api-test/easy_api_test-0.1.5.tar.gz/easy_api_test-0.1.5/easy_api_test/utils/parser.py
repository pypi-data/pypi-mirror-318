

import json
import re


class CURLParser:

    def __init__(self, curl: str):
        self._curl = curl
        self._url = ''
        self._method = 'GET'
        self._headers = {}
        self._raw_data: str = ''
        self._data: dict | str | None = None
        self.parse()

    @property
    def url(self):
        return self._url
    
    @property
    def method(self):
        return self._method.upper()
    
    @property
    def headers(self):
        return self._headers
    
    @property
    def data(self):
        return self._data
    

    def is_start(self, i: int, s: str):
        if self._curl[i:i+len(s)] == s:
            return True
        return False

    def parse(self):
        c = re.compile(r' -[a-zA-Z\-]+ ')
        findIter = c.finditer(self._curl)
        pre_match = next(findIter)
        curl = self._curl[:pre_match.start()]
        self._url = curl[4:].strip().strip('"').strip('\'').strip()
        key = [self._curl[pre_match.start():pre_match.end()]]
        value = []
        for match in findIter:
            value.append(self._curl[pre_match.end():match.start()].strip().strip('"'))
            key.append(self._curl[match.start():match.end()].strip().strip('"'))
            pre_match = match
        else:
            value.append(self._curl[pre_match.end():].strip().strip('"'))
        for k, v in zip(key, value):
            if k == '-H':
                a, b = v.split(':', maxsplit=1)
                self._headers[a.strip().lower()] = b.strip()
            elif k == '--data-raw' or k == '--data' or k == '-D':
                self._raw_data = v.strip()
            elif k == '-X':
                self._method = v.strip().upper()
        if self._raw_data and self._method == 'GET':
            self._method = 'POST'
        
        if self._raw_data:
            if self._headers.get('content-type', '').startswith('application/x-www-form-urlencoded'):
                data = {k: v for k, v in [i.split('=') for i in self._raw_data.split('&')]}
            elif self._headers.get('content-type', '').startswith('multipart/form-data'):
                boundary = self._headers.get('content-type', '').split(';')[1].split('=')[1].strip()
                data = {}
                for i in map(str.strip, self._raw_data.split(f'--{boundary}')):
                    if not i:
                        continue
                    i = i[len('Content-Disposition: form-data;'):].strip().split('\n', maxsplit=1)
                    if len(i) != 2:
                        continue
                    name, value = map(str.strip, i)
                    name = name.split('=')[1].strip('"')
                    value = value.strip()
                    data[name] = value

            else:
                try:
                    data = json.loads(self._raw_data)
                except:
                    data = self._raw_data
            self._data = data


