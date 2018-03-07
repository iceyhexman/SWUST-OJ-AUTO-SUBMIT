import requests
import os
import time

PROBLEM_START_ID = 220  # 问题开始id
PROBLEM_END_ID = 250  # 问题结束id

header = {"Cookie": "JSESSIONID=C2764EBBF6F7202695C183D029A0CB4D; csrftoken=9Ewq4gYCCt390r6oDzYuFihzlmcHem82; UM_distinctid=",
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIiLCJzdWJtaXRDb3VudCI6MCwic3VibWl0VGltZSI6bnVsbCwicm9sZUlkIjo0LCJpc3MiOiJTd3VzdE9KX0pXVCIsInZhaWxkQ29kZSI6bnVsbCwiZXhwIjoxNTIwNDM0MDI1LCJ1c2VySWQiOjg4ODIsImlhdCI6MTUyMDQxMjQyNSwiQ0xBU1NfVFlQRSI6Im9yZy5rZWxhYi5zd3VzdG9qLmNvbnN0YW50Lkpzb25XZWJUb2tlbkNvbnN0YW50JEpzb25XZWJUb2tlbkNsYWltcyIsInVzZXJuYW1lIjoiaGV4bWFuIn0.Ch42dwbbbs9J5Fev5LGRVxKaqpsHHk_VK1xcg4ckNJo"}


class autosubmit(object):

    def __init__(self,problem_end_id=PROBLEM_END_ID,problem_start_id=PROBLEM_START_ID, header=header):
        self.problem_id=problem_end_id
        self.header=header
        self.problem_testdata_path = os.getcwd()
        self.problem_start_id = problem_start_id
        self.templet = ""
        self.input = []
        self.output = []

    def submit(self):
        for i in range(self.problem_start_id, self.problem_id + 1):
            self.input = []
            self.output = []
            with open("%s/%d/config" % (self.problem_testdata_path,i)) as fconfig:
                for testdata in range(int(fconfig.read())):
                    with open('%s/%s/%s.in' % (self.problem_testdata_path, str(i), str(testdata))) as inputdata:
                        self.input.append(len(inputdata.readlines()))
                    with open('%s/%s/%s.out' % (self.problem_testdata_path, str(i), str(testdata))) as outputdata:
                        self.output.append(outputdata.read())
                self.templet = "import sys\ninputvalue=%s\noutputvalue=%s\nfor i in range(len(inputvalue)):\n    for s in range(inputvalue[i]):\n        raw_input()\n    sys.stdout.write(outputvalue[i])" % (str(self.input),str(self.output))
            json = {"source": self.templet, "problemId": str(i), "compilerId": 5, "contestId": "-1"}
            r = requests.post("http://acm.swust.edu.cn/api/submit.do", headers=self.header, json=json)
            print("NOW SUBMITTING NO.%d" % i)
            time.sleep(2)  # 等待oj判题，否则一下子几页waiting


a=autosubmit()
a.submit()
