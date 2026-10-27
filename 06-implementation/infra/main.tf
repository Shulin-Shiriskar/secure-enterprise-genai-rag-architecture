terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}

resource "azurerm_resource_group" "demo" {
  name     = var.resource_group_name
  location = var.location
  tags     = { project = "enterprise-rag-portfolio", environment = "demo" }
}

resource "azurerm_log_analytics_workspace" "demo" {
  name                = var.log_analytics_name
  location            = azurerm_resource_group.demo.location
  resource_group_name = azurerm_resource_group.demo.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "azurerm_container_app_environment" "demo" {
  name                       = var.environment_name
  location                   = azurerm_resource_group.demo.location
  resource_group_name        = azurerm_resource_group.demo.name
  log_analytics_workspace_id = azurerm_log_analytics_workspace.demo.id
}

resource "azurerm_container_app" "demo" {
  name                         = var.app_name
  container_app_environment_id = azurerm_container_app_environment.demo.id
  resource_group_name          = azurerm_resource_group.demo.name
  revision_mode                = "Single"

  template {
    min_replicas = 0
    max_replicas = 1
    container {
      name   = "rag-demo"
      image  = var.image
      cpu    = 0.5
      memory = "1Gi"
      env {
        name  = "ANSWER_MODE"
        value = "extractive"
      }
    }
  }
  ingress {
    external_enabled = false
    target_port      = 8000
    transport        = "auto"
    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }
}
