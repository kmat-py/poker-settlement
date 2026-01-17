import streamlit as st

st.set_page_config(page_title="ポーカー精算", layout="centered")
st.title("🃏 ポーカー精算アプリ")

st.write("Buy-in と Cash-out を入力してください")

MAX_PLAYERS = 6
players = []

for i in range(MAX_PLAYERS):
    st.subheader(f"プレイヤー {i+1}")
    name = st.text_input("名前", key=f"name{i}")
    buyin = st.number_input("Buy-in（円）", min_value=0, step=1000, key=f"buy{i}")
    cashout = st.number_input("Cash-out（円）", min_value=0, step=1000, key=f"cash{i}")

    if name:
        players.append({
            "name": name,
            "balance": cashout - buyin
        })

st.divider()

if st.button("精算する"):
    winners = [(p["name"], p["balance"]) for p in players if p["balance"] > 0]
    losers = [(p["name"], -p["balance"]) for p in players if p["balance"] < 0]

    st.subheader("💰 精算結果")

    if not winners or not losers:
        st.write("精算はありません")
    else:
        i = j = 0
        while i < len(losers) and j < len(winners):
            loser, l_amt = losers[i]
            winner, w_amt = winners[j]

            pay = min(l_amt, w_amt)
            st.write(f"**{loser} → {winner} : {pay:,} 円**")

            losers[i] = (loser, l_amt - pay)
            winners[j] = (winner, w_amt - pay)

            if losers[i][1] == 0:
                i += 1
            if winners[j][1] == 0:
                j += 1