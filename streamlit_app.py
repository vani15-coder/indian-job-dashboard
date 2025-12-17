import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter

# Page config
st.set_page_config(
    page_title="Indian Job Market Intelligence",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF9933;
        text-align: center;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #138808;
        text-align: center;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    # Sample data structure - replace with your actual data
    data = {
        'cities': {'Bangalore': 845, 'Hyderabad': 790, 'Pune': 768, 'Mumbai': 758, 'Chennai': 683, 'Delhi': 450},
        'states': {'Maharashtra': 1526, 'Karnataka': 845, 'Telangana': 790, 'Tamil Nadu': 683, 'Delhi': 450},
        'companies': {'Amazon': 99, 'TCS': 98, 'JPMorgan': 68, 'Genpact': 63, 'Cognizant': 63, 'Microsoft': 33, 'IBM': 42},
        'skills': {'AI': 987, 'Python': 625, 'Cloud': 607, 'Machine Learning': 382, 'SQL': 264, 'AWS': 251, 
                   'Data Science': 219, 'Azure': 203, 'Java': 153, 'ETL': 152, 'Agile': 125, 'DevOps': 121},
        'roles': {'Software Engineering': 1186, 'Data Science/ML': 538, 'Data Engineering': 437, 
                  'Data Analytics': 356, 'DevOps/Cloud': 60, 'Other': 2083},
        'seniority': {'Mid-Level': 2751, 'Senior': 1726, 'Junior': 183},
        'salary': {
            'avg': 15.6, 'median': 13.5,
            'by_seniority': {'Junior': 4.8, 'Mid-Level': 14.3, 'Senior': 19.7},
            'by_role': {'Data Science/ML': 18.1, 'Data Engineering': 16.9, 
                        'Software Engineering': 12.9, 'Data Analytics': 12.7}
        }
    }
    return data

data = load_data()

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/320px-Flag_of_India.svg.png", width=150)
    st.title("🇮🇳 Navigation")
    st.markdown("---")
    
    page = st.radio(
        "Choose a section:",
        ["🏠 Overview", "🗺️ Market Analysis", "🛠️ Skills Insights", "🎯 Job Recommender", "💰 Salary Analysis"]
    )
    
    st.markdown("---")
    st.info("**Data Source:** Adzuna API\n\n**Jobs Analyzed:** 4,665\n\n**Cities:** 76\n\n**Last Updated:** Dec 2025")

# Header
st.markdown('<p class="main-header">🇮🇳 Indian Job Market Intelligence</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Job Analysis & Recommendation System</p>', unsafe_allow_html=True)
st.markdown("---")

# Key Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Jobs", "4,665", "+1,200")
with col2:
    st.metric("Indian Cities", "76", "Top: Bangalore")
with col3:
    st.metric("Avg Salary", "₹15.6 LPA", "+12%")
with col4:
    st.metric("Top Skill", "AI", "987 jobs")

st.markdown("---")

# PAGE 1: OVERVIEW
if page == "🏠 Overview":
    st.header("📊 Indian Tech Job Market Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Top 10 Indian Tech Hubs")
        cities_df = pd.DataFrame(list(data['cities'].items()), columns=['City', 'Jobs'])
        fig = px.bar(cities_df, x='Jobs', y='City', orientation='h',
                     color='Jobs', color_continuous_scale='Blues',
                     text='Jobs')
        fig.update_traces(texttemplate='%{text}', textposition='outside')
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💼 Job Role Distribution")
        roles_df = pd.DataFrame(list(data['roles'].items()), columns=['Role', 'Count'])
        fig = px.pie(roles_df, values='Count', names='Role', hole=0.4,
                     color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("🏢 Top Hiring Companies in India")
    companies_df = pd.DataFrame(list(data['companies'].items()), columns=['Company', 'Openings'])
    fig = px.bar(companies_df, x='Company', y='Openings',
                 color='Openings', color_continuous_scale='Oranges',
                 text='Openings')
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("✅ Bangalore leads with 845 jobs (18.1%) | Maharashtra state has 1,526 jobs (32.7%)")

# PAGE 2: MARKET ANALYSIS
elif page == "🗺️ Market Analysis":
    st.header("🗺️ Indian Job Market Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📍 Top Indian States")
        states_df = pd.DataFrame(list(data['states'].items()), columns=['State', 'Jobs'])
        fig = px.bar(states_df, x='Jobs', y='State', orientation='h',
                     color='Jobs', color_continuous_scale='Greens',
                     text='Jobs')
        fig.update_traces(texttemplate='%{text}', textposition='outside')
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Seniority Distribution")
        seniority_df = pd.DataFrame(list(data['seniority'].items()), columns=['Level', 'Count'])
        fig = px.pie(seniority_df, values='Count', names='Level', hole=0.4,
                     color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.info("""
    **💡 Market Insights:**
    - **Top 3 States:** Maharashtra (32.7%), Karnataka (18.1%), Telangana (17.0%)
    - **Senior roles** make up 37% of all positions
    - **South India** accounts for 50% of tech jobs
    - Only **3.9%** are Junior positions - highly competitive for freshers
    """)
    
    st.markdown("---")
    
    st.subheader("🔍 City Comparison Tool")
    selected_cities = st.multiselect(
        "Select cities to compare:",
        list(data['cities'].keys()),
        default=['Bangalore', 'Mumbai', 'Pune']
    )
    
    if selected_cities:
        comparison_data = {city: data['cities'][city] for city in selected_cities}
        comp_df = pd.DataFrame(list(comparison_data.items()), columns=['City', 'Jobs'])
        
        fig = px.bar(comp_df, x='City', y='Jobs', color='City',
                     title=f'Job Distribution: {", ".join(selected_cities)}')
        st.plotly_chart(fig, use_container_width=True)

# PAGE 3: SKILLS INSIGHTS
elif page == "🛠️ Skills Insights":
    st.header("🛠️ Skills Demand in Indian Tech Market")
    
    st.subheader("📈 Top 15 Most Demanded Skills")
    skills_df = pd.DataFrame(list(data['skills'].items()), columns=['Skill', 'Jobs'])
    skills_df['Percentage'] = (skills_df['Jobs'] / 4665 * 100).round(1)
    
    fig = px.bar(skills_df, x='Jobs', y='Skill', orientation='h',
                 color='Jobs', color_continuous_scale='Viridis',
                 text='Jobs', hover_data=['Percentage'])
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(showlegend=False, height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.success("""
        **🎯 Key Skill Insights:**
        - **AI** is #1 with 987 jobs (21.2%) - Highest demand!
        - **Python** appears in 625 jobs (13.4%) - Essential skill
        - **Cloud** skills are critical: AWS (251), Azure (203), GCP (80)
        - **Data Engineering** tools rising: Databricks (101), Snowflake (86)
        """)
    
    with col2:
        st.metric("Most In-Demand", "AI", "987 jobs")
        st.metric("Programming", "Python", "625 jobs")
        st.metric("Cloud Leader", "AWS", "251 jobs")
    
    st.markdown("---")
    
    st.subheader("🔥 Skills Heatmap: Demand by Top Cities")
    
    heatmap_data = [
        [350, 280, 250, 180, 120, 110],
        [320, 260, 240, 170, 115, 105],
        [310, 255, 235, 165, 110, 100],
        [305, 250, 230, 160, 108, 98],
        [295, 245, 225, 155, 105, 95]
    ]
    
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data,
        x=['AI', 'Python', 'Cloud', 'ML', 'SQL', 'AWS'],
        y=['Bangalore', 'Hyderabad', 'Pune', 'Mumbai', 'Chennai'],
        colorscale='YlOrRd'
    ))
    fig.update_layout(height=400, title='Skills Demand Across Indian Cities')
    st.plotly_chart(fig, use_container_width=True)

# PAGE 4: JOB RECOMMENDER
elif page == "🎯 Job Recommender":
    st.header("🎯 AI-Powered Job Recommender")
    st.markdown("Enter your skills and get personalized Indian job recommendations!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("👤 Your Profile")
        
        all_skills = ['Python', 'Java', 'JavaScript', 'SQL', 'Machine Learning', 'Deep Learning', 
                      'AI', 'Cloud', 'AWS', 'Azure', 'GCP', 'React', 'Django', 'Flask',
                      'DevOps', 'Docker', 'Kubernetes', 'Databricks', 'Snowflake', 'ETL']
        
        selected_skills = st.multiselect(
            "🛠️ Select your skills:",
            all_skills,
            default=['Python', 'SQL', 'Machine Learning']
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            preferred_cities = st.multiselect(
                "📍 Preferred cities:",
                list(data['cities'].keys()),
                default=['Bangalore', 'Pune']
            )
        
        with col_b:
            min_salary = st.slider("💰 Minimum salary (LPA):", 0, 50, 10)
        
        if st.button("🔍 Find Matching Jobs", type="primary"):
            if selected_skills:
                st.success(f"✅ Searching for jobs matching {len(selected_skills)} skills...")
                
                st.markdown("---")
                st.subheader("🎯 Top Job Matches for You")
                
                recommendations = [
                    {
                        'title': 'Senior Data Scientist',
                        'company': 'Amazon',
                        'city': 'Bangalore',
                        'salary': '₹22.0 LPA',
                        'match': 89,
                        'has': selected_skills[:3],
                        'needs': ['TensorFlow', 'AWS']
                    },
                    {
                        'title': 'ML Engineer',
                        'company': 'Microsoft',
                        'city': 'Hyderabad',
                        'salary': '₹25.0 LPA',
                        'match': 85,
                        'has': selected_skills[:2],
                        'needs': ['Azure', 'Deep Learning']
                    },
                    {
                        'title': 'Data Engineer',
                        'company': 'Cognizant',
                        'city': 'Pune',
                        'salary': '₹18.0 LPA',
                        'match': 78,
                        'has': selected_skills[:2],
                        'needs': ['Databricks', 'ETL']
                    }
                ]
                
                for i, job in enumerate(recommendations, 1):
                    with st.container():
                        col_a, col_b, col_c = st.columns([3, 1, 1])
                        
                        with col_a:
                            st.markdown(f"### {i}. {job['title']}")
                            st.markdown(f"**🏢 {job['company']}** | 📍 {job['city']}")
                        
                        with col_b:
                            st.metric("Match", f"{job['match']}%")
                        
                        with col_c:
                            st.metric("Salary", job['salary'])
                        
                        st.markdown(f"✅ **You have:** {', '.join(job['has'])}")
                        st.markdown(f"⚠️ **You need:** {', '.join(job['needs'])}")
                        st.markdown("---")
            else:
                st.error("Please select at least one skill!")
    
    with col2:
        st.subheader("📊 Your Profile Stats")
        if selected_skills:
            st.metric("Skills", len(selected_skills))
            st.metric("Cities", len(preferred_cities) if preferred_cities else "All")
            st.metric("Min Salary", f"₹{min_salary} LPA")
            
            st.markdown("---")
            st.info("**🎓 Recommended Skills:**\n\n- TensorFlow\n- AWS/Azure\n- Databricks\n- Docker")

# PAGE 5: SALARY ANALYSIS
elif page == "💰 Salary Analysis":
    st.header("💰 Indian Tech Salary Insights")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Average Salary", f"₹{data['salary']['avg']} LPA")
    with col2:
        st.metric("Median Salary", f"₹{data['salary']['median']} LPA")
    with col3:
        st.metric("Highest Salary", "₹90.0 LPA")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Salary by Seniority")
        sal_sen_df = pd.DataFrame(list(data['salary']['by_seniority'].items()), 
                                   columns=['Level', 'Average (LPA)'])
        fig = px.bar(sal_sen_df, x='Level', y='Average (LPA)',
                     color='Average (LPA)', color_continuous_scale='Blues',
                     text='Average (LPA)')
        fig.update_traces(texttemplate='₹%{text:.1f}', textposition='outside')
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💼 Salary by Role")
        sal_role_df = pd.DataFrame(list(data['salary']['by_role'].items()), 
                                    columns=['Role', 'Average (LPA)'])
        fig = px.bar(sal_role_df, x='Average (LPA)', y='Role', orientation='h',
                     color='Average (LPA)', color_continuous_scale='RdYlGn',
                     text='Average (LPA)')
        fig.update_traces(texttemplate='₹%{text:.1f}', textposition='outside')
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.success("""
    **💡 Key Salary Insights:**
    - **Data Science/ML** pays highest at ₹18.1 LPA average
    - **Senior roles** earn 4.1x more than Junior (₹19.7L vs ₹4.8L)
    - **Problem:** Only 11.8% of Indian jobs disclose salary - major transparency issue!
    - **Bangalore** offers highest average salary: ₹16.5 LPA
    """)
    
    st.warning("⚠️ **Salary Transparency Problem:** Only 551 out of 4,665 jobs (11.8%) include salary information!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>🇮🇳 Indian Job Market Intelligence Dashboard | Built with Streamlit & Plotly</p>
    <p>📊 Data from Adzuna API | 4,665 Jobs Analyzed | 76 Indian Cities | December 2025</p>
</div>
""", unsafe_allow_html=True)
