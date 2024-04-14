import bpy
import csv
import pathlib
import math

#file neighbourhood
file_loc = pathlib.Path(__file__).parent.resolve()
folder = pathlib.Path(file_loc).parent.resolve()

data = ''

#set scene framerate
fps = 50
bpy.context.scene.render.fps = fps
frame_end = 1731

#data sources
data = pathlib.Path(folder).joinpath(data)
scene = bpy.context.scene

with open(data) as csv_file:    
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:        
        if line_count > 0:
            #initial setup
            if line_count == 1:
                camera_data = bpy.data.cameras.new(f'{row[0]}_data')
                camera_object = bpy.data.objects.new(f'{row[0]}', camera_data)
                #camera_lens = bpy.data.cameras.new(f'{row[0]}', camera_data)
                bpy.data.collections["Cameras"].objects.link(camera_object)
                
                #camera data setup
                camera_object.show_axis = True
                camera_data.clip_start = 1
                camera_data.clip_end = 1000000
                
                camera_data.display_size = 1
                
                #add target
                target = bpy.data.objects.new(f'{row[0]}_target', None)
                bpy.data.collections["Cameras"].objects.link(target)
                
                #add camera constraint using target
                constraint = camera_object.constraints.new(type='TRACK_TO')
                constraint.target = target
                            
            if line_count >= 1:
                
                frame = float(row[0]) * fps
                
                #set camera focal length
                camera_data.lens = float(row[8])
                
                                
                #check camera digital 2x zoom
                
                                    
                if bool(row[5]) == 0:
                    if bool(row[5]) == 1:
                        camera_data.lens = float(row[8]) * 2
                    else:
                        camera_data.lens = float(row[8])
                else:
                        camera_data.lens = float(row[8])
                
                #set camera location
                camera_object.location[0] = float(row[25])
                camera_object.location[1] = float(row[26])
                camera_object.location[2] = float(row[27])
                
                #set target location
                target.location[0] = float(row[28])
                target.location[1] = float(row[29])
                target.location[2] = float(row[30])
                
                #insert keyframes
                camera_object.keyframe_insert(data_path="location", frame=frame)
                target.keyframe_insert(data_path="location", frame=frame)
                #insert focal length keyframe
                camera_data.keyframe_insert(data_path="lens", frame=frame)
                
                
                bpy.data.scenes["Scene"].frame_end = frame_end
                
                print(camera_object.location, frame, line_count)
            
                    
        line_count += 1
   
    #bpy.context.scene.objects.active = camera_object
    #bpy.ops.nla.bake(frame_start=0, frame_end=frame, clear_constraints=True, bake_types={'OBJECT'})

