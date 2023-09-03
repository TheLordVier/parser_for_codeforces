from rest_framework import status
from rest_framework.test import APITestCase

from .models import Problem


class ProblemTestCase(APITestCase):
    def setUp(self) -> None:
        """
        Create test db
        """
        self.url = '/parser/'
        self.data = {
            'themes': 'test',
            'number_solutions': 20,
            'problem_name': 'test',
            'number': '12345',
        }
        self.problem = Problem.objects.create(**self.data)

    def test_create_problem(self) -> None:
        """
        Problem creation testing
        """
        response = self.client.post(f'{self.url}add_problems/')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(Problem.objects.all().count(), 0)

    def test_list_problem(self) -> None:
        """Problem list testing """
        response = self.client.get(f'{self.url}problems/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'problem_name': 'test', 'rating': None, }]
        )

    def test_retrieve_problem(self) -> None:
        """
        Problem retrieve testing
        """
        response = self.client.get(f'{self.url}problems/{self.problem.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'problem_name': 'test', 'rating': None, 'themes': 'test', 'number_solutions': 20, 'number': '12345'}
        )


# import pytest
# from rest_framework import status
# from parser.models import Problem
#
#
# @pytest.mark.django_db
# def test_create_problem(api_client):
#     """Problem creation testing """
#
#     response = api_client.post('/parser/add_problems/')
#
#     assert response.status_code == status.HTTP_201_CREATED
#     assert Problem.objects.all().count() != 0
#
#
# @pytest.mark.django_db
# def test_list_problems(api_client, sample_problem):
#     """Problem list testing """
#
#     response = api_client.get('/parser/problems/')
#
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == [
#         {'problem_name': 'Sample Problem', 'rating': 5, 'themes': 'sample theme', 'number_solutions': 10,
#          'number': '12345'}]
#
#
# @pytest.mark.django_db
# def test_retrieve_problem(api_client, sample_problem):
#     """Problem retrieve testing """
#
#     response = api_client.get(f'/parser/problems/{sample_problem.pk}/')
#
#     assert response.status_code == status.HTTP_200_OK
#
#     assert response.json() == {'problem_name': 'Sample Problem', 'rating': 5, 'themes': 'sample theme',
#                                'number_solutions': 10, 'number': '12345'}
