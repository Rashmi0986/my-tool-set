import time
import requests

def poll_job_status(url, check_interval=5, timeout=60):
    """
    Polls the job status at the given URL until the job is complete or timeout occurs.
    
    :param url: The URL to check the job status.
    :param check_interval: The time interval (in seconds) between each poll.
    :param timeout: The maximum time (in seconds) to keep polling before giving up.
    :return: The job status response if completed within timeout, else None.
    """
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        response = requests.get(url)
        if response.status_code == 200:
            job_status = response.json().get('status')
            if job_status == 'completed':
                print("Job completed!")
                return response.json()
            elif job_status == 'failed':
                print("Job failed!")
                return response.json()
            else:
                print(f"Job status: {job_status}. Retrying in {check_interval} seconds...")
        else:
            print(f"Failed to fetch job status. HTTP Status Code: {response.status_code}")
        
        time.sleep(check_interval)
    
    print("Timeout occurred while waiting for the job to complete.")
    return None

# Example usage
job_status_url = "http://example.com/api/job/status"  # Replace with the actual URL
result = poll_job_status(job_status_url)
print("Result:", result)
