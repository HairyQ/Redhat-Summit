import paho.mqtt.client as mqtt
from multiprocessing import Process
import optparse, time, json

files = [
    'plane_data/non-anomalous.csv',
    'plane_data/anomalous.csv',
    'plane_data/non-anomalous_2.csv',
    'plane_data/non-anomalous_3.csv',
    'plane_data/non-anomalous_4.csv']

realtime = False
metadata = [
    'temperature',
    'temperature',
    'temperature',
    'temperature',
    'pressure',
    'pressure',
    'pressure',
    'pressure',
    'pressure',
    'pressure',
    'pressure',
    'rpm',
    'rpm',
    'pps']

devices = []
devices_J1 = [
    'ciUBz09nEsey0tM7peyq', # LPCT - 4
    'PU8ohI0w1olGkuk7hgrm', # HPCT - 3
    'vw45fpot44bwjk193icd', # HPTT - 1
    'IxvfunLWTvE4hJqUCsV9', # LPTT - 2
    'Uwq153N6XF0ekKCxsVld', # BPD  - 5
    'wjKLFHDcwhhGiSyaGJOQ', # FIP  - 6
    'GPiUbpDqfzLinuisMhj7', # FOP  - 7
    'gvQLAoF6hONTzB4xcg1W', # LPCP - 8
    '8TRGHiHXjjNb0h6P6Wx3', # HPCP - 9
    'afKooROhFfU7SLeqmgrP', # BOP  - 10
    'yoX8zZGyDJoSyRaG0BSL', # LPTP - 11
    'CaseRrKucnG6nR6rGrgj', # FRT  - 12
    '74AIbAwL5lB60RIetPOl', # CRT  - 13
    'e1dMAagkrj8L3P6clpNy'] # FF   - 14

devices_J2 = [
    'KWy8Xp1Az3dBHRyIJMfJ', # LPCT - 4
    'BtSbjxjeZHjcZZ0TNHtY', # HPCT - 3
    'rBmB4YlYX41YumguKcDX', # HPTT - 1
    'fLxOzRIhByMG1gvH1tCi', # LPTT - 2
    'iUvTv2QzPYonlxBMMBq1', # BDP - 5
    '2upbgbp9YRZCaGq2jVbi', # FIP - 6
    'ywWYkzCPIHKT5tHXxRb3', # FOP - 7
    'Q9VlK1OK3l6w2tpy7pmN', # LPCP - 8
    'r3fgaGd2gWwLlvMfQTAt', # HPCP - 9
    '0rylcqhDli1fCzijYxNC', # BOP - 10
    'raa2yw0JOEArKFsNLE1e', # LPTP - 11
    'EZwwgxeX2oAI4pXKjJXj', # FRT - 12
    'Cf8aKFlGaJg8arin64dD', # CRT - 13
    'AoDhes4z8QEgQAQL0Wzl'] # FF - 14

devices_J3 = [
    'DyZWoaYC2hKDZ7tPRSZr', # LPCT - 4
    'NMCL097frehlVUOctDAd', # HPCT - 3
    'fPIF1ut5bdzwju9Qc7W5', # HPTT - 1
    'DCrVn2Me7zxhe9546BHM', # LPTT - 2
    'ptA60S9E0hA0iU2l40gL', # BPD  - 5
    '19utEJk03wofNdFPYJfZ', # FIP  - 6
    'RWPNQrG4MqjjyodtR4cM', # FOP  - 7
    'eTViS3PQcGauE1oSQRpG', # LPCP - 8
    'sDd3gU5R4IiopUu4KvPi', # HPCP - 9
    '74hKT1BfZUXW47YCKQGn', # BOP  - 10
    'MkG1kUjkxhjDYvUqo8kk', # LPTP - 11
    'NgOX2dVXo0iyyPZChWwW', # FRT  - 12
    '6vj7gtn5r7mdh8hmdip1', # CRT  - 13
    'j3v0j87zf5joa1gfqynd'] # FF   - 14

