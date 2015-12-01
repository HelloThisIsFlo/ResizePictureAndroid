# ResizePictureAndroid

This tiny program resizes sample pictures for Android Projects.

The problem with sample pictures is that : 
 * If they are too low resolution and in xxhdpi folder, they will be even more downscaled for hdpi/mdpi/ldpi/etc ...
 * If they are too high resolution and in ldpi folder, they still be upscaled for xhdpi/xxhdpi/etc ... resulting in OOM Error
 
The solution is to resize sample pictures to a base width while keeping the aspect ratio, regarding of their original resolution.
Of course this solution is just a quick fix that should only be used with sample images that won't be included in production.
