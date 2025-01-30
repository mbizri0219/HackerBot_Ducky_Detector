# Hackerbot

## Raspberry Pi and Arduino Installation
Once you have installed your Raspberry pi OS and connected it to your network, connect through your terminal with ssh. 

` ssh <user>@<hackerbot device name> `

Once you are connected, you need to update the device and software.

`sudo apt update && sudo apt upgrade -y`    
`sudo apt install -y python3 python3-pip git curl build-essential`

Now the device is updated, install Arduino CLI onto the raspberry pi using the shell

<code>
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
mkdir -p /home/<user>/arduino-cli
mv bin/arduino-cli /home/<user>/arduino-cli/arduino-cli
echo 'export PATH=$PATH:/home/<user>/arduino-cli' >> ~/.bashrc
source ~/.bashrc
arduino-cli version
</code>

Next we need to link the type of board to the Arduino CLI. You can do this by editing the arduino-cli.yaml.

The file should be located below:

`nano $user/.arduino15/arduino-cli.yaml`

Edit the code so it reflects:

<code>
board_manager:
    additional_urls: [https://adafruit.github.io/arduino-board-index/package_adafruit_index.json]
</code>

Once it has been updated, you need to reload the yaml file by running the code below and then installing the board.

`arduino-cli core update-index`
`arduino-cli core install adafruit:samd`

## Installing Arduino Libraries

First if at any point you are trying to search and install any library for Arduino CLI, you can use the command below.

`arduino-cli lib search <search term>`

To install you need to run:

`arduino-cli lib install <library to install>`



## Installing the Internal Firmware

Move the terminal into the "Arduino/libraries" folder. If it's not there make it using the command below.

`mkdir -p Arduino/libraries`

We are going to pull down the firmware repo into this folder. You can run the command below to clone the repo.

`git clone https://github.com/hackerbotindustries/internal_development.git Hackerbot` 

You need to have a username and token setup on github to be able to clone the repo. 

You can now run arduino-cli to compile and upload the firmware.

Compiling Arduino: 

`arduino-cli compile -p /dev/ttyACM0 --fqbn adafruit:samd:adafruit_qtpy_m0 ~/Arduino/libraries/Hackerbot/examples/Hackerbot-Basic/Hackerbot-Basic.ino`

Uploading to Arduino:

`arduino-cli upload -p /dev/ttyACM0 --fqbn adafruit:samd:adafruit_qtpy_m0 ~/Arduino/libraries/Hackerbot/examples/Hackerbot-Basic/Hackerbot-Basic.ino`

If the board does not connect using the "/dev/ttyACM0", you can identify the correct port by running the command:

`arduino-cli board list`

## Installing the Flask_API

Go to the user's directory on the raspberry device. Once there, run the git clone command on the repo.

`git clone https://github.com/hackerbotindustries/api-flask.git`

Once it is cloned, we want to set up the virtual environment for the application. 

`cd api-flask`
`python3 -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

Those commands should create the venv, activate it and then install the correct python librarys to run the applicaiton. 

To run the application, you can either running directly in the terminal window and leaving it open in the shell. This allows you to see the logs but once you close the shell it closes the application.

`python3 main.py`

You can also run the flask application in the background which will allows it to keep running even once the terminal is closed. 

`nohup python3 main.py`

Now all of the API commands should be accessible by the using the hackerbot raspberry pi's ip address at port 5000.