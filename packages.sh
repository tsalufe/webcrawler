#apt packages
# sudo apt install -y python3.7 python3-pip
alias python3=python3.7
pip3 install --upgrade pip

#pip3 packages
pip3 install django
pip3 install selenium
if [[ "$(uname -s)" == Linux* ]]; then
    wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux32.tar.gz
elif [[ "$(uname -s)" == Darwin* ]]; then
    wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-macos.tar.gz
fi
tar -xvf geckodriver*.tar.gz
chmod +x geckodriver
mv geckodriver /usr/local/bin/
rm geckodriver*.tar.gz
# sudo apt update
# sudo apt -y install firefox