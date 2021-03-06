import argparse

def parse_train_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--loss', type=str, choices=['vae', 'bvae', 'bce', 'btcvae'],
                        help='The loss function to use', default='bce')

    parser.add_argument('--binvox_dir', type=str,
                        help='Volumetric data directory.',
                        default=None)

    parser.add_argument('--image_dir', type=str,
                        help='Image data directory.',
                        default=None)

    parser.add_argument('--dataset_scale', type=tuple,
                        help='training_dataset_scale : testing_dataset_scale',
                        default=(0.8, 0.2))

    parser.add_argument('--graph_dir', type=str,
                        help='The directory to write the training graphs.',
                        default='../graphs/Celeb_A/')

    parser.add_argument('--save_dir', type=str,
                        help='The directory to save the trained model.',
                        default='../saved_models/')

    parser.add_argument('--test_image_folder', type=str,
                        help='The directory of the test images.',
                        default='../test_images/')

    parser.add_argument('--latent_vector_size', type=int,
                        help='The size of the embedding layers.',
                        default=128)

    parser.add_argument('--val_split', type=float,
                        help='The percentage of generated_data in the validation set',
                        default=0.2)

    parser.add_argument('--batch_size', type=int,
                        help='Batch size for training.',
                        default=16)

    parser.add_argument('--val_batch_size', type=int,
                        help='Batch size for validation.',
                        default=64)

    parser.add_argument('--optimizer', type=str, choices=['ADAGRAD', 'ADADELTA', 'ADAM', 'RMSPROP', 'SGD'],
                        help='The optimization algorithm to use', default='ADAM')

    parser.add_argument('--initial_learning_rate', type=float,
                        help='The initial learning rate for the training.',
                        default=0.002)

    parser.add_argument('--num_epochs', type=int,
                        help='The total number of epochs for training.',
                        default=120)

    parser.add_argument('--scheduler_epoch', type=int,
                        help='The number of epochs to wait for the val loss to improve.',
                        default=10)

    parser.add_argument('--decay_factor', type=float,
                        help='The learning rate decay factor.',
                        default=0.1)

    parser.add_argument('--beta', type=float,
                        help='The vae regularizer.',
                        default=1.5)

    parser.add_argument('--capacity', type=float,
                        help='The latent space capacity.',
                        default=10.0)

    parser.add_argument('--max_epochs', type=float,
                        help='The maximum epoch to linearly increase the vae capacity.',
                        default=100)

    parser.add_argument('--num_workers', type=float,
                        help='The number of workers to use during training.',
                        default=8)

    parser.add_argument('--multi_process', type=bool,
                        help='Use multi-processing for dit generator during training.',
                        default=True)

    parser.add_argument('--processed_dataset', type=str,
                        help='The processed dataset contains image and voxel data for all classes',
                        default=None)

    parser.add_argument('--modelnet_voxel_dataset', type=str,
                        help='The modelnet dataset contains voxel data for all classes',
                        default=None)

    parser.add_argument('--modelnet_image_dataset', type=str,
                        help='The modelnet dataset contains image data for all classes',
                        default=None)


    return parser.parse_args(argv)

def parse_test_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--weights_file', type=str,
                        help='the path of weights in .h5 file.',
                        default=None)

    parser.add_argument('--weights_dir', type=str,
                        help='the dictionary that save all of weights of momels in .h5 file.',
                        default=None)

    parser.add_argument('--input_form', type=str, choices=['voxel', 'image', 'both'],
                        help='The input form of test model', default=None)

    parser.add_argument('--voxel_data_dir', type=str,
                        help='the path of test data in .binvox.',
                        default=None)

    parser.add_argument('--image_data_dir', type=str,
                        help='the path of test image data.',
                        default=None)

    parser.add_argument('--model_dir', type=str,
                        help='the path trained model in .h5 form',
                        default=None)

    parser.add_argument('--save_dir', type=str,
                        help='The directory to save the test data.',
                        default='../saved_models/')

    parser.add_argument('--save_ori', type=int,
                        help='Save the original test data in the save_dir.',
                        default=0)

    parser.add_argument('--save_bin', type=int,
                        help='Save the reconstructed data in .binvox',
                        default=0)

    parser.add_argument('--generate_img', type=int,
                        help='Generate images from .binvox files',
                        default=0)

    parser.add_argument('--latent_vector_size', type=int,
                        help='The size of the embedding layers.',
                        default=128)

    parser.add_argument('--dataset', type=str, choices=['shapenet', 'modelnet'],
                        help='the dataset we use ', default='shapenet')

    parser.add_argument('--batch_size', type=int,
                        help='the size of mini_batch', default=32)

    parser.add_argument('--generation', type=int,
                        help='Generate object in testing, 1: True, 0: False', default=0)

    parser.add_argument('--voxel_npz', type=str,
                        help='the path of voxel data in .npz form',
                        default=None)

    parser.add_argument('--image_npz', type=str,
                        help='the path of image data(only object index) in .npz form',
                        default=None)

    parser.add_argument('--modelnet_voxel_dataset', type=str,
                        help='The modelnet dataset contains voxel data for all classes',
                        default=None)

    parser.add_argument('--modelnet_image_dataset', type=str,
                        help='The modelnet dataset contains image data for all classes',
                        default=None)


    return parser.parse_args(argv)

def parse_dataset_arguments(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument('--category_list', nargs='+',
                        help='the category list in the dataset,each element in the list is a 8-digits string',
                        default=None)

    parser.add_argument('--original_dataset_path', type=str,
                        help='the path of original dataset',
                        default=None)

    parser.add_argument('--voxel_dataset_path', type=str,
                        help='the path of volumetric data of a category',
                        default=None)

    parser.add_argument('--image_dataset_path', type=str,
                        help='the path of image data of a category',
                        default=None)

    parser.add_argument('--split_scale', nargs='+', type=float,
                        help='ration for train and test data',
                        default=None)

    parser.add_argument('--save_path', type=str,
                        help='the path to save the processed dataset',
                        default=None)

    parser.add_argument('--sub_num', type=int,
                        help='the number of elements in test_sub dataset',
                        default=100)
    return parser.parse_args(argv)


