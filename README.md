# Grafana Deployment with Python, Jenkins, Terraform, and Microsoft Teams Integration

This repository automates the deployment of **Grafana** on a Kubernetes cluster, with alerts for **HTTP 400 response ratios**. It integrates **Terraform**, **Prometheus**, **Microsoft Teams**, and **Jenkins** to provide end-to-end automation with monitoring, alerting, and notifications.

## Project Structure

```
grafana-deployment/
│
├── Jenkinsfile            # Jenkins pipeline configuration
├── main.tf                # Terraform configuration for Grafana and Kubernetes resources
├── terraform_apply.sh     # Script to apply Terraform configurations and install Python dependencies
├── alerts.yml             # Prometheus alerting rules
├── prometheus.yml         # Prometheus configuration for scraping web application metrics
├── send_teams_alert.py    # Python script to send alerts to Microsoft Teams
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Prerequisites

1. **Kubernetes Cluster** with `kubectl` configured.
2. **Prometheus** and **Grafana** installed or configured via this project.
3. **Terraform** installed: [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli).
4. **Jenkins** installed with **GitHub Integration**.
5. **Python 3.x** installed along with **pip**.
6. **Microsoft Teams** webhook URL for notifications.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/<your-repo>.git
    cd grafana-deployment
    ```

2. Set up Microsoft Teams webhook and update alert configurations.

3. Run Terraform:
    ```bash
    ./terraform_apply.sh
    ```

4. Verify deployment and trigger alerts with simulated HTTP 400 errors.

## License

This project is licensed under the MIT License.
