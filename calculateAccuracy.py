import jwt
import sys
import requests

if len(sys.argv) != 5:
    print "Usage: python calculateAccuracy.py <APPID> <TOKEN> <EncodingAESKey> <InputFile>"
    exit()

APPID = sys.argv[1]
TOKEN = sys.argv[2]
EncodingAESKey = sys.argv[3]

fin = open(sys.argv[4], 'r')

correct_count = 0; total_count = 0
for line in fin.readlines():
    query, ground_truth_intent = line.strip().split('\t')

    # encode data
    data = {"username": "1", "msg": query}
    signed_data = jwt.encode(data, EncodingAESKey, "HS256")

    # send request
    r = requests.post("https://openai.weixin.qq.com/openapi/message/%s?query=%s" % (TOKEN, signed_data))

    # extract returned intent
    response = r.json()
    test_intent = response["title"]
    if ground_truth_intent == test_intent.encode('utf8'):
        correct_count += 1
    total_count += 1

print "accuracy:", float(correct_count)/total_count
