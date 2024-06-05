import streamlit as st
import requests

def fetch_ip():
    # Fetch the public IP address from an external API
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

def main():
    
    try:
        ip_address = fetch_ip()
        st.write(f"Your IP Address is: {ip_address}. Next time, dont click on random links over the internet. You should be glad i am not logging this.")
    except Exception as e:
        st.error(f"Failed to fetch IP address: {str(e)}")

if __name__ == '__main__':
    main()
