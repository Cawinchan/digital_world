# Bubble Mayhem

Try to stay alive for as long as possible, without dying!

## Getting Started

### Prerequisites
Kivy

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
We have three types of enemies.

```
Type:   Normal, Thick and Fast 
Colour: White,  Grey  and Blue
Speed:  Normal, Slow  and Fast
```

When you shoot a bubble, it bursts and **split into two**! So watch out!!

We found some information of these bubbles, when shot they will always
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

Money is worthless if you are dead, but you can always die richer than others! 
Try to stay alive for as long enough to see how much you can earn!  

##### Built With
Only Kivy's default images were used, no external libraries were used to build this game! 
