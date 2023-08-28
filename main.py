import requests
from bs4 import BeautifulSoup


# def processJob(job): =


def main():
    url = "https://boards-api.greenhouse.io/v1/boards/gitlab/departments"
    response = requests.get(url)
    parsedResponse = response.json()
    for department in parsedResponse['departments']:
        for job in department['jobs']:
            data = {
                "title": job['title'],
                "location": job['location']['name'],
                "id": job['id'],
                "absolute_url": job['absolute_url'],
                "updated_at": job['updated_at'],
                "internal_job_id": job['internal_job_id'],
                "metadata": job['metadata'],
                "requisition_id": job['requisition_id'],
                "department": department['name'],
            }
            # processJob(data)


if __name__ == '__main__':
    main()
