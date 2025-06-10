import streamlit as st
import psutil
import time
import matplotlib.pyplot as plt

# Function to collect real-time system metrics
def get_system_metrics():
    metrics = {
        "CPU Usage": psutil.cpu_percent(interval=1),
        "Memory Usage": psutil.virtual_memory().percent,
        "Disk Usage": psutil.disk_usage('/').percent,
        "Network Traffic": psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    }
    return metrics

# Function to simulate multiple devices
def simulate_devices(num_devices):
    devices = {}
    for i in range(num_devices):
        device_name = f"Device_{i+1}"
        devices[device_name] = get_system_metrics()
    return devices

# Function to perform alerting
def alerting(devices):
    alerts = {}
    for device, metrics in devices.items():
        alerts[device] = {metric: value for metric, value in metrics.items() if value > 80}
    return alerts

# Function to perform triage
def triage(alerts):
    triaged_data = {device: "Critical" for device, metrics in alerts.items() if metrics}
    return triaged_data

# Function to fetch context (mocked)
def fetch_context(triaged_data):
    context = {device: f"Context for {device}" for device in triaged_data.keys()}
    return context

# Function to simulate automation engine
def automation_engine(context_data):
    actions = {device: f"Action taken for {device}" for device in context_data.keys()}
    return actions

# Function to resolve issues
def resolve_issues(actions_taken):
    resolutions = {device: f"Issue resolved for {device}" for device in actions_taken.keys()}
    return resolutions

# Function to record changes
def record_changes(resolutions):
    change_log = {device: f"Change recorded for {device}" for device in resolutions.keys()}
    return change_log

# Function to perform predictive maintenance
def predictive_maintenance(change_log):
    maintenance_actions = {device: f"Predictive maintenance scheduled for {device}" for device in change_log.keys()}
    return maintenance_actions

# Function to update knowledge base
def continuous_learning_loop(change_log):
    knowledge_base = {device: f"Knowledge updated for {device}" for device in change_log.keys()}
    return knowledge_base

# Function to visualize dashboard
def visualize_dashboard(devices, alerts, resolutions, maintenance_actions):
    st.title('IT Infrastructure Automation Dashboard')

    for device, metrics in devices.items():
        st.subheader(device)
        fig, axs = plt.subplots(2, 2, figsize=(10, 8))
        fig.suptitle(f'{device} Metrics')

        for i, (metric, value) in enumerate(metrics.items()):
            axs[i//2, i%2].bar(metric, value)
            axs[i//2, i%2].set_title(metric)
            axs[i//2, i%2].set_ylim(0, 100)

        st.pyplot(fig)

    st.subheader("Alerts")
    for device, metrics in alerts.items():
        st.write(f"{device}: {metrics}")

    st.subheader("Resolutions")
    for device, desc in resolutions.items():
        st.write(f"{device}: {desc}")

    st.subheader("Predictive Maintenance Actions")
    for device, desc in maintenance_actions.items():
        st.write(f"{device}: {desc}")

# Streamlit app
def main():
    st.sidebar.title("Settings")
    num_devices = st.sidebar.slider("Number of Devices", 1, 10, 3)
    refresh_rate = st.sidebar.slider("Refresh Rate (seconds)", 1, 10, 2)

    if st.sidebar.button("Run Prototype"):
        while True:
            devices = simulate_devices(num_devices)
            alerts = alerting(devices)
            triaged_data = triage(alerts)
            context_data = fetch_context(triaged_data)
            actions_taken = automation_engine(context_data)
            resolutions = resolve_issues(actions_taken)
            change_log = record_changes(resolutions)
            maintenance_actions = predictive_maintenance(change_log)
            knowledge_base = continuous_learning_loop(change_log)

            visualize_dashboard(devices, alerts, resolutions, maintenance_actions)
            time.sleep(refresh_rate)

if __name__ == "__main__":
    main()
