#!/usr/bin/env python
import rospy
import rosgraph.masterapi 
 
def listener():

    #Saves file every "time_to_save_file_in_sec" seconds and runs 50 times a second.
    node_rate =  50
    time_to_save_file_in_sec = 2
    rate = rospy.Rate(node_rate)
    master = rosgraph.masterapi.Master('/rostopic')
    count = 0
    
    while not rospy.is_shutdown():
        topics_list = master.getPublishedTopics('/') 
        count =  count +1
        if (count %(node_rate * time_to_save_file_in_sec) == 0):
            print ("List of topics Saved.")
            topic_file = open('output/topic_names.txt', 'w')
            for item in topics_list:
                topic_file.write("%s\n" % item)
            topic_file.close()
        rate.sleep()
     

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    listener()
