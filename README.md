# Motions

## Overview:

Motions is a versatile tool designed to define triggers for executing various actions. These actions, termed as "motions," encompass a wide range of functionalities including scroll, mouse click, key press, key hold, cursor movement, and more. With Motions, users can effortlessly create custom triggers tailored to their specific needs, thereby enhancing productivity and efficiency in various tasks.

## Features:

- **Custom Motion Creation**: Motions empowers users to define personalized triggers according to their preferences and requirements.
- **Multiple Motion Types**: The tool supports diverse motion types such as scroll, mouse click, key click, key hold, cursor movement, and more, ensuring flexibility in action execution.
- **Intuitive Interface**: With an intuitive and user-friendly interface, Motions enables seamless navigation and effortless creation of motion triggers.
- **Configurable Settings**: Users have the freedom to configure settings for each motion, allowing for fine-tuning and optimization based on individual preferences.
- **Cross-Platform Compatibility**: Motions is compatible across various operating systems, ensuring accessibility and usability for a wide range of users.
- **Automation Capabilities**: By defining triggers for specific actions, users can automate repetitive tasks and streamline workflows, saving time and effort.
- ** Custom motions **: even though there is a big system of motions and executors you can always define ypur own due to the easy syntax and also using the custom web server you can make all kinds of motions -> example: you can define some script or exe and add this to the custom motion options and for the trigger you can use the custom web server
pseudo Syntax: 
```py
trigger: "motion_name", //will be later referenced oin the web server
executor: "hi.exe"

```
like this whenever a req is send to this web server ( which can be automated ny a script to send a req based in a certain condition [hmm ... could be another motion] it will execute the ``` exe ``` )


## Getting Started:

To begin using Motions, follow these simple steps:

1. **Installation**: Download and install Motions from the official website or preferred distribution platform.

2. **Launch the Application**: Open Motions on your device to access the main interface.

3. **Define Triggers**: Create custom triggers by selecting the desired motion type and configuring the associated settings.

4. **Save and Apply**: Once the triggers are defined, save your configurations and apply them to initiate the specified actions.

## Motion and Trigger Types:

- **Scroll Motion**: Define triggers for automatic scrolling through documents or web pages, including options to change the scrolling speed and direction.

- **Mouse Click Motion**: Create triggers for performing mouse clicks at specified locations on the screen, with options to define single-click, double-click, or right-click actions.

- **Key Press Motion**: Define triggers for executing keyboard shortcuts or input commands, with options to specify the keys to be pressed and the duration of the key hold.

- **Key Hold Motion**: Create triggers for holding down specific keys for a defined period, useful for continuous input actions or gaming commands.

- **Cursor Movement Motion**: Configure triggers for simulating cursor movements on the screen, including options to specify the starting and ending positions, as well as the duration of the movement.

- **Change in Screen Motion**: Define triggers based on changes in the screen, such as window focus changes, window size changes, or pixel color changes at specific coordinates.




## Things To Do
- make an event based system: set up a localhost:3000 listener on which you list6en for requests and based on the req perform a motion ( e.g. you make a motion to execute and it executes whenever a req is recieved on certain url and could be made with the following syntax -> 
```json  
{
    motion_name: "placeholder",
    passowrd: "placeholder"
}

```
and it will execute the motion associated with the name [ all motions could be inside a dict in whioch the name is the key and the function to execute is the value`]

)
