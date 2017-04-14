#!/usr/bin/python
import time,requests,socket,json,argparse,sys
import graphitesend
from datetime import datetime
from influxdb import InfluxDBClient
import random

#Function to send data to graphite
def send_data_graphite(schema, backend_addr, backend_port, pmb_return):
	g=graphitesend.init(graphite_server=backend_addr, graphite_port=backend_port, lowercase_metric_names=True, system_name='', prefix='')
	g.send(schema+"."+"http_status",pmb_return["http_status_code"])
	g.send(schema+"."+"request_time",pmb_return["http_request_time"])
	g.send(schema+"."+"dns_lookup",pmb_return["dns_lookup"])
	g.send(schema+"."+"tcp_connection",pmb_return["tcp_connection"])
	g.send(schema+"."+"server_processing",pmb_return["server_processing"])
	g.send(schema+"."+"content_transfer",pmb_return["content_transfer"])
	if pmb_return["ssl"] == True:
		g.send(schema+"."+"tls_handshake",pmb_return["tls_handshake"])
		g.send(schema+"."+"ssl_days_left",pmb_return["ssl_days_left"])

#Function to send data to influxdb
def send_data_influxdb(backend_addr, backend_port, pmb_return, backend_user, bakend_pwd, backend_db):
	client = InfluxDBClient(backend_addr, backend_port, backend_user, backend_pwd, backend_db)
	current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
	client.write_points([{"measurement": "http_status","tags": {"host": payload["url"],"region": "" } ,"time": current_time,"fields": {"value": mb_return["http_status_code"]}}])
	client.write_points([{"measurement": "http_request_time","tags": {"host": payload["url"],"region": "" } ,"time": current_time,"fields": {"value": mb_return["http_request_time"]}}])
	client.write_points([{"measurement": "dns_lookup","tags": {"host": payload["url"],"region": "" } ,"time": current_time,"fields": {"value": mb_return["dns_lookup"]}}])
	client.write_points([{"measurement": "tcp_connection","tags": {"host": payload["url"],"region": "" } ,"time": current_time,"fields": {"value": mb_return["tcp_connection"]}}])
	client.write_points([{"measurement": "server_processing","tags": {"host": payload["url"],"region": "" } ,"time": current_time,"fields": {"value": mb_return["server_processing"]}}])
	client.write_points([{"measurement": "content_transfer","tags": {"host": payload["url"],"region": "" } ,"time": current_time,"fields": {"value": mb_return["content_transfer"]}}])
	if pmb_return["ssl"] == True:
		client.write_points([{"measurement": "tls_handshake","tags": {"host": payload["url"],"region": "" } ,"time": current_time,"fields": {"value": mb_return["tls_handshake"]}}])
		client.write_points([{"measurement": "ssl_days_left","tags": {"host": payload["url"],"region": "" } ,"time": current_time,"fields": {"value": mb_return["ssl_days_left"]}}])

#Variables declarations
cmd = ""
payload = {}

#Parsing arguments
parser = argparse.ArgumentParser(description='A Pingmeback client.', add_help=True)
parser.add_argument('-u', help='url to check', action='store', required=True)
parser.add_argument('-upmb', help='url of your pinmeback instance', required=True)
parser.add_argument('-p', help='pattern to check on the url', default="")
parser.add_argument('-i', help='insecure mod (boolean true or false) ', default="")
parser.add_argument('-t', help='time to respond to declare that the request timedout', default="")
parser.add_argument('-b', help='backend to send your data, default is graphite', default="graphite")
parser.add_argument('-s', help='schema to stored your data in graphite\n for example: customer.app.env.servername', default="test.test.prod.host.pingmeback")
parser.add_argument('-H', help='host of your backend, default is loaclhost', default="localhost")
parser.add_argument('-P', type=int, help='port of your backend, default is graphite port', default=2003)
parser.add_argument('-U', help='user of your backend')
parser.add_argument('-pwd', help='password of your backend')
parser.add_argument('-db', help='name of your backedn db')

#Feeding variables
args = parser.parse_args()
url_pingmeback=args.upmb
payload["url"]=args.u
if args.p != "":
	payload["pattern"]=args.p
if args.i != "":
	payload["insecure"]=args.i
if args.t != "":
	payload["timeout"]=args.t
backend=args.b
schema=args.s
backend_addr=args.H
backend_port=args.P
backend_db=args.db
backend_user=args.U
backend_pwd=args.pwd

#Open socket
#print json.dumps(payload)
r = requests.post(url_pingmeback, data=json.dumps(payload))
pmb_return=r.json()
if "message" in pmb_return:
	print (pmb_return["message"])
	sys.exit(0)

if backend == "graphite":
	send_data_graphite(schema, backend_addr, backend_port, pmb_return)

if backend == "influxdb":
	send_data_influxdb(backend_addr, backend_port, pmb_return, backend_user, bakend_pwd, backend_db)
