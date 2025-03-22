
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('🌳 Random Forest分类应用')

# 加载数据
data = pd.read_csv('dataset.csv')

# 显示数据
st.write("### 数据预览：")
st.dataframe(data.head())

# 选择特征和标签
X = data[['feature1', 'feature2', 'feature3', 'feature4']]
y = data['target']

# 训练随机森林模型
model = RandomForestClassifier()
model.fit(X, y)

st.write("### 🌟 模型已训练完毕！")

# 用户输入预测
st.sidebar.header('请输入特征进行预测')

def user_input_features():
    f1 = st.sidebar.slider('Feature 1', float(X.feature1.min()), float(X.feature1.max()), float(X.feature1.mean()))
    f2 = st.sidebar.slider('Feature 2', float(X.feature2.min()), float(X.feature2.max()), float(X.feature2.mean()))
    f3 = st.sidebar.slider('Feature 3', float(X.feature3.min()), float(X.feature3.max()), float(X.feature3.mean()))
    f4 = st.sidebar.slider('Feature 4', float(X.feature4.min()), float(X.feature4.max()), float(X.feature4.mean()))
    return pd.DataFrame({'feature1':[f1],'feature2':[f2],'feature3':[f3],'feature4':[f4]})

input_df = user_input_features()

st.write("### 用户输入特征：")
st.write(input_df)

# 进行预测
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.write("### 预测结果：")
st.write('类别为：', prediction[0])

st.write("### 预测概率：")
st.write(prediction_proba)
