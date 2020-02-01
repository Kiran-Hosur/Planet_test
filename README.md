# Newtons Law of Gravitation - Simulation on planets

## Simulation

1. Run the script "Planet_sim.py".
2. You can see the red object which acts as Sun
3. Now left click on the screen and drag & drop to create a planet with some initial velocity.
4. You can see the planet rotating around the sun with its snail trail.

## Science part
According to Newtons law of Gravitaion:  
"Every particle attracts every other particle in the universe with the force directly propotional to the product of their masses and inversly propotional to the square of distance between them."  
Therefore  
>  F = G * M1 * M2 / r^2  

This implies that if an object is moving with constant velocity (zero or otherwise) will move with the same velocity unless someone apply an external force. This applied force will either acclerate the object or decelrate the object. 
> F = M * a

## Program part
1. Every particle in the Universe has a mass, occupies space and has a shape.
2. The best way to represent this in any program is the concept of Object oriented programming.
3. Thus we need to have a class of particle but also we will fix the shape of the particle as circle for our easiness and thus we will create a class with the name of "ball".
4. We will be calculating all the calculations in Cartesian co-ordinate system.
5. Now this class will have mass, radius and position (x,y). Each ball object also needs to remember its velocity (vx and vy).
6. Now this class needs to have a method to calculate the new position based on the force applied by other objects. 