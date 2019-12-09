python3 test_lanenet.py --weights_path ./model/tusimple_lanenet_vgg/tusimple_lanenet_vgg.ckpt --image_path `./data/tusimple_test_image/0.jpg`
python3 evaluate_lanenet_on_tusimple.py  --image_dir ./test_output --weights_path ./model/tusimple_lanenet_vgg/tusimple_lanenet_vgg.ckpt --save_dir ./test

python3 lanenet_data_feed_pipline.py --dataset_dir ./data/training_data_example --tfrecords_dir ./data/training_data_example/tfrecords
python train_lanenet.py --net vgg  --dataset_dir ./data/training_data_example -m 0

cv2.circle(frame, (int(frame.shape[0]*5/6), int(frame.shape[1]*2/5)), 30, (0, 0, 255), -1)
