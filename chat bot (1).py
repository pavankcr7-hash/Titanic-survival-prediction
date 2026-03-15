import streamlit as st

# App Title
st.title("🛒 Customer Support Chatbot")

st.write("Hello! I am your Customer Support Assistant. Ask me about orders, refunds, delivery, or payments.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function for rule-based responses
def get_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "order" in user_input or "track" in user_input:
        return "You can track your order in the 'My Orders' section of your account."

    elif "delivery" in user_input or "shipping" in user_input:
        return "Delivery usually takes 3–5 business days."

    elif "refund" in user_input:
        return "Refunds are processed within 5–7 working days after approval."

    elif "return" in user_input:
        return "You can return products within 7 days of delivery."

    elif "payment" in user_input:
        return "We accept credit cards, debit cards, UPI, and net banking."

    elif "cancel" in user_input:
        return "You can cancel your order before it is shipped from the 'My Orders' section."

    elif "contact" in user_input or "support" in user_input:
        return "You can contact our support team at support@example.com."

    elif "bye" in user_input:
        return "Thank you for contacting support. Have a great day!"

    else:
        return "Sorry, I didn't understand that. Please ask about orders, delivery, refund, return, or payment."

# User input
user_input = st.chat_input("Ask your question...")

if user_input:
    
    # Save user message
    st.session_state.messages.append(("user", user_input))
    
    # Generate response
    bot_response = get_response(user_input)
    
    # Save bot message
    st.session_state.messages.append(("bot", bot_response))

# Display chat history
for sender, message in st.session_state.messages:
    
    if sender == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)