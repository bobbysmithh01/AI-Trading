
def run_strategy(symbol):
    # Simulated strategy logic
    entry = 100.0
    exit = 102.0
    pnl = round(exit - entry, 2)
    return {
        "symbol": symbol,
        "entry_price": entry,
        "exit_price": exit,
        "pnl": pnl,
        "status": "simulated"
    }
