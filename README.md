# HandGesture-Pong
This project brings a twist to the classic Pong game by utilizing hand gestures as the control mechanism. Instead of relying on keyboard or mouse inputs, players move their paddle up and down by positioning their hand within the camera's view. 
This README provides all the information you need to get started which includes: 
- Setup instructions
- Gameplay details
- Resources used to create this project

## Setup Instructions
### Prerequisites
Python installed on current environment. (3.6 or newer is recommended) 
Working webcam for the hand gesture detection to function.
### Installation
1. Clone the repository

  ``` git clone https://github.com/rhythmpatel12/HandGesture-Pong.git ```

  ``` cd HandGesture-Pong ```

2. Run setup.py script to install required packages and test the webcam
   
  ``` python setup.py ```
### Running the game 
To run the game simply run the following command on your terminal. 

``` python main.py ```

Alternatively, you can simply run the main.py python file in an IDE.

## Gameplay details 

### Instructions 
You would simply need to follow the instructions on screen to play the game. 

When running the game, use ``` Space ``` to start, ``` Esc ``` to end, ``` R ``` to restart, and ``` Q ``` to quit the game. 

Moving the Paddle: Position your hand at different heights within the camera's view to move the paddle up and down. The game uses the FIRST hand it detects as the controller. 

Customizing Gameplay: Feel free to dive into the code to adjust the game's difficulty, obstacle parameters, or ball speed to your liking.

## Resources 
This project was made possible with the help of several resources and tutorials. Below is a list of some of the key resources used during development:
ChatGPT: Provided guidance on Python best practices, game logic, and problem-solving strategies. OpenAI ChatGPT

[cvzone Repository](https://github.com/cvzone/cvzone/blob/master/cvzone/HandTrackingModule.py): Offered example code on their public repository which showed how to use their HandGesture module.

[YouTube Tutorial](https://www.youtube.com/watch?v=LIDJzJhlyyg&ab_channel=Murtaza%27sWorkshop-RoboticsandAI): A specific YouTube tutorial helped in understanding the integration of hand gestures and using it to control entities. This method was then transferred to pygame during framework switch. 

[Python PEP 8 Documentation](https://peps.python.org/pep-0008/): The official Python documentation was a go-to resource for best practices, especially regarding Pythonic ways to implement game logic and structure. Python's Official Documentation is an invaluable resource for any Python developer.

