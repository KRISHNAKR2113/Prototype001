import streamlit as st
import psutil
import matplotlib.pyplot as plt

# Function to collect real-time system metrics
def get_system_metrics():
    return {
        "CPU Usage": psutil.cpu_percent(interval=1),
        "Memory Usage": psutil.virtual_memory().percent,
        "Disk Usage": psutil.disk_usage('/').percent,
        "Network Traffic": psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    }

# Dashboard visualization
def visualize_dashboard(metrics):
    st.markdown("### 🔍 Proactive IT Monitoring Dashboard")

    tab1, tab2, tab3 = st.tabs(["📊 Metrics", "📈 Trends", "🛠️ Maintenance"])

    with tab1:
        st.subheader("Real-Time System Metrics")
        cols = st.columns(4)
        for i, (metric, value) in enumerate(metrics.items()):
            display_value = f"{value:.2f}%" if "Traffic" not in metric else f"{value / (1024**2):.2f} MB"
            cols[i].metric(metric, display_value)

    with tab2:
        st.subheader("Metric Snapshot")
        fig, ax = plt.subplots()
        ax.bar(metrics.keys(), metrics.values(), color='skyblue')
        ax.set_ylabel("Usage (%)")
        ax.set_ylim(0, 100)
        st.pyplot(fig)

    with tab3:
        st.subheader("Maintenance Actions")
        st.write("No maintenance actions scheduled.")

# Main app
def main():
    st.set_page_config("Proactive Monitoring", layout="wide")

    if "run_monitoring" not in st.session_state:
        st.session_state.run_monitoring = False

    with st.sidebar:
        st.header("⚙️ Settings")
        refresh_rate = st.slider("Refresh Rate (seconds)", 1, 10, 2)

        if st.button("▶️ Start Monitoring"):
            st.session_state.run_monitoring = True
        if st.button("⏹️ Stop Monitoring"):
            st.session_state.run_monitoring = False

    if st.session_state.run_monitoring:
        metrics = get_system_metrics()
        visualize_dashboard(metrics)

    if st.button("🔄 Refresh Metrics"):
        metrics = get_system_metrics()
        visualize_dashboard(metrics)

if __name__ == "__main__":
    main()
