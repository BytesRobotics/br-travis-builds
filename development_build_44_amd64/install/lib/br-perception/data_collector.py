#!/usr/bin/env python2
import rospy
from std_msgs.msg import Bool, String
from sensor_msgs.msg import NavSatFix, Image
from geometry_msgs.msg import Twist, PoseArray
import os, time, datetime, csv, cv2, sys
from cv_bridge import CvBridge, CvBridgeError

# Connect to the remote storage device - not implemented yet
# from ftplib import FTP
# ftp = FTP("192.168.1.1")
# # ftp.connect('ftp://192.168.1.1/sda1/', 21)
# ftp.login('admin','password')
# ftp.dir()
# ftp.cwd('sda1')
# ftp.quit()

class DataCollector:
    def __init__(self):
        rospy.loginfo("Data collector starting...")

        # Create the cv_bridge object
        self.bridge = CvBridge()

        self.data_collection_rate = rospy.get_param("~data_collection_rate", 5.0) # Hz
        self.multicam = rospy.get_param("~multicam", False)
        self.data_root_dir = rospy.get_param("~data_root_dir", "/media/data_usb")
        self.dataset_name = rospy.get_param("~dataset_name", "dataset")

        self.field_names = ['time_stamp', 'x', 'r','lat_raw', 'long_raw', 'lat_filtered', 'long_filtered', 'nav_path', 'multicam', 'date']

        # topics for controlling data collection
        rospy.Subscriber("is_data_collecting", Bool, self.data_collecting_status_cb, queue_size=10)
        self.collect_data = False
        self.collection_timer = rospy.Timer(rospy.Duration(1.0/self.data_collection_rate), self.collect_data_cb)


        # subscribe to latest drive commands from joy (x,r)
        rospy.Subscriber('/mobile_base_controller/cmd_vel', Twist, self.cmd_cb, queue_size=1)
        self.last_cmd = None

        # define subscribers for the image topics and variable to store the last image from each topic
        rospy.Subscriber("/camera/camera/image_rect_color", Image, self.center_camera_cb, queue_size=1)
        self.last_front_image = None
        rospy.Subscriber("/camera_r/camera/image_rect_color", Image, self.right_camera_cb, queue_size=1)
        self.last_right_image = None
        rospy.Subscriber("/camera_l/camera/image_rect_color", Image, self.left_camera_cb, queue_size=1)
        self.last_left_image = None

        # subscribe to GPS topics
        rospy.Subscriber("/gps", NavSatFix, self.gps_unfiltered_cb, queue_size=1)
        self.last_gps_unfiltered = None
        rospy.Subscriber("/gps/filtered/utm", NavSatFix, self.gps_filtered_cb, queue_size=1)
        self.last_gps_filtered = None

        # The navsat goal path used for generating the navigation data
        rospy.Subscriber("data_collector/nav_points", PoseArray, self.nav_points_cb, queue_size=10)
        rospy.Subscriber("data_collector/nav_file", String, self.nav_file_cb, queue_size=10)
        self.nav_path = None # array [[lat1, long1], [lat2,long2], ...] Note the order from A->B


    def data_collecting_status_cb(self, msg):
        last_state = self.collect_data
        self.collect_data = msg.data
        if last_state != self.collect_data:
            if self.collect_data:
                rospy.loginfo("Collecting Data")
            else:
                rospy.loginfo("Not Collecting Data")

    def nav_points_cb(self, msg):
        poses = msg.poses
        self.nav_path = []
        for pose in poses:
            self.nav_path.append([pose.position.x, pose.position.y])
        rospy.loginfo("New nav path data uploaded!")
        rospy.logdebug(self.nav_path)

    def nav_file_cb(self, msg):
        if os.path.exists(msg.data):
            self.nav_path = []
            with open(msg.data) as file:
                csvreader = csv.reader(file, delimiter=',')
                csvreader.next() # clear the header
                for row in csvreader:
                    self.nav_path.append([row[0], row[1]])
            rospy.loginfo("New nav path data uploaded!")
            rospy.logdebug(self.nav_path)
        else:
            rospy.logerr("File does not exist!")

    def cmd_cb(self, msg):
        self.last_cmd = msg

    def gps_unfiltered_cb(self, msg):
        self.last_gps_unfiltered = msg

    def gps_filtered_cb(self, msg):
        self.last_gps_filtered = msg

    def center_camera_cb(self, image):
        try:
            self.last_front_image = self.bridge.imgmsg_to_cv2(image, desired_encoding="bgr8")
        except CvBridgeError as e:
            self.get_logger().error(e)

    def right_camera_cb(self, image):
        try:
            self.last_right_image = self.bridge.imgmsg_to_cv2(image, desired_encoding="bgr8")
        except CvBridgeError as e:
            self.get_logger().error(e)

    def left_camera_cb(self, image):
        try:
            self.last_left_image = self.bridge.imgmsg_to_cv2(image, desired_encoding="bgr8")
        except CvBridgeError as e:
            self.get_logger().error(e)

    def collect_data_cb(self, event):

        if self.nav_path is None:
            rospy.logdebug("No nav path is currently defined")

        if self.collect_data and not (self.last_front_image is None or self.last_cmd is None):
            rospy.logdebug("Logging data")
            folder = self.dataset_name
            root_dir = self.data_root_dir
            dataset_dir = os.path.join(root_dir, folder)
            time_stamp = time.time()
            date = datetime.date.today()

            if not os.path.isdir(root_dir):
                rospy.logerr("Data collection root dir does not exists: " + root_dir)
                sys.exit(1)

            if not os.path.isdir(dataset_dir):  # check if dataset already exists, else create it
                os.mkdir(dataset_dir)
                os.mkdir(os.path.join(dataset_dir, "center_images"))
                os.mkdir(os.path.join(dataset_dir, "left_images"))
                os.mkdir(os.path.join(dataset_dir, "right_images"))
                with open(os.path.join(dataset_dir, "tags.csv"), 'w+') as csvfile:  # csv in test folder
                    # ['time_stamp', 'x', 'r','lat_raw', 'long_raw', 'lat_filtered', 'long_filtered', 'nav_path', 'multicam', 'date]
                    csv_writer = csv.DictWriter(csvfile, self.field_names)
                    csv_writer.writeheader()

            if self.multicam and not (self.last_right_image is None or self.last_left_image is None):
                rospy.logdebug("Logging multicam")
                cv2.imwrite(os.path.join(dataset_dir, "left_images/" + str(time_stamp) + ".jpg"), self.last_left_image)  # write image into test folder
                cv2.imwrite(os.path.join(dataset_dir, "right_images/" + str(time_stamp) + ".jpg"), self.last_right_image)  # write image into test folder

            # save all that data
            cv2.imwrite(os.path.join(dataset_dir, "center_images/" + str(time_stamp) + ".jpg"), self.last_front_image)  # write image into test folder

            with open(os.path.join(dataset_dir, "tags.csv"), 'a') as csvfile: # append to csv file
                csv_writer = csv.writer(csvfile, self.field_names)
                new_data = [str(time_stamp), str(self.last_cmd.linear.x), str(self.last_cmd.angular.z),
                            str(self.last_gps_unfiltered.latitude), str(self.last_gps_unfiltered.longitude), str(self.last_gps_filtered.latitude),
                            str(self.last_gps_filtered.longitude), str(self.nav_path), str(self.multicam), str(date)]
                csv_writer.writerow(new_data)

if __name__ == '__main__':
    rospy.init_node("data_collector")
    data_collector = DataCollector()
    rospy.spin()
