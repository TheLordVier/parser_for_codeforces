import requests
from celery import shared_task

from parser.models import Problem


def request_data() -> dict:
    """Gets data about problems from codeforces.com"""
    url: str = "https://codeforces.com/api/problemset.problems"
    response = requests.get(url)

    if response.status_code == 200:
        vacancies = response.json()
        return vacancies['result']
    else:
        print("Error:", response.status_code)


@shared_task
def problem_data_create() -> None:
    """Adds problems to the db after parsing"""
    problem_data: dict = request_data()
    problem_db = []
    for p in problem_data['problems']:
        if Problem.objects.filter(problem_name=p['name']).count() == 0:
            problem = {'themes': ', '.join(p['tags']),
                       'number_solutions': int([pr['solvedCount'] for pr in problem_data['problemStatistics'] if
                                                pr['contestId'] == p['contestId'] and pr['number'] == p['number']][0]),
                       'problem_name': p['name'],
                       'number': p['number'],
                       'rating': None
                       }
            try:
                problem['rating'] = p['rating']
            except KeyError:
                pass
            problem_db.append(Problem(**problem))
    Problem.objects.bulk_create(problem_db)


def make_used_problem(problem_set: list) -> None:
    """Changes flag is_used to True when the problem is used in some contest"""
    for problem in problem_set:
        problem['is_used'] = True
        problem.save()
