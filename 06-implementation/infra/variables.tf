variable "subscription_id" {
  description = "Azure subscription ID"
  type        = string
}
variable "location" {
  type    = string
  default = "australiaeast"
}
variable "resource_group_name" {
  type    = string
  default = "rg-enterprise-rag-demo"
}
variable "log_analytics_name" {
  type    = string
  default = "log-enterprise-rag-demo"
}
variable "environment_name" {
  type    = string
  default = "cae-enterprise-rag-demo"
}
variable "app_name" {
  type    = string
  default = "ca-enterprise-rag-demo"
}
variable "image" {
  description = "Container image accessible to Azure Container Apps"
  type        = string
}
