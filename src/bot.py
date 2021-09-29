import requests
import json
from time import sleep

class AnswerBot():


    def __init__(self, jwt='', book='', baseUrl=''):
        self.jwt = jwt
        self.baseUrl = baseUrl
        self.book = book
        self.baseRequest = {
            "operationName": "",
            "query": "",
            "variables": {
                "id": ""
            }
        }

        self.exercises = []

        self.session = requests.Session()
        self.session.headers = dict()
        self.session.headers["Content-Type"] = 'application/json'
        self.session.headers['User-JWT'] = self.jwt


    def getBookExercises(self):
        self.baseRequest["operationName"] = 'bookEdition'
        self.baseRequest["query"] = 'query bookEdition($id: ID!) {\n  bookEdition(id: $id) {\n    id\n    name\n    solvedPercentage\n    amplitudeName\n    book {\n      id\n      name\n      author\n      imagePath\n      volume\n      theme {\n        id\n        name\n        __typename\n      }\n      editions {\n        id\n        __typename\n      }\n      __typename\n    }\n    chapters {\n      id\n      name\n      sections {\n        id\n        name\n        questions {\n          id\n          name\n          exercise {\n            id\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n'
        self.baseRequest["variables"]["id"] = self.book
        response = self.session.post(self.baseUrl, data=json.dumps(self.baseRequest), allow_redirects=True)
        if (response.status_code == 200):
            chapters = json.loads(response.content.decode('utf-8'))["data"]["bookEdition"]["chapters"]

            for chapter in chapters:
                for section in chapter["sections"]:
                    for question in section["questions"]:
                        self.exercises.append({
                            "id":question["exercise"]["id"],
                            "name": question["name"] + ' - Cap ' + chapter["name"] + ' Section ' + section["name"]
                        })
        else:
            print("> Bad Request")


    def getExercisesSolution(self):
        self.baseRequest["operationName"] = 'bookExercise'
        self.baseRequest["query"] = 'query bookExercise($id: ID!) {\n  bookExercise(id: $id) {\n    id\n    solution\n    answer\n    topic {\n      id\n      name\n      subject {\n        id\n        name\n        __typename\n      }\n      theory {\n        id\n        __typename\n      }\n      exercises {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n'

        with open('book.html', 'a') as outfile:
            for ex in self.exercises:
                currentSolution = f"<h1>{ex['name']}</h1>"

                self.baseRequest["variables"]["id"] = ex["id"]
                ok = False
                response = None
                while not ok:
                    try:
                        response = self.session.post(self.baseUrl, data=json.dumps(self.baseRequest), allow_redirects=True)
                        ok = True
                    except:
                        pass

                if (response.status_code == 200):
                    exercise = json.loads(response.content.decode('utf-8'))["data"]["bookExercise"]
                    for solution in exercise["solution"]:
                        currentSolution += solution

                    currentSolution += exercise["answer"]
                    outfile.write(currentSolution)
                    print(f"> {ex['name']} mapped!")
                    sleep(0.1)
            outfile.close()


    def start(self):
        self.getBookExercises()
        self.getExercisesSolution()

