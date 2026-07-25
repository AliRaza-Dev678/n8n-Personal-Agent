import streamlit as st
import requests

# NOTE: This is an n8n TEST webhook URL. Test webhooks only work for ONE
# call after you click "Execute workflow" in the n8n editor, then they
# deregister and return a 404 until you click it again.
# For a persistent Streamlit app, activate your n8n workflow and switch
# this to the PRODUCTION URL (uses /webhook/ instead of /webhook-test/).
WEBHOOK_URL = "http://localhost:5678/webhook/6157a077-2a85-4cbc-9bb5-8ae662402bcb"

# create the title for the page
st.title("🤝 Your Personal Assistant")

# add subheader
st.subheader("What can your personal assistant do?")

# create a list of what your assistant can do
st.markdown("""
            1. Answer questions on various topics.   
            2. Arrange Calendar events and meetings.  
            3. Read your emails and send replies, can even summarize them for you.
            4. Manage your tasks and to-do lists.
            5. Take quick notes for you.
            6. Track your expenses and budgeting.
            """)

# add chats subheader
st.subheader("💬 Chat with your assistant")

# create a session state for message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show the messages in chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# create a chat input box
user_message = st.chat_input()


def extract_ai_response(data):
    """
    Safely extract the 'output' text from an n8n webhook response,
    regardless of whether n8n returns a list, a dict, or something else.
    """
    # Case 1: n8n returned a list of items, e.g. [{"output": "..."}]
    if isinstance(data, list):
        if len(data) == 0:
            return "⚠️ The assistant returned an empty list response."
        first_item = data[0]
        if isinstance(first_item, dict):
            return first_item.get("output", f"⚠️ No 'output' key found. Got: {first_item}")
        return str(first_item)

    # Case 2: n8n returned a single dict, e.g. {"output": "..."}
    if isinstance(data, dict):
        return data.get("output", f"⚠️ No 'output' key found. Got: {data}")

    # Case 3: anything else (string, number, etc.)
    return str(data)


# if user sends a message
if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
    # append the user message to message history
    st.session_state.messages.append({"role": "user", "content": user_message})

    ai_response = None

    try:
        # send the user message to the n8n webhook
        response = requests.post(
            WEBHOOK_URL,
            json={"message": user_message},
            timeout=30,
        )

        if response.status_code != 200:
            ai_response = (
                f"⚠️ Webhook returned status {response.status_code}: {response.text}"
            )
        else:
            try:
                data = response.json()
                ai_response = extract_ai_response(data)
            except requests.exceptions.JSONDecodeError:
                ai_response = f"⚠️ Webhook did not return valid JSON. Raw response: {response.text}"

    except requests.exceptions.RequestException as e:
        ai_response = f"⚠️ Could not reach the webhook: {e}"

    # display the AI response in chat
    with st.chat_message("assistant"):
        st.markdown(ai_response)
    # append the AI response to message history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})