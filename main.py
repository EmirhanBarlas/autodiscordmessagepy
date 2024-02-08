from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Discord'a giriş yapmak için kullanıcı adı ve şifrenizi girin
username = "your_username"
password = "your_password"

# Mesajı göndereceğiniz kanalın URL'si
channel_url = "https://discord.com/channels/your_server_id/your_channel_id"

# WebDriver'ı başlatma
driver = webdriver.Chrome()  # Chrome kullanıyorsanız, ChromeDriver indirmelisiniz

# Discord'un giriş sayfasına gitme
driver.get("https://discord.com/login")

# Kullanıcı adı ve şifre alanlarını bulma ve giriş yapma
time.sleep(2)  # Sayfanın yüklenmesini beklemek için
username_field = driver.find_element_by_name("email")
username_field.send_keys(username)
password_field = driver.find_element_by_name("password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Kanala gitme
time.sleep(5)  # Sayfanın yüklenmesini beklemek için
driver.get(channel_url)

# Mesaj gönderme
time.sleep(2)  # Sayfanın yüklenmesini beklemek için
message_field = driver.find_element_by_xpath("//div[@role='textbox']")
message_field.send_keys("Merhaba, bu otomatik bir mesajdır.")
message_field.send_keys(Keys.RETURN)

# WebDriver'ı kapatma
time.sleep(2)  # Mesajın gönderilmesini beklemek için
driver.quit()
