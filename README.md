# Bubble Mayhem

Try to stay alive for as long as possible, without dying!

## Getting Started

### Prerequisites

Kivy

##### For All:

Please run the **code once**, **press esc** and **run it again**.

For some reason the configurations of the screen only load after the first initial run



##### For Windows:

Open Anaconda Prompt
python -m pip install --upgrade pip wheel setuptools
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

##### For Mac:

Have not tested on Mac


### Running Python code
1. Save it to **Desktop**

2. Open Anaconda Prompt(Windows) or Terminal(Linux)

3. Go to your **Desktop**: 

   ```
   cd Desktop
   ```

   

4. Run the Python Code by typing 

   ```
   python cawin_game.py
   ```

## How To Play
**Move** with the arrow keys
**Dash** with v key
**Fire** with spacebar

### How it works 

#### Enemy

We have three types of enemies.

```
Type:   Normal, Thick and Fast 
Colour: White,  Grey  and Blue
Speed:  Normal, Slow  and Fast
```

When you shoot a bubble, it bursts and **split into two**! So watch out!!

We have some information of these bubbles, when shot they will always
split half their size and move **diagonally downwards**! 

These bubbles are crafty buggers, they found a way to bounce across all surfaces
just to get you! 

We will **reward** you for each bubble you burst, 
you get **bonus points** for finishing off the smaller bubbles! 

Here are the point scores

```
Bubble: Normal, Thick and Fast 
Big   :  --   ,  $5   and  --
Medium:  $2   , $10   and  --
Small :  $5   , $15   and $25    
XSmall:  $10  , $20   and $50
```

Money is worthless if you are dead, but at least you can die richer! 
Try to stay alive for as long enough to see how much you can earn!  

#### Bullet

We have a shortage of resources so you have **only two bullets**, 

Once you fired your two shots, you have to 

either wait for your **bullets to leave the screen**,

or       wait for your **bullet to hit an enemy**

***Hint: you can chain your shots by shooting enemies as they come down like a machine gun!* 

#### Dash

We don't have much but we are crafty!!

When you **dash** you are **invincible**! You will **evade all bubbles** when you are dashing! 



However! You will get **tired**! So you will only be able to use it **every 1 second** to be safe! 



#### Health

You will have **three lives** displayed by the audio bar on the top right 





#### Display





##### Built With
Only Kivy's default images were used, no external libraries were used to build this game! 
