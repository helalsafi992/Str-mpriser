from eq_fetch import fetch_all_forecasts
from historical_loader import load_historical_data
from decision_engine import decide_trade

if __name__ == "__main__":
    live_df = fetch_all_forecasts()
    hist_df = load_historical_data()
    result = decide_trade(live_df, hist_df)

    if result:
        print(f"\n✅ Køb kl. {result['buy_hour']} → Sælg kl. {result['sell_hour']} → Forventet spread: {result['spread']} øre/MWh")
    else:
        print("\n⚠️ Ingen god handel fundet i dag.")
