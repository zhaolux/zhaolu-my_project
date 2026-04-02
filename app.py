import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="数据分析 BI 工具", layout="wide")

st.title("📊 数据分析 Dashboard")

# 上传文件
file = st.file_uploader("上传 CSV 文件", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("数据预览")
    st.dataframe(df)

    col1, col2 = st.columns(2)

    # 分类统计
    if "product" in df.columns:
        sales = df.groupby("product")["quantity"].sum()

        with col1:
            st.subheader("📊 分类销量")
            fig, ax = plt.subplots()
            ax.bar(sales.index, sales.values)
            st.pyplot(fig)

        with col2:
            st.subheader("🥧 占比")
            fig2, ax2 = plt.subplots()
            ax2.pie(sales, labels=sales.index, autopct="%1.1f%%")
            st.pyplot(fig2)

    # 时间趋势
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
        trend = df.groupby("date")["quantity"].sum()

        st.subheader("📈 销售趋势")
        fig3, ax3 = plt.subplots()
        ax3.plot(trend.index, trend.values, marker="o")
        st.pyplot(fig3)
