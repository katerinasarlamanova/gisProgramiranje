import os
import PhotoScan


print("Script started")

doc = PhotoScan.app.document
chunk = doc.addChunk()

path_photos = PhotoScan.app.getExistingDirectory("Specify folder with input photos:")

# checking save filename
project_path = PhotoScan.app.getSaveFileName("Specify project filename for saving:")
if not project_path:
    print("Script aborted")

if project_path[-4:].lower() != ".psz":
    project_path += ".psz"

# adding photos
image_list = os.listdir(path_photos)

for photo in image_list:
    if (".jpg" or ".jpeg" or ".tif" or ".png") in photo.lower():
        chunk.addPhotos([path_photos + "\\" + photo])

PhotoScan.app.update()

# align photos
chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, preselection=PhotoScan.NoPreselection, filter_mask=False, keypoint_limit=40000, tiepoint_limit=4000)
chunk.alignCameras()

# build dense cloud
chunk.buildDenseCloud(quality=PhotoScan.MediumQuality, filter=PhotoScan.AggressiveFiltering)

# build mesh
chunk.buildModel(surface=PhotoScan.Arbitrary, source=PhotoScan.DenseCloudData, interpolation=PhotoScan.EnabledInterpolation, face_count=PhotoScan.HighFaceCount)

# build texture
chunk.buildUV(mapping=PhotoScan.GenericMapping)
chunk.buildTexture(blending=PhotoScan.MosaicBlending, color_correction=False, size=4096)

# save
doc.save(project_path)

PhotoScan.app.update()
print("Script finished")