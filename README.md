# Python CI/CD on GCP

This repo is created to demontrate how to setup **CI/CD on GCP** and covers the below steps.

 1. Audit the packages installed
 2. Security scans by Sonar scanner
 3. Unittest
 4. Code coverage by Unittest
 5. Safety check for vulnerabilities
 6. Snyk.io scan for vulnerability check

## Files

 - *Dockerfile*
 - *cloudbuild.yaml*
 - src/
	 - *app.py*
	 - *requirements.txt*

## Dependencies

 - *gcp-cicd-security-scans*
 - *gcp-sonar-scanner*

Clone these Repos and follow the readme file under the respective repos for deployment.

## How trigger the pipeline automatically?
Enable Google Cloud Build for your repository. 
**Github > Market place > Google Cloud Build App > Enable.**

Setup build triggger under Google Cloud Project under Cloud Build for the repository.

## Command
Clone the Repo and run the below command on GCP Cloud shell.

    gcloud builds submit --config=cloudbuild.yaml
