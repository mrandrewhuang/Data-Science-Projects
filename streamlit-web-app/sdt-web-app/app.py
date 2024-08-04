import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('datasets/vehicles_us_cleaned.csv')
alt_color_sequence = px.colors.qualitative.Light24

# Data viewer
st.header('Data viewer')
st.dataframe(df)

# Plot a scatter plot to visualize correlation between odometer and price
st.header('Vehicle `odometer` vs. `price` by `condition` & `model_year`')
df_odometer_price_filtered = df[(df['odometer'] <= 550000) & (df['price'] <= 100000)]
min_year, max_year = df_odometer_price_filtered['model_year'].min(), df_odometer_price_filtered['model_year'].max()
year_range = st.slider(
    'Choose year range',
    value=(min_year, max_year),
    min_value=min_year,
    max_value=max_year
)
selected_year_range = list(range(year_range[0], year_range[1] + 1))
filtered_df_for_plot = df_odometer_price_filtered[df_odometer_price_filtered['model_year'].isin(list(selected_year_range))]
fig = px.scatter(
    filtered_df_for_plot,
    x='odometer',
    y='price',
    color='condition'
)
st.write(fig)

# Plot a scatter plot to visualize correlation between model year and how long it takes to sell
st.header('Vehicle `model_year` vs. `days_listed` by `manufacturer` and `condition`')
df_model_year_filtered = df[df['model_year'] > 1980]
condition_choice = df_model_year_filtered['condition'].unique()
selected_condition_choice = st.selectbox(
    'Filter by condition',
    condition_choice
)
filtered_df_for_plot = df_model_year_filtered[df_model_year_filtered['condition'] == selected_condition_choice]
fig = px.scatter(
    filtered_df_for_plot,
    x='model_year',
    y='days_listed',
    color='manufacturer',
    color_discrete_sequence=alt_color_sequence
)
st.write(fig)

# Plot a histogram to visualize the distribution of paint colors
st.header('Vehicle `paint_color` by `type`')
df_paint_color_filtered = df[~(df['paint_color'] == 'unknown') & ~(df['type'] == 'other')]
normalize = st.checkbox(
    'Normalize plot by sample percentage',
    value=False
)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

fig = px.histogram(
    df_paint_color_filtered,
    x='paint_color',
    color='type',
    color_discrete_sequence=alt_color_sequence,
    histnorm=histnorm
)
st.write(fig)

# Plot a histogram to visualize the distribution of car age
st.header('Vehicle `car_age` by `condition` & `odometer`')
min_miles, max_miles = df['odometer'].min(), df['odometer'].max()
odometer_range = st.slider(
    'Choose odometer range',
    value=(min_miles, max_miles),
    min_value=min_miles,
    max_value=max_miles
)
selected_odometer_range = list(range(odometer_range[0], odometer_range[1] + 1))
filtered_df_for_plot = df[df['odometer'].isin(list(selected_odometer_range))]
fig = px.histogram(
    filtered_df_for_plot,
    x='car_age',
    color='condition'
)
st.write(fig)
