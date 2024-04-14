To be used inside blender's python console.

It reads from a csv that has coordinates for the following data:

1. camera position (either relative or world, it doesn't really matter conversion can be determined, blender will always read x and y) 
2. camera target
3. camera zoom
4. camera focal length 

Then it adds the camera and target object and adds keyframes per row in the corresponding positions. 

In theory it should recreate the data to a fairly accurate 3D standard. In practice due to the framerates etc, it depends on the data, on the framerate of your scene, on the orientation (that's a hard one to get sometimes) for the speed (because that's what's up for debate here) to be determined accurately. 

use as a basis, evaluate if it helps.
