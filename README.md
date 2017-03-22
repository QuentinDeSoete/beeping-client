# pingmeback-python-client v0.1.0

This is a simple client to use with [Pingmeback] (https://github.com/yanc0/pingmeback) made by YancO.
You can use this client in a cron or with [dkron] (http://dkron.io) to check the response time of your website and the validity of your SSL certificates.
The client will redirect the Pingmeback return in a backend theat you will specified (graphite by default)

## Usage

The minimal command to use this client is :
```
./pingmeback-client.py -u example.site.com -upmb host.instance.pingmeback.com 
```
You need to specify twoo parameters :
	* the '-u' wich is the url of the website that you want to check.
	* the -'upmb' wich is the url or ip to reach your Pingmeback instance.
 
You have other parameters that you can specify like :
	* the '-p' wich is a string that Pingmeback will check on your page, it's usefull to check if your website has been hacked or not
	* the '-i' wich is the insecure mod, if your SSL certificate is deprecated or broken set this to true to still have check
	* the '-t' wich is the timeout, it is the time after wich Pingmecack will tell you that your website had a timeout (default is 20 sec)
	* the '-b' wich is the backend that you want to send your data to, the default backend is set to [graphite] (http://graphite.readthedocs.io)
	* the '-s' wich is the schema under wich you want to set your data in graphite for example
	* the '-H' wich is the host of your backend, the default value is localhost
	* the '-P' wich is the port of your backend, the default value is 2003

Example to change your backend host and port :
```
./pingmeback-client.py -u example.site.com -upmb host.instance.pingmeback.com -H backend.example.com -P 42
```

Example to change the schema that you want to send to graphite :
```
./pingmeback-client.py -u example.site.com -upmb host.instance.pingmeback.com -s customer.app.env.servername.pingmeback
```

## To Do

- [ ] Add other backend

## Contributing

Feel free to make a pull request.

## Licence

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
