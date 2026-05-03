import streamlit as st

if __name__ == '__main__':
    # 1- 标题
    st.title("黑马智能聊天机器人")

    # 2- 段落
    st.write(
        "GBK全称《汉字内码扩展规范》（GBK即“国标”、“扩展”汉语拼音的第一个字母，英文名称：Chinese Internal Code Specification） ，中华人民共和国全国信息技术标准化技术委员会1995年12月1日制订，国家技术监督局标准化司、电子工业部科技与质量监督司1995年12月15日联合以技监标函1995 229号文件的形式，将它确定为技术规范指导性文件。2000年已被GB18030-2000《信息交换用 汉字编码字符集 基本集的扩充》国家强制标准替代。 [1]2005年GB18030-2005发布，替代了GB18030-2000。")

    # 3- markdown笔记
    "# 1级标题"
    "## 2级标题"
    "### 3级标题"
    "#### 4级标题"

    # 4- 展示图片
    # 这里如果使用相对路径，一定要注意工作目录是在什么地方
    st.image("ollama-robat/data/1.jpg", width=300)

    # 5- 分割线
    st.divider()

    # 6- 普通表格
    table_data = {
        "姓名": ["b", "a", "c"],
        "年龄": [20, 18, 19],
        "考试成绩": [99.5, 87, 92]
    }

    st.table(data=table_data)

    st.divider()

    # 7- 交互的表格
    st.dataframe(data=table_data)

    # 8.1 普通文本输入框
    name = st.text_input(label="请输入姓名")
    if name:
        st.write(f"欢迎{name}")

    # 8.2 密码输入框
    password = st.text_input(label="请输入密码", type="password")
    if password:
        st.write(f"密码是{password}")

    # 8.3 数值输入框
    age = st.number_input(label="请输入年龄", min_value=18, max_value=100, value=18, step=1)
    if age:
        st.write(f"您的年龄是{age}")

    # 8.4- 数值输入框：其他一些参数设置
    age = st.number_input("请输入年龄", value=99, min_value=0, max_value=100, step=1)
    if age:
        st.write(f"您的年龄是{age}")

    # 9 多行文本输入框
    st.text_area('描述你的专业技能')






























