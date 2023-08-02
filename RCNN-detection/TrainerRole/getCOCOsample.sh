#/bin/bash
curl -L -o https://github.com/matterport/Mask_RCNN/releases/download/v2.1/balloon_dataset.zip 
unzip -n ./balloon_dataset.zip 'balloon/*' -d ./dectrainer/src/CoCoSample/
rm ./balloon_dataset.zip
