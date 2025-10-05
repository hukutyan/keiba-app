import streamlit as st
import pandas as pd

# サンプルデータ（本当はオッズや過去走をAPIから取得）
data = {
    "horse_id": [101, 102, 103],
    "place_odds": [1.8, 2.2, 1.4],
    "place_rate": [0.6, 0.5, 0.7]
}
df = pd.DataFrame(data)
df["expected_value"] = df["place_odds"] * df["place_rate"]

st.title("複勝1.5倍以上 狙い馬アプリ")

candidates = df[df["place_odds"] >= 1.5].sort_values("expected_value", ascending=False)
st.dataframe(candidates)
