import streamlit as st
from Read_vcf import read_vcf
from Send_Messages import send_message

cl1, cl2, cl3 = st.columns([3, 3, 2])

# Initialize the list outside the function
if 'selected_contacts' not in st.session_state:
    st.session_state.selected_contacts = []

with cl1:
    # print first message
    st.image('whatsapp.png' , width=150)
    st.write("### Whatssap Message Bulker")
    # input field
    msg = st.text_area("Your Message ? : ")

    # send the message
    send = st.button("Send Message")
    clear = st.button("Clear List")
    if clear:
        st.session_state.selected_contacts.clear()
## check box list
contact_list = read_vcf('Contacts.vcf')

# Display a title
with cl2:
    # Create a search bar
    search_query = st.text_input("Search contacts:")

    # Filter contacts based on search query
    filtered_contacts = [contact for contact in contact_list if search_query.lower() in contact.lower()]

    expander = st.expander("##### Select Contact", expanded=True)

    # Create checkboxes for each filtered contact
    for idx, contact in enumerate(filtered_contacts):
        # Check if the contact is in the selected_contacts list
        checkbox_result = expander.checkbox(f"{idx + 1}. {contact}", key=f"checkbox_{idx}",
                                            value=(contact in st.session_state.selected_contacts))

        # Update the selected_contacts list based on the checkbox state
        if checkbox_result and contact not in st.session_state.selected_contacts:
            st.session_state.selected_contacts.append(contact)
        elif not checkbox_result and contact in st.session_state.selected_contacts:
            st.session_state.selected_contacts.remove(contact)

with cl3:
    # Display the selected contacts

    st.write("##### Slected Contact")
    for item in st.session_state.selected_contacts:
        st.markdown("-" + item)


# click to send
if send:
    if st.session_state.selected_contacts:
        send_message(st.session_state.selected_contacts, msg)
        st.session_state.selected_contacts.clear()
