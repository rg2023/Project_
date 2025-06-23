provider "google" {
  project = var.project_id
  region  = var.region
  impersonate_service_account = var.sa_email_to_impersonate
}
terraform {
  backend "gcs" {
    bucket  = "gcs-terraform---state"
    prefix  = "terraform/state"
  }
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.1"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "~> 6.1"
    }
  }
  required_version = ">= 1.3.0"
}
  
