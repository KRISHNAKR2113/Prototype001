import streamlit as st
import psutil
import matplotlib.pyplot as plt
from streamlit_autorefresh import st_autorefresh

# System metrics
def get_system_metrics():
    return {
        "CPU Usage": psutil.cpu_percent(interval=1),
        "Memory Usage": psutil.virtual_memory().percent,
        "Disk Usage": psutil.disk_usage('/').percent,
        "Network Traffic": psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    }

# Simulate devices
def simulate_devices(num_devices):
    return {f"Device_{i+1}": get_system_metrics() for i in range(num_devices)}

# Alerting and automation
def alerting(devices): return {d: {m: v for m, v in metrics.items() if v > 80} for d, metrics in devices.items()}
def triage(alerts): return {d: "Critical" for d, m in alerts.items() if m}
def fetch_context(triaged): return {d: f"Context for {d}" for d in triaged}
def automation_engine(context): return {d: f"Action taken for {d}" for d in context}
def resolve_issues(actions): return {d: f"Issue resolved for {d}" for d in actions}
def record_changes(resolutions): return {d: f"Change recorded for {d}" for d in resolutions}
def predictive_maintenance(log): return {d: f"Maintenance scheduled for {d}" for d in log}
def continuous_learning_loop(log): return {d: f"Knowledge updated for {d}" for d in log}

# Dashboard
def visualize_dashboard(devices, alerts, resolutions, maintenance_actions):
    tab1, tab2, tab3 = st.tabs(["📊 Metrics", "🚨 Alerts", "🛠️ Maintenance"])

    with tab1:
        for device, metrics in devices.items():
            st.subheader(device)
            cols = st.columns(4)
            for i, (metric, value) in enumerate(metrics.items()):
                cols[i].metric(metric, f"{value:.2f}%", delta=None)

    with tab2:
        st.subheader("Active Alerts")
        if any(alerts.values()):
            for device, metrics in alerts.items():
                st.error(f"{device}: {metrics}")
        else:
            st.success("No critical alerts detected.")

    with tab3:
        st.subheader("Resolutions & Maintenance")
        for device in resolutions:
            st.info(f"{device}: {resolutions[device]}")
            st.write(f"🔧 {maintenance_actions[device]}")

# Main app
def main():
    st.set_page_config("Proactive Monitoring", layout="wide")

    # Compact header
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown("### 🔍 Proactive IT Monitoring Dashboard")
    with col2:
        st.markdown("")

    if "run_monitoring" not in st.session_state:
        st.session_state.run_monitoring = False

    with st.sidebar:
        st.header("⚙️ Settings")
        num_devices = st.slider("Number of Devices", 1, 10, 1)
        refresh_rate = st.slider("Refresh Rate (seconds)", 1, 10, 2)

        if st.button("▶️ Start Monitoring"):
            st.session_state.run_monitoring = True
        if st.button("⏹️ Stop Monitoring"):
            st.session_state.run_monitoring = False

    if st.session_state.run_monitoring:
        # Auto-refresh
        st_autorefresh(interval=refresh_rate * 1000, limit=None, key="refresh")

        devices = simulate_devices(num_devices)
        alerts = alerting(devices)
        triaged = triage(alerts)
        context = fetch_context(triaged)
        actions = automation_engine(context)
        resolutions = resolve_issues(actions)
        change_log = record_changes(resolutions)
        maintenance = predictive_maintenance(change_log)
        knowledge = continuous_learning_loop(change_log)

        visualize_dashboard(devices, alerts, resolutions, maintenance)

if __name__ == "__main__":
    main()
