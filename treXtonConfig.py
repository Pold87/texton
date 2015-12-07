import configargparse

parser = configargparse.ArgumentParser(default_config_files=['treXton.ini'])

parser.add_argument("--dev", type=int, help="Camera index", default=0)
parser.add_argument("-nc", "--channels", type=int, help="Number of channels (1: grayscale, 3: color)", default=3)
parser.add_argument("-nd", "--num_draug_pics", type=int, help="The amount of draug pictures to use", default=300)
parser.add_argument("-nv", "--num_valid_pics", type=int, help="The amount of valid pictures to use", default=49)
parser.add_argument("-sv", "--start_valid", type=int, help="Filenumber of the first valid picture", default=0)
parser.add_argument("-t", "--num_test_pics", type=int, help="The amount of test images to use", default=40)
parser.add_argument("-d", "--dir", default="../draug/genimgs_folder/", help="Path to draug directory")    
parser.add_argument("-tp", "--test_imgs_path", default="../draug/genimgs_folder/", help="Path to test images")
parser.add_argument("-s", "--start_pic_num", type=int, default=20, help="Discard the first pictures (offset)")
parser.add_argument("-g", "--show_graphs", help="Show graphs of textons", action="store_true")
parser.add_argument("-ttr", "--test_on_trainset", help="Test on trainset (calculate training error)", action="store_true")
parser.add_argument("-tte", "--test_on_testset", help="Test on testset (calculate error)", action="store_true")
parser.add_argument("-tv", "--test_on_validset", help="Test on validset (calculate valid error)", action="store_true")
parser.add_argument("-nt", "--num_textons", help="Size of texton dictionary", type=int, default=30)
parser.add_argument("-mt", "--max_textons", help="Maximum amount of textons per image", type=int, default=700)
parser.add_argument("-o", "--use_optitrack", help="Use optitrack", action="store_true")
parser.add_argument("-ts", "--texton_size", help="Size of the textons", type=int, default=5)
parser.add_argument("-c", "--clustering", default=False, help="Do clustering or load clusters from file", action="store_true")
parser.add_argument("-tfidf", "--tfidf", default=False, help="Perform tfidf", action="store_true")
parser.add_argument("-std", "--standardize", default=False, help="Perform standarization", action="store_true")
parser.add_argument("-ds", "--do_separate", default=False, help="Use two classifiers (x and y)", action="store_true")
parser.add_argument("-udf", "--use_draug_folder", default=False, help="Use picture enhanced by draug (folder)", action="store_true")
parser.add_argument("-cs", "--color_standardize", default=False, help="Standardize channel 2 and 3 by dividing them by channel 1", action="store_true")
parser.add_argument("-hs", "--histogram_standardize", default=False, help="Standardize the (grayscale) picture using histogram equalization", action="store_true")
parser.add_argument("-ud", "--use_dipoles", default=False, help="Standardize the (grayscale) picture using histogram equalization", action="store_true")
parser.add_argument("-ls", "--local_standardize", default=False, help="Use local standardization", action="store_true")
parser.add_argument("-gtl", "--ground_truth_labeler", help="Path of SIFT ground truth csv file")
parser.add_argument("-m", "--mymap", default="../draug/img/bestnewmat.png", help="Path to the mat image")
parser.add_argument("-mo", "--mode", default=0, help="Use the camera (0), test on train pictures (1), test on test pictures (2)", type=int)
parser.add_argument("-p", "--predictions", default="predictions.npy", help="Path to the predictions of extract_textons_draug.py")
parser.add_argument("-f", "--filter", default=False, help="Use Kalman filter for filtering", action="store_true")
parser.add_argument("-us", "--use_sift", default=False, help="Use SIFT from OpenCV to display its estimation", action="store_true")
parser.add_argument("-un", "--use_normal", default=False, help="Use normal drone to display its estimation", action="store_true")
parser.add_argument("-ug", "--use_ground_truth", default=False, help="Use SIFT from OpenCV to display its estimation", action="store_true")
parser.add_argument("--load_histograms", default=False, help="Load previously saved histograms", action="store_true")
parser.add_argument("--load_clf_settings", default=False, help="Load previously saved classifier", action="store_true")

if __name__ == "__main__":
   args = parser.parse_known_args()
