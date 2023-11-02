INSERT INTO employers VALUES (%s, %s, %s)
INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)
SELECT emp_title, vacancy_count FROM employers
SELECT emp_title, vac_title, salary_from, salary_to, url FROM vacancies INNER JOIN employers USING (employer_id)
SELECT emp_title, ROUND(AVG(salary_from)) FROM vacancies INNER JOIN employers USING (employer_id) WHERE salary_from > 0 GROUP BY emp_title
SELECT vac_title, url FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)
SELECT vac_title, url FROM vacancies WHERE vac_title LIKE '%ython%'