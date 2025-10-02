import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the performance DataFrame
performance_df = pd.DataFrame({
    'Model': ['Random Forest', 'XGBoost', 'LightGBM', 'LightGBM (Tuned)'],
    'Accuracy': [0.9452054794520548, 0.9461839530332681, 0.9471624266144814, 0.9393346379647749],
    'Precision': [0.125, 0.2727272727272727, 0.3333333333333333, 0.2],
    'Recall': [0.02, 0.06, 0.08, 0.08],
    'F1-score': [0.034482758620689655, 0.09836065573770492, 0.12903225806451613, 0.11428571428571428]
})

# NOTE: In a real application, you would load models from saved files.
# For this example, we assume the models are available in memory.
# In a production setting, serialize and deserialize your models.
# For demonstration purposes, we will use placeholder variables.
rf_model = 'RandomForestClassifier Model Placeholder'
xgb_model = 'XGBClassifier Model Placeholder'
lgbm_model = 'LGBMClassifier Model Placeholder'
lgbm_tuned_model = 'LGBMClassifier Tuned Model Placeholder'

st.title('Healthcare Dataset Model Performance Dashboard')

st.header('Model Performance Metrics')

st.write('The following table displays the performance metrics (Accuracy, Precision, Recall, and F1-score) for the trained models on the test set.')

st.dataframe(performance_df)

st.header('Model Performance Comparison')

st.write('The following bar plot compares the performance metrics across different models.')

# Reshape the DataFrame for plotting
performance_df_melted = performance_df.melt(id_vars='Model', var_name='Metric', value_name='Score')

# Create a bar plot
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='Metric', y='Score', hue='Model', data=performance_df_melted, ax=ax)
ax.set_title('Model Performance Comparison')
ax.set_ylabel('Score')
ax.set_ylim(0, 1) # Set y-axis limit to 0-1 for scores

# Display the plot in Streamlit
st.pyplot(fig)

st.markdown("""
### How to run this app locally:
1.  Save the code above as `model_dashboard.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the command: `streamlit run model_dashboard.py`
5.  This will start a local web server and open the application in your default web browser.

### Deployment
Deploying a Streamlit app involves hosting it on a server or a cloud platform. Detailed deployment instructions are outside the scope of this task.
""")
