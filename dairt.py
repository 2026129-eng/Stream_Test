{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red108\green0\blue181;
\red11\green11\blue11;\red162\green55\blue4;\red104\green102\blue97;\red15\green112\blue1;\red16\green19\blue24;
\red4\green57\blue181;\red14\green110\blue109;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c50588\c0\c76078;
\cssrgb\c4314\c4314\c4314;\cssrgb\c70196\c29020\c0;\cssrgb\c48235\c47451\c45490;\cssrgb\c0\c50196\c0;\cssrgb\c7843\c9412\c12157;
\cssrgb\c0\c31765\c76078;\cssrgb\c0\c50196\c50196;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
import streamlit as at\cb1 \
\cb3 import pandas as pd\cb1 \
\cb3 import numpy as np\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 st.title("European Dairy Products Dashboard")\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 DATA_PATH = "apro_mk_pobta_defaultview_linear_2_0.csv"\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 @st.cache_data\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 def load_data():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3     data = pd.read_csv(DATA_PATH)\cb1 \
\cb3     data = data.dropna(subset=["OBS_VALUE"])\cb1 \
\cb3     return data\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 data_load_state = st.text("Loading Data...")\cb1 \
\cb3 df = load_data()\cb1 \
\cb3 data_load_state.text("Loading Data...Done!")\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 st.subheader("Raw Data")\cb1 \
\cb3 st.write(df)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 st.subheader("Filter by Country")\cb1 \
\cb3 countries = sorted(df["Geopolitical entity (reporting)"].unique())\cb1 \
\cb3 selected_country = st.selectbox("Select a country", countries, index=countries.index("Ireland") if "Ireland" in countries else 0)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \'a0filtered = df[df["Geopolitical entity (reporting)"] == selected_country]\cb1 \
\cb3 st.write(filtered)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 st.subheader(f"Average OBS_VALUE per Year \'97 \{selected_country\}")\cb1 \
\cb3 yearly = filtered.groupby("TIME_PERIOD")["OBS_VALUE"].mean()\cb1 \
\cb3 st.bar_chart(yearly)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 st.subheader(f"Average OBS_VALUE by Milk Item \'97 \{selected_country\}")\cb1 \
\cb3 by_item = filtered.groupby("milkitem")["OBS_VALUE"].mean()\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 st.bar_chart(by_item)\cb1 \
\cb3 st.subheader("Summary Statistics")\cb1 \
\cb3 st.write(filtered["OBS_VALUE"].describe())}