devices_J4 = [
    'EA9UbjvvfZooMu9opKMV', # LPCT - 4
    'EUPZxnW07QVj2npRrxZe', # HPCT - 3
    'y99qxBFQUj3ZQPvzeNJX', # HPTT - 1
    'ELJsroeWykSCHIN5ujfZ', # LPTT - 2
    'kI8OJTO3oxtWT7YZE1GF', # BDP - 5
    'imvXnGaFF4BJMR9MLnOe', # FIP - 6
    'MLsg6VfZ4M90wsbBQWD7', # FOP - 7
    '69XntbQ9s8LL1gE2EKow', # LPCP - 8
    'FTihj5m5SqpgcmJ7GZYK', # HPCP - 9
    'SoxAh1pafMcrArcvGEB8', # BOP - 10
    '44IScrePVa8nWHxNRqAN', # LPTP - 11
    'KedkubZNwzW4LCynqJ9M', # FRT - 12
    '8VQlFCbczhpiZ9AtL2GG', # CRT - 13
    'Wiuz4y0QQSIkE6Yi97FI'] # FF - 14

devices_J5 = [
    'wq37h82wg5f3ozdbc5n8', # LPCT - 4
    'zo028iu178lvdhieue4n', # HPCT - 3
    '8oAjfmMvu1MUJSMZKnxB', # HPTT - 1
    'kP1lJLWwUEQkYhSVyDTG', # LPTT - 2
    '79ewumn4iu1lv1bio3t4', # BDP - 5
    'VMpaRudUCWz8hT7W3f9o', # FIP - 6
    'Rifo4Mf5cmYpG7ceD2qI', # FOP - 7
    'zh19d5z8ntqki455hmvw', # LPCP - 8
    'EERGcjtFJlyMGZUj5XEJ', # HPCP - 9
    'bPhUMw1gZdo4XivZ6hvZ', # BOP - 10
    'HaREBfOJotebpomeqIb0', # LPTP - 11
    'b7EUmWwqNXVMO4jznGjx', # FRT - 12
    'fj4n6eymofd8f75gf3f4', # CRT - 13
    'zAHF6CUAoYFMtlsDjfXv'] # FF - 14

devices.append(devices_J1)
devices.append(devices_J2)
devices.append(devices_J3)
devices.append(devices_J4)
devices.append(devices_J5)

broker_address = 'tb-route-mttq-transport-thingsboard.apps.thingsboard.openshift.solutions'
broker_port = 30864

client_list = []
for j in range(len(devices)):
    clients = []
    for i in range(14):
        client = mqtt.Client()
        client.username_pw_set(devices[j][i])
        client.connect(broker_address, broker_port, 120)
        clients.append(client)
    client_list.append(clients)

parser = optparse.OptionParser()
parser.add_option('-r', '--realtime', dest='realtime', default=False,
                  help='Use this flag to run this program in real time rather than as a batch',
                  action='store_true')

options, args = parser.parse_args()
if options.realtime:
    realtime = options.realtime
    
def reader_func(file_name, clients):
    total_rows = 0
    with open(file_name) as f:
        total_rows = sum(1 for line in f)
    
    current_time_ms = round(time.time() * 1000)
    time_step = current_time_ms - (total_rows * 1000)

    if realtime:
        with open(file_name) as f:
            l = 0
            for line in f:
                terms = line.strip().split(',')
                i = 0
                time_step = round(time.time() * 1000)
                for term in terms:
                    msg = json.dumps({"ts":time_step, "values":{metadata[i]:term}})
                    clients[i].publish('v1/devices/me/telemetry', msg, 0)
                    i += 1
                l += 1
                if file_name == 'plane_data/non-anomalous_4.csv':
                    print(l)
                time.sleep(1)

    else:
        with open(file_name) as f:
            l = 0
            for line in f:
                terms = line.strip().split(',')
                i = 0
                time_step += 1000
                for term in terms:
                    msg = json.dumps({"ts":time_step, "values":{metadata[i]:term}})
                    clients[i].publish('v1/devices/me/telemetry', msg, 0)
                    i += 1
                l += 1
                if file_name == 'plane_data/non-anomalous_4.csv':
                    print(l)
                time.sleep(0.1)

    return;

# Deploy on 1 process per jet engine file
procs = []
for i in range(len(client_list)):
    proc = Process(target=reader_func, args = (files[i], client_list[i]))
    i += 1
    procs.append(proc)
    proc.start()

# Harvest the processes
for proc in procs:
    proc.join()
