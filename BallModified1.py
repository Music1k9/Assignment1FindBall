# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:55:35 2023

@author: nlewisbassett
"""
  #y = v0*t - 0.5*g*t**2
  
def height(v0, t):
      g = 32.8
      
      y = v0*t - 0.5*g*t**2
      return y
  
t=1
while t > 0:
      v0 = input( 'input velocity:')
      v0 = float(v0)
      t = input('input time, sec: ')
      t = float(t)
      y = height(v0,t)
      
      print(f'after {t} seconds height = {y}')
      
      """
      at time 1.6 ball reached maximum height
      which was about 38 feet. Assuming we throw it
      vertically at initial velocity 50 fps
      """
def calculate_max_height(v0, g):
    # Formula for maximum height: h_max = (v0^2) / (2g)
    h_max = (v0 ** 2) / (2 * g)
    return h_max

def main():
    # Constants
    v0 = 50  # Initial velocity of the ball in ft/sec
    g = 32.8  # Acceleration due to gravity in ft/sec^2

    # Calculate the maximum height
    max_height = calculate_max_height(v0, g)

    # Display the result
    print("The maximum height reached by the ball is:", max_height, "ft")

# Run the program
if __name__ == "__main__":
    main()
