import unittest
import json
from app import app
from database import init_db
from seed_data import seed_all

class TestHirePrepPlatform(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        seed_all()
        cls.client = app.test_client()

    def test_01_index_page(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'LMT JOBS', res.data)
        self.assertIn(b'Job Explorer', res.data)

    def test_02_dashboard_stats(self):
        res = self.client.get('/api/dashboard/stats')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertGreater(data['total_jobs'], 0)
        self.assertGreater(data['total_dsa'], 0)
        self.assertIn('dsa_breakdown', data)

    def test_03_jobs_api(self):
        # Fetch all
        res = self.client.get('/api/jobs')
        self.assertEqual(res.status_code, 200)
        jobs = res.get_json()
        self.assertGreater(len(jobs), 0)

        # Filter by type
        res_filter = self.client.get('/api/jobs?type=Full-time')
        self.assertEqual(res_filter.status_code, 200)
        filtered = res_filter.get_json()
        self.assertTrue(all(j['job_type'] == 'Full-time' for j in filtered))

        # Search
        res_search = self.client.get('/api/jobs?search=Google')
        self.assertEqual(res_search.status_code, 200)
        searched = res_search.get_json()
        self.assertTrue(any('Google' in j['company'] for j in searched))

    def test_04_job_apply_and_applications(self):
        res_jobs = self.client.get('/api/jobs')
        all_jobs = res_jobs.get_json()
        unapplied_job = next(j for j in all_jobs if j['application_status'] is None)

        res = self.client.post('/api/jobs/apply', json={
            'job_id': unapplied_job['id'],
            'name': 'Test User',
            'email': 'test.user@example.com',
            'portfolio': 'https://github.com/testuser',
            'resume_name': 'Test_Resume.pdf',
            'notes': 'Looking forward to interviewing!'
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])

        # Verify in applications list
        res_apps = self.client.get('/api/applications')
        self.assertEqual(res_apps.status_code, 200)
        apps = res_apps.get_json()
        self.assertTrue(any(a['candidate_email'] == 'test.user@example.com' for a in apps))

    def test_05_prep_topics_and_quiz(self):
        res = self.client.get('/api/prep/topics')
        self.assertEqual(res.status_code, 200)
        topics = res.get_json()
        self.assertGreater(len(topics), 0)

        # Get quiz questions
        res_quiz = self.client.get('/api/prep/quiz')
        self.assertEqual(res_quiz.status_code, 200)
        quiz = res_quiz.get_json()
        self.assertGreater(len(quiz), 0)

        # Submit quiz
        first_q = quiz[0]
        res_submit = self.client.post('/api/prep/quiz/submit', json={
            'answers': {str(first_q['id']): 0}
        })
        self.assertEqual(res_submit.status_code, 200)
        result = res_submit.get_json()
        self.assertEqual(result['total'], 1)
        self.assertIn('percentage', result)

    def test_06_companies_and_eligibility(self):
        res = self.client.get('/api/companies')
        self.assertEqual(res.status_code, 200)
        comps = res.get_json()
        self.assertGreater(len(comps), 0)

        # Check eligibility for TCS (id=3 or search TCS)
        tcs = next(c for c in comps if c['name'] == 'TCS')
        res_elig = self.client.post('/api/companies/check-eligibility', json={
            'company_id': tcs['id'],
            'cgpa': 7.8,
            'branch': 'CSE',
            'backlogs': 0
        })
        self.assertEqual(res_elig.status_code, 200)
        elig_data = res_elig.get_json()
        self.assertTrue(elig_data['is_eligible'])

    def test_07_dsa_sheet_and_progress(self):
        res = self.client.get('/api/dsa/sheet')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertGreater(len(data['problems']), 0)
        self.assertGreater(len(data['topics_summary']), 0)

        # Update problem status and notes
        first_prob = data['problems'][0]
        res_status = self.client.post('/api/dsa/status', json={
            'problem_id': first_prob['id'],
            'status': 'solved',
            'notes': 'Test note: Optimal hashmap approach verified.'
        })
        self.assertEqual(res_status.status_code, 200)

if __name__ == '__main__':
    unittest.main()
