import random

# Define our crypto database
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10
    },
    "Polkadot": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7/10
    }
}

# Greeting messages
GREETINGS = [
    "Hey there! Let's find you a green and growing crypto!",
    "Welcome to CryptoBuddy! Ready to explore sustainable investments?",
    "Hello! I'm CryptoBuddy, your AI-powered financial sidekick!",
    "Hi there! Let's discover profitable and eco-friendly cryptos together!"
]

# Farewell messages
FAREWELLS = [
    "Remember: Crypto is risky—always do your own research! Happy investing!",
    "Don't forget to diversify your portfolio! See you next time!",
    "CryptoBuddy signing off! Stay safe in the crypto world!",
    "Before investing, consider consulting a financial advisor. Bye for now!"
]

def get_greeting():
    """Return a random greeting message"""
    return random.choice(GREETINGS)

def get_farewell():
    """Return a random farewell message"""
    return random.choice(FAREWELLS)

def recommend_profitable():
    """Recommend cryptocurrencies based on profitability"""
    profitable_coins = [
        name for name, data in crypto_db.items() 
        if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]
    ]
    
    if not profitable_coins:
        return "I couldn't find any strongly trending cryptocurrencies right now."
    
    if len(profitable_coins) == 1:
        coin = profitable_coins[0]
        return f"{coin} is currently trending up with a solid market cap! 📈"
    
    return "Here are some profitable options: " + ", ".join(profitable_coins) + "."

def recommend_sustainable():
    """Recommend cryptocurrencies based on sustainability"""
    sustainable_coins = [
        (name, data["sustainability_score"]) 
        for name, data in crypto_db.items() 
        if data["energy_use"] == "low" and data["sustainability_score"] >= 7/10
    ]
    
    if not sustainable_coins:
        return "I couldn't find any highly sustainable cryptocurrencies right now."
    
    # Sort by sustainability score (highest first)
    sustainable_coins.sort(key=lambda x: x[1], reverse=True)
    
    if len(sustainable_coins) == 1:
        coin = sustainable_coins[0][0]
        return f"{coin} is the most eco-friendly option with a top-tier sustainability score! 🌱"
    
    top_coin = sustainable_coins[0][0]
    other_coins = [coin[0] for coin in sustainable_coins[1:]]
    return f"{top_coin} is the most sustainable! Also consider: {', '.join(other_coins)}."

def recommend_balanced():
    """Recommend cryptocurrencies that balance profitability and sustainability"""
    balanced_coins = [
        (name, (data["sustainability_score"] + 
                (0.5 if data["price_trend"] == "rising" else 0) +
                (0.3 if data["market_cap"] == "high" else 0.1 if data["market_cap"] == "medium" else 0)))
        for name, data in crypto_db.items()
    ]
    
    if not balanced_coins:
        return "I couldn't find any good options right now."
    
    # Sort by our combined score
    balanced_coins.sort(key=lambda x: x[1], reverse=True)
    top_coin = balanced_coins[0][0]
    
    return f"For a balance of growth and sustainability, consider {top_coin}! ⚖"

def get_coin_info(coin_name):
    """Get detailed information about a specific cryptocurrency"""
    coin_name = coin_name.title()
    if coin_name not in crypto_db:
        similar = [name for name in crypto_db.keys() if coin_name.lower() in name.lower()]
        if similar:
            return f"I don't have data on {coin_name}, but I do have info on: {', '.join(similar)}."
        return f"I don't have data on {coin_name}. Try asking about Bitcoin, Ethereum, or Cardano."
    
    data = crypto_db[coin_name]
    info = [
        f"Here's what I know about {coin_name}:",
        f"• Price trend: {data['price_trend']}",
        f"• Market cap: {data['market_cap']}",
        f"• Energy use: {data['energy_use']}",
        f"• Sustainability score: {data['sustainability_score']*10}/10"
    ]
    return "\n".join(info)

def handle_query(user_query):
    """Process the user's query and return an appropriate response"""
    user_query = user_query.lower()
    
    if any(word in user_query for word in ["hi", "hello", "hey", "greetings"]):
        return get_greeting()
    
    if any(word in user_query for word in ["bye", "exit", "quit", "goodbye"]):
        return get_farewell()
    
    if any(word in user_query for word in ["profit", "grow", "trend", "rising"]):
        return recommend_profitable()
    
    if any(word in user_query for word in ["sustain", "green", "eco", "energy", "environment"]):
        return recommend_sustainable()
    
    if any(word in user_query for word in ["balance", "both", "middle", "compromise"]):
        return recommend_balanced()
    
    if any(word in user_query for word in ["info", "information", "detail", "data", "know"]):
        for coin in crypto_db:
            if coin.lower() in user_query:
                return get_coin_info(coin)
        return "Which cryptocurrency would you like information about? Try 'Tell me about Bitcoin'."
    
    if "recommend" in user_query or "should i buy" in user_query or "invest" in user_query:
        if "sustain" in user_query or "green" in user_query:
            return recommend_sustainable()
        if "profit" in user_query or "grow" in user_query:
            return recommend_profitable()
        return recommend_balanced()
    
    return "I'm not sure I understand. You can ask about profitable cryptos, sustainable cryptos, or get info on specific coins."

def run_chatbot():
    """Run the chatbot interaction loop"""
    print(get_greeting())
    print("\nI can help you with:")
    print("- Trending/profitable cryptocurrencies")
    print("- Eco-friendly/sustainable options")
    print("- Information about specific coins")
    print("- Balanced recommendations")
    print("\nType 'bye' to exit at any time.\n")
    
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
            
        response = handle_query(user_input)
        print(f"CryptoBuddy: {response}")
        
        if any(word in user_input.lower() for word in ["bye", "exit", "quit", "goodbye"]):
            break

# Run the chatbot
if _name_ == "_main_":
    run_chatbot()
