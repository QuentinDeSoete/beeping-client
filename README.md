# beeping-client v0.3.0

This is a simple client to use with [beeping](https://github.com/yanc0/beeping) made by YancO.
You can use this client in a cron or with [dkron](http://dkron.io) to check the response time of your website and the validity of your SSL certificates.
The client will redirect the Pingmeback return in a backend that you will specified (graphite by default)

Thanks to :
* YancO for his good work on [beeping](https://github.com/yanc0/beeping)
* daniellawrence for his good librairie [graphitesend](https://github.com/daniellawrence/graphitesend)

## Requirements

* [graphitesend](https://github.com/daniellawrence/graphitesend)
* [requests](http://docs.python-requests.org/en/master/user/install/)
* [influxdb](https://github.com/influxdata/influxdb-python)
* [prometheus/client_python](https://github.com/prometheus/client_python#custom-collectors)

## Usage

The minimal command to use this client is :
```
./beeping-client.py -u example.site.com -upmb host.instance.beeping.com 
```
You need to specify two parameters :
* the '-u' which is the url of the website that you want to check.
* the -'upmb' which is the url or ip to reach your Pingmeback instance.
 
You have other parameters that you can specify like :
* the '-p' which is a string that beeping will check on your page, it's useful to check if your website has been hacked or not
* the '-i' which is the insecure mod, if your SSL certificate is deprecated or broken set this to true to still have check
* the '-t' which is the timeout, it is the time after which Pingmeback will tell you that your website had a timeout (default is 20 sec)
* the '-b' which is the backend that you want to send your data to, the default backend is set to [graphite](http://graphite.readthedocs.io)
* the '-s' which is the schema under which you want to set your data in graphite for example
* the '-H' which is the host of your backend, the default value is localhost
* the '-P' which is the port of your backend, the default value is 2003
* the '-U' which is the user of your backend if you need to be loged in like in influxdb
* the '-pwd' which is the password of your backend if you need to be logged in like in influxdb
* the '-db' which is the database where you want to store your data (required for influxdb)

Example to change your backend host and port :
```
./beeping-client.py -u example.site.com -upmb host.instance.beeping.com -H backend.example.com -P 42
```

Example to change the schema that you want to send to graphite :
```
./beeping-client.py -u example.site.com -upmb host.instance.beeping.com -s customer.app.env.servername.beeping
```

## To Do

- [x] Add support for influxdb
- [x] Add support for prometheus
- [ ] Add support for datadog
- [ ] Add support for opentsdb

## Contributing

Feel free to make a pull request.

## Licence

```
MIT License

Copyright (c) 2017 QuentinDeSoete

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
