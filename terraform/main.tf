module "service_accounts" {
  source  = "terraform-google-modules/service-accounts/google"
  version = "4.5.4"
  project_id = var.project_id
  names = ["cloud-run-backend-sa"]
}
resource "google_project_iam_member" "service_account_roles" {
  for_each = toset([
    "roles/storage.objectAdmin",
    "roles/cloudsql.client",
    "roles/secretmanager.secretAccessor",
    "roles/aiplatform.user"
  ])

  project = var.project_id
  role    = each.key
  member  = "serviceAccount:${module.service_accounts.email}"
}
module "cloud_run_backend" {
  source = "github.com/GoogleCloudPlatform/cloud-foundation-fabric//modules/cloud-run?ref=master"
  project_id = var.project_id
  region     = var.region
  name       = "cloud-run-backend"
  containers = {
    backend = {
      image = "gcr.io/cloudrun/hello"
      port = 8080
    }
  }
 service_account = module.service_accounts.email
}

module "artifact-registry" {
  source  = "GoogleCloudPlatform/artifact-registry/google"
  version = "0.3.0"
  project_id    = var.project_id
  location      = var.region
  format        = "DOCKER"
  repository_id = "repo"
}
# module "sql-db" {
#   source  = "terraform-google-modules/sql-db/google//modules/mysql"
#   version = "25.2.2"
#   name                 = var.db_name
#   random_instance_name = true
#   database_version     = "MYSQL_5_6"
#   project_id           = var.project_id
#   zone                 = "me-west1-a"
#   region               = var.region
#   tier                 = "db-n1-standard-1"
# }
module "bucket" {
  source  = "terraform-google-modules/cloud-storage/google//modules/simple_bucket"
  version = "~> 11.0"
  name       = "bucket_${var.project_id}"
  project_id = var.project_id
  location   = var.region
  iam_members = [{
    role   = "roles/storage.objectViewer"
    member = "user:rachelge-aaaa@sandboxgcp.cloud"
  }]
}
module "create_sa_cloudbuild" {
  source               = "github.com/GoogleCloudPlatform/cloud-foundation-fabric//modules/iam-service-account"
  project_id           = var.project_id
  name                 = "sa-cloudbuild"
  service_account_create = true
  description          = "Service Account for Cloud Build"
  display_name         = "Cloud Build Service Account"
  iam_project_roles = {
    "${var.project_id}" = [
      "roles/cloudbuild.builds.editor",
      "roles/run.admin",
      "roles/artifactregistry.writer",
      "roles/logging.logWriter",
    ]
  }
  iam_sa_roles = {
    # "projects/${var.project_id}/serviceAccounts/${module.cloud_run_frontend.service_account_email}" = [
    #   "roles/iam.serviceAccountUser"
    # ],
    "projects/${var.project_id}/serviceAccounts/${module.cloud_run_backend.service_account_email}" = [
      "roles/iam.serviceAccountUser"
    ]
  }
}
module "cloudbuild_trigger_backend" {
  source       = "./module/cloud_build"
  project_id   = var.project_id
  trigger_name = "backend-trigger"
  trigger_path = "server/cloud-build-server.yaml"
  github_owner = "rg2023"
  github_repo  = "Project_"
  trigger_branch = "^master$"
  included_files = ["server/**"]
  service_account_email = module.create_sa_cloudbuild.email
 }

