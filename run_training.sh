
python train_MMI_all.py --loss vae  \
                --binvox_dir /home/zmy/Datasets/3d-r2n2-datasat/03001627_processed/voxel/train \
                --image_dir /home/zmy/Datasets/3d-r2n2-datasat/03001627_processed/image/train \
                --processed_dataset /home/zmy/Datasets/3d-r2n2-datasat_processed \
                --save_dir /home/zmy/TrainingData/2021.2.17 \
                --num_epochs 5 \
                --batch_size 4 \
                --initial_learning_rate 0.002 \
                --beta 1 \
                --latent_vector_size 128